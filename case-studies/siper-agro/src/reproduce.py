"""Public independent arithmetic reconstruction of SIPER-AGRO's synthetic demo.

This is NOT the proprietary SIPER-AGRO engine, its risk model or its security layer.
Only explicit relation IDs are grouped; no implied joins or currency conversions.
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_transactions.csv"
EXPECTED_UNITS = {"inventory": "TN", "settlements": "ARS", "logistics": "ARS", "prices": "ARS/TN"}


def compute(path: Path = DATA) -> list[dict[str, str]]:
    groups = defaultdict(lambda: defaultdict(list))
    seen = set()
    with Path(path).open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            family, relation, role, record = (row[k].strip() for k in ("family", "relation_id", "role", "record_id"))
            if family not in EXPECTED_UNITS or not relation or not record:
                raise ValueError("Unknown family or missing explicit relation/record ID")
            if row["unit"].strip() != EXPECTED_UNITS[family]:
                raise ValueError("Unit mismatch: conversion is intentionally prohibited")
            identity = (family, relation, role, record)
            if identity in seen:
                raise ValueError("Duplicate record within an explicit relation")
            seen.add(identity)
            try:
                value = Decimal(row["value"])
            except InvalidOperation as error:
                raise ValueError("Non-numeric source record") from error
            if not value.is_finite():
                raise ValueError("Non-finite source record")
            groups[(family, relation)][role].append(value)

    def one(roles, name):
        values = roles.get(name, [])
        if len(values) != 1:
            raise ValueError(f"Expected one {name}, got {len(values)}")
        return values[0]

    results = []
    for (family, relation), roles in sorted(groups.items()):
        permitted = {
            "inventory": {"opening", "purchase", "sale", "closing"},
            "settlements": {"settlement", "payment"},
            "logistics": {"logistics", "ledger_cost"},
            "prices": {"purchase_price", "sale_price"},
        }[family]
        if not set(roles).issubset(permitted):
            raise ValueError("Invalid role for relation family")
        if family == "inventory":
            if not roles.get("purchase") or not roles.get("sale"):
                raise ValueError("Inventory relation needs purchases and sales")
            delta = one(roles, "closing") - (one(roles, "opening") + sum(roles["purchase"]) - sum(roles["sale"]))
        elif family == "settlements":
            if not roles.get("payment"):
                raise ValueError("Settlement requires explicit payments")
            delta = sum(roles["payment"]) - one(roles, "settlement")
        elif family == "logistics":
            if not roles.get("ledger_cost"):
                raise ValueError("Logistics needs an independent cost ledger")
            delta = one(roles, "logistics") - sum(roles["ledger_cost"])
        else:
            delta = one(roles, "sale_price") - one(roles, "purchase_price")
        results.append({"family": family, "relation_id": relation, "difference": str(delta),
                        "unit": EXPECTED_UNITS[family], "status": "REVIEW" if delta else "MATCH"})
    if not results:
        raise ValueError("No explicit reconciliations")
    return results


if __name__ == "__main__":
    print(json.dumps({"source": "SYNTHETIC_CONTROLLED", "economic_authority": "NONE",
                      "reconciliations": compute()}, ensure_ascii=False, indent=2))
