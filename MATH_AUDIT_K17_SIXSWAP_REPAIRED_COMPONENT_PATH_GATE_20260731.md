# Six occurrence swaps clean the marked forest, but one component has no clean fixed-port connector

Date: 2026-07-31  
Status: exact source-relative replay and solver-free fixed-endpoint no-go; no
`K17` word or unrestricted obstruction is claimed

## Result

The six certified changes of the retained rank-six occurrence are

```text
z= 9486  (0,4064) -> (0,5826)
z=16502  (0,1781) -> (0,6254)
z= 1675  (0,1997) -> (0,5349)
z= 2829  (0,2849) -> (0,6201)
z=22632  (0,1571) -> (0,4923)
z=26800  (0,2423) -> (0,5775)
```

An independent reconstruction from the authenticated parent gives:

* 1430 literal A/X/Y macros and 19305 distinct macro-owner tokens;
* a macro-port linear forest with 5005 components and degree profile
  `0^4016 1^1978 2^441`;
* 108 forced macros in 106 components;
* component closure 154 macros, 46 optional macros, 3815 owner tokens; and
* zero strict internal `D2<3` and zero strict internal `D3<4` runs in every
  one of the 106 marked components.

Thus the six swaps genuinely remove the former component-interior residence
obstruction.

They do not close the fixed-port component path.  One singleton component,
canonical local index 77, is

```text
macro order       [18]
required macros   [18]
ports             [16638,22835]
endpoint owners   [82174,55603]
owner count       111
```

It has three undirected neighbouring components through two old-U labels,
hence six directed oriented incidences.  Every one creates exactly one new owner run of length
two and one adjacent-OR run of length three.  The responsible coordinates
are 0, 9, or 14.  Therefore component 77 has no incoming and no outgoing
residence-clean connector in either orientation.  A Hamilton path through
all 106 components is impossible in this fixed-port, one-old-U-per-join
face.

## Exact connector definition

For an oriented marked component `C`, let `t(C)` be its exposed tail port and
`W(C)` its literal owner word.  For oriented distinct `C,D`, the stored ports
permit at most one pure old-U connector:

\[
 U=t(C)\cup h(D).
\]

It is geometric iff `|U|=9` and the two rank-eight ports differ in exactly
two coordinates.  It is residence-clean iff

\[
                 W(C),U,W(D)
\]

has no strict internal positive run below three and its adjacent-OR
derivative has none below four.

The repaired catalogue contains 412 geometric directed arcs, 312 clean arcs,
and 140 distinct old-U labels.  The six literal failed arcs incident with
component 77 are emitted in the audit JSON, including both bad-run ledgers.

This definition retains the stored macro endpoint incidences.  It does not
cover endpoint-facet recolouring, an optional-atom bridge, a longer old-U
chain, or a nonflat socket exchange.

## Port Hall is not the obstruction

Before fixing any marked connectors, the exact residual network

\[
 s\longrightarrow {\cal U}\longrightarrow {\cal T}\longrightarrow t,
 \qquad
 {cal U}=\binom{[15]}9,
 \quad {cal T}=\binom{[15]}8,
\]

has supply two at every old-U owner, unit containment arcs, and demand
`2-deg_P(T)` at every port.  Independent Dinic replay gives

\[
                         10010/10010.
\]

So the unconditioned generalized Hall system is feasible.

If a 105-edge marked path existed, its fixed graph would have

\[
 5005-105=4900
\]

components, and exactly 4900 old-U owners and 9800 port incidences would
remain.  The scalar identities therefore close exactly.  Component 77 kills
the path before conditioned Hall or connected residual completion is
relevant.

## Smallest exact augmented master

The fixed-port master uses one Boolean for each of the 312 clean labelled
arcs, one orientation per component, a dummy-vertex circuit constraint to
make a Hamilton path, and

\[
                     \sum_{a:u(a)=u}x_a\le1
\]

for old-U owner uniqueness.  It is immediately inconsistent because
component 77 has empty incident support.

The minimal open extension must add at least one **socket actuator** incident
with component 77.  Each augmented arc must explicitly record:

1. the occurrence-labelled endpoint incidence removed or recoloured;
2. every inserted owner and rank-eight lower colour;
3. the exact capped D2/D3 boundary signature;
4. the old-U and lower-colour capacity consumed; and
5. the displaced incidence exported to the complementary bank.

After a marked candidate is fixed, residual feasibility remains one integral
max-flow test.  With fixed incidence set `F`, a source-side owner set `A` and
lower-colour set `B` must satisfy

\[
 \sum_{v\in A}(2-\deg_F(v))
 \le
 \sum_{L\in B}(2-\deg_F(L))
 +e_{\rm free}(A,{\cal L}\setminus B).
\]

A failed cut is a linear Benders row on the selected augmented connectors.
A passing flow gives only a degree-two factor.  To make the marked bank and
its complement each contiguous, contract the marked path and impose the
usual quotient connectivity cuts

\[
                 \sum_{e\in\delta(Q)}z_e\ge2
 \quad(\varnothing\ne Q\subsetneq\text{quotient vertices}).
\]

Thus the exact gate order is:

```text
one component-77 socket -> labelled 106-component path
                        -> conditioned residual Hall
                        -> quotient connectedness
                        -> deeper service/common cap
```

## Reproduction and scope

```text
python3 scratch/audit_k17_sixswap_repaired_component_flow_gate_20260731.py
python3 -m py_compile scratch/audit_k17_sixswap_repaired_component_flow_gate_20260731.py
```

The audit reconstructs the six moves and every headline count from the
parent, forced-pattern map, and census certificate.  It does not invoke a SAT
or CP solver.  The no-go applies only to the repaired fixed macro forest with
stored endpoint ports and one pure old-U owner at each marked join.
