# Independent audit of the one-collar rooted target reduction

Date: 2026-08-01  
Scope: `MATH_THEOREM_O1_H1_ROOTED_ROTATING_HOLE_EXACT_GATE_AND_FINITE_BASES_20260801.md`  
Verdict: **PASS with the stated conditional all-dimensional scope.**

## 1. Proof audit

The directed certificate is exact.  A directed q1-rainbow factor is the
union of two incidence perfect matchings, represented by the tail and head
bijections `t,s`.  Its owner cycles are exactly the cycles of
`s compose t^{-1}`, and the adjacent-upper colour on the occurrence `q` is
`t(q) union s(q)`.  Thus planted orientation, one-cycle topology, and paired
upper surjectivity are three genuinely correlated rows.

The bare reverse/cut statement is also exact.  Reversal creates two residual
cycles in addition to the intended resident sidecar.  Choosing one common
cut on each while retaining every upper colour is precisely the stated
two-left-node capacitated Hall problem with capacities `mu(R)-1`.  The
frozen `m=4,h=1` fixture is a valid counterexample to automatic safe cutting:
all common edges on its residual five-cycle are unique upper providers.
This does not refute existence of a more favourable rooted target.

For the insured collar, the connector `D-T-C` has two new lower colours and
one repeated upper colour `R`.  It makes the plus support one directed path.
After reversal it is a monochromatic-upper triangle, so one connector cut is
safe.  In any upper-surjective `W`-edge factor, at least
`Delta+1`, `Delta=W-binomial(2m-1,m+1)=2W/(m+1)`, edge occurrences have a
repeated upper colour.  Since `Delta+1>h+7` for `m>=4`, `h<=m-3`, one such
edge lies outside the protected path, hence on the unchanged bulk path, and
is a safe second common cut.  The two cut q1 colours are distinct by q1
injectivity.

The protected Catalan-connector equivalence is exact after fixing the first
incidence matching `M0` (or existentially quantifying it together with all
other layers).  The tail and head incidence classes of the directed planted
path are respectively `P0,P1`.  The union `Q0 union Q1` is required to be a
matching, not merely two edge-disjoint matchings.  Its link graph is a
spanning directed path.  The last residual edge must lie outside `M0`; this
closes the path rather than making a rooted loop.  Conversely, deleting one
upper-transparent unprotected second-matching edge from a rooted Hamilton
factor yields exactly these layers.

No step proves the missing all-dimensional existence of the protected
upper-surjective Hamilton completion.  The theorem correctly leaves that
statement open and does not infer the full contiguous-OR result.

## 2. Replay audit

The following independent replays all pass:

```text
PASS_O1_ML7_ALIGNED_COLLAR_UPPER_UNSAFE_COMMON_CUT
payload_sha256=bafd0e21af3b6c06f01022976c388b94fed7dcdee4cdb5ca70b1866e963a4f85

PASS_O1_SHORTEST_COLLAR_UPPER_INSURANCE_CONNECTOR
cases=84
payload_sha256=ab2ee14d5ccb34109efe666b378d0a004e0b9e79c1bd25b68b80342ec4a0512d

PASS_ROOTED_ROTATING_HOLE_UPPER_FINITE_REPLAY
payload_sha256=43d932505e2d835c09ae7c3df61f6aff1a7a2604520d55fc0922b0910cf8ea43

PASS_INSURED_ROTATING_HOLE_UPPER_FINITE_REPLAY
payload_sha256=66c07a1bbb2748394568d7922c4711d76490845f20c88a00b090dbfd2407afe1
```

The finite tables for every legal bare depth at `m=4,5`, every
connector-legal insured depth there, all component sizes, and all safe-cut
counts agree with the frozen search artifacts.  Coordinate transitivity
extends each canonical witness to every legal relabelling in that same
finite dimension only.

## 3. Exact conclusion

The strongest audited conclusion is conditional but dimension-uniform:

> If the insured directed collar path has an adjacent-upper-surjective
> q1-rainbow Hamilton completion, then reversal and two common cuts preserve
> the adjacent-upper palette automatically for all `m>=4` and
> `1<=h<=m-3`.

The remaining all-dimensional gate is exactly the protected rooted
Catalan-connector completion.  The finite positive bases and the unsafe-cut
fixture neither prove nor refute that gate.
