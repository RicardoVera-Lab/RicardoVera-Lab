"""New public, deliberately small simulation of one reversible pilot slot.

Not a production authorization, identity, or audit system. These are public
explanatory rules, not a port of a private execution engine.
"""
from __future__ import annotations
import re
from dataclasses import dataclass

ID_PATTERN = re.compile(r'^(?:SYN|EVT|EXE|REV)-[A-Z0-9]+(?:-[A-Z0-9]+)*$')

class ControlStop(ValueError):
    pass


def canonical_id(value: object) -> str:
    if not isinstance(value, str) or not ID_PATTERN.fullmatch(value):
        raise ControlStop('INVALID_CANONICAL_ID')
    return value


@dataclass
class PilotSlot:
    """Single-slot state transitions; synthetic IDs are never real signatures."""
    slot_owner: str | None = None
    status: str = 'FREE'
    execution_id: str | None = None

    def reserve(self, pilot_id: str) -> str:
        canonical_id(pilot_id)
        if self.status != 'FREE':
            raise ControlStop('SLOT_OCCUPIED')
        self.slot_owner = pilot_id
        self.status = 'RESERVED'
        return self.status

    def execute(self, pilot_id: str, execution_id: str) -> str:
        canonical_id(pilot_id)
        canonical_id(execution_id)
        if self.status != 'RESERVED' or pilot_id != self.slot_owner:
            raise ControlStop('NOT_RESERVED_FOR_PILOT')
        self.execution_id = execution_id
        self.status = 'EXECUTED'
        return self.status

    def cancel(self, pilot_id: str) -> str:
        canonical_id(pilot_id)
        if pilot_id != self.slot_owner:
            raise ControlStop('OWNER_MISMATCH')
        if self.status == 'EXECUTED':
            raise ControlStop('REVERSAL_REQUIRED_AFTER_EXECUTION')
        if self.status != 'RESERVED':
            raise ControlStop('NOT_CANCELLABLE')
        self._release()
        return 'RELEASED_PRE_EXECUTION'

    def rollback(self, pilot_id: str, execution_id: str, reversal_id: str) -> str:
        canonical_id(pilot_id)
        canonical_id(execution_id)
        canonical_id(reversal_id)
        if self.status != 'EXECUTED' or pilot_id != self.slot_owner:
            raise ControlStop('NO_EXECUTED_PILOT')
        if execution_id != self.execution_id:
            raise ControlStop('INVALID_REVERSAL_REFERENCE')
        # Evidence of a matching reversal is the supplied explicit reference in
        # this simplified event model, not proof of a physical undo.
        self._release()
        return 'RELEASED_AFTER_MATCHED_REVERSAL'

    def _release(self) -> None:
        self.status = 'FREE'
        self.slot_owner = None
        self.execution_id = None


def demonstration() -> dict:
    pre = PilotSlot(); pre.reserve('SYN-A'); pre_cancel = pre.cancel('SYN-A')
    post = PilotSlot(); post.reserve('SYN-B'); post.execute('SYN-B', 'EXE-001')
    try:
        post.cancel('SYN-B')
    except ControlStop as exc:
        post_cancel = str(exc)
    else:
        raise AssertionError('Post-execution cancellation should stop')
    retained_while_stopped = post.status == 'EXECUTED' and post.slot_owner == 'SYN-B'
    try:
        post.rollback('SYN-B', 'EXE-WRONG', 'REV-001')
    except ControlStop as exc:
        bad_reverse = str(exc)
    else:
        raise AssertionError('Bad reversal should stop')
    rollback_result = post.rollback('SYN-B', 'EXE-001', 'REV-002')
    invalid_id_rejected = False
    try:
        PilotSlot().reserve('  ')
    except ControlStop:
        invalid_id_rejected = True
    return {'pre_execution_cancellation': pre_cancel, 'slot_after_pre_cancel': pre.status,
            'post_execution_cancellation': post_cancel,
            'post_execution_slot_retained': retained_while_stopped,
            'bad_reversal': bad_reverse, 'valid_reversal': rollback_result,
            'slot_after_valid_reversal': post.status, 'invalid_id_rejected': invalid_id_rejected}

if __name__ == '__main__':
    import json
    print(json.dumps(demonstration(), indent=2, ensure_ascii=False))
