# Audit and exact variable-path extension of the generalized Pascal braid

Date: 2026-07-29  
Lane: AD  
Status: equations audited; fixed-path artifacts replayed; exact segment-LNS
implemented and solver-free audited; no new H100 job launched while the host
is saturated

## 1. Verdict

The six generalized-braid equation families in

```text
MATH_THEOREM_GENERALIZED_PASCAL_BRAID_LINEAR_MODEL_20260729.md
scratch/solve_k15_generalized_pascal_braid.py
```

are mathematically correct.  Their original theorem statement mislabelled
two physical ranks; that statement is now corrected.  Both lower sectors
have child rank `m`, and both upper sectors have child rank `m+2`.

The frozen solver snapshot that produced the diagnostic artifacts,

```text
scratch/k15_generalized_pascal_braid_20260729/
```

is not fully fail-closed.  It uses removable Python assertions for critical
input and postsolve checks, does not validate the full path deck, accepts an
incompatible minimization flag combination, overwrites raw `OPTIMAL` in its
JSON, omits the objective bound and provenance hashes, and does not
independently postverify a single active upper channel.  Positive artifacts
below were therefore replayed from their literal selected edges.  Negative
and optimality claims retain trusted CP-SAT/log scope.

The apparent upper-channel obstruction is now closed positively.  The fixed
path has a physical factor satisfying both upper-q1 sectors simultaneously:

```text
scratch/k15_generalized_pascal_braid/full_q1_s15105.json
SHA-256 e8092469c88b0a224bf0b11ed2661e06b5de260cc349717ea704732f47e00f29
log SHA-256 f9c502ee22aa659ca496fd1388727d449ff5ae72c8336840b71a79d638403143
```

The run imposed the no-z channel and maximized z-upper distinct coverage;
CP-SAT returned `OPTIMAL`, objective and bound `3003`.  Independent literal
replay gives zero holes in both sectors, exact lower q1, and degree two.
Thus there is no fixed-path z/no-z infeasibility or shared-controller
capacity obstruction at q1.  Its distinguished-coordinate forest still has
97 short components, and the completed factor has 1,527 total residence
defects.

Hard z-residence is already infeasible when both upper families are absent.
Therefore that fixed-path obstruction cannot arise from upper-channel
interaction.  The exact lower/degree optimum is 17 short AA components, 13
of length two and four of length three.  This number is proved only for
equations (2.1)--(2.4) on the frozen path; the 17 displayed locations form
one optimum, not a universal positional core.

The new implementation

```text
scratch/solve_k15_generalized_pascal_segment_lns_ad.py
SHA-256 71a131d58b2d2b018e0ef01e85164b8ff6d549ad83ac32dffab49a05a0a05042
```

jointly changes the k14 Hamilton chronology and AA selection.  Its exact
305-segment neighbourhood has 512 orientation states, 6,359 active directed
segment arcs, 6,331 candidate physical AA edges, and 50,977 AA wedges.  It
can solve the AA projection or the complete cross/BB braid, impose either
upper channel, minimize the exact short-component count, or require hard
z-residence.  It is H100 guarded, uses no exactness assertions, validates
the model, hash-binds all inputs/model/source, preserves raw solver status
and bound, and exhaustively decodes the literal Hamilton path and factor.

## 2. Correct equation theorem

Let `n=2m`, let `z` be new, and split the rank-`m+1` child middle deck into

\[
 A=z+\binom{[2m]}m,\qquad B=\binom{[2m]}{m+1}.
\]

For an AA edge `TT'`, use `x_(TT')`; for a containment `T subset U`, use
cross variable `c_(T,U)`; and for an unordered BB Johnson edge `U_1U_2`,
with intersection `T`, use `y_(T;U_1,U_2)`.  Equations (2.1)--(2.6) are

\[
 \sum_{TT':T\cap T'=X}x_{TT'}=1
 \quad\left(X\in\binom{[2m]}{m-1}\right),               \tag{2.1}
\]

\[
 d_A(T)+\sum_{U\supset T}c_{T,U}=2,                    \tag{2.2}
\]

\[
 \sum_{U\supset T}c_{T,U}+
 \sum_{U_1\cap U_2=T}y_{T;U_1,U_2}=1,                 \tag{2.3}
\]

\[
 \sum_{T\subset U}c_{T,U}+
 \sum_{U'\sim U}y_{U\cap U';U,U'}=2,                 \tag{2.4}
\]

\[
 \sum_{TT':T\cup T'=U}x_{TT'}+sum_{T\subset U}c_{T,U}\ge1,
                                                                    \tag{2.5}
\]

\[
 \sum_{U_1\cup U_2=V}y_{U_1\cap U_2;U_1,U_2}\ge1.   \tag{2.6}
\]

The selected AA, cross, and BB edges give degree two at every child middle
vertex by (2.2) and (2.4).  Equation (2.1) enumerates exactly

\[
 z+\binom{[2m]}{m-1},
\]

while (2.3) enumerates exactly `C([2m],m)`; together these are all rank-`m`
lower q1 colours.  Equation (2.5) covers exactly
`z+C([2m],m+1)`, while (2.6) covers `C([2m],m+2)`; together these are all
rank-`m+2` upper q1 colours.  This proves the two-sector theorem.

Combining (2.2) and (2.3), with `C_T` and `Y_T` the cross and BB loads of
lower label `T`, gives

\[
 C_T=2-d_A(T),\qquad Y_T=d_A(T)-1.                    \tag{2.7}
\]

Since the AA graph is contained in a path, `d_A(T)<=2`; nonnegativity in
(2.7) gives `d_A(T)>=1`.  Hence it is a spanning path forest.  For `m=7`,

\[
 AA=3003,\qquad \#\text{AA paths}=429,\qquad
 cross=858,\qquad BB=2574.                             \tag{2.8}
\]

## 3. Exact controller projection and channel interaction

Fix an AA selection and write `E={T:d_A(T)=1}` and
`I={T:d_A(T)=2}`.  Equations (2.2)--(2.3) have the exact following
interpretation:

* each `T in E` chooses one extension coordinate `a notin T`, hence the
  cross edge from `z+T` to `T+a`;
* each `T in I` chooses one unordered extension pair `{a,b}`, hence the BB
  edge `(T+a)(T+b)`.

Write that singleton or pair as `S_T`.  Equation (2.4) is precisely

\[
 \sum_{T=U-\{a\}}1[a\in S_T]=2
 \qquad\left(U\in\binom{[14]}8\right).                 \tag{3.1}
\]

Conversely, any such `S_T` family reconstructs a unique cross/BB assignment
satisfying (2.2)--(2.4).  If

\[
 A_U(x)=\sum_{i:T_i\cup T_{i+1}=U}x_i,
\]

then the z channel is

\[
 A_U(x)+\sum_{\substack{T\in E,,T\subset U\\S_T=U-T}}1\ge1,       \tag{3.2}
\]

and the no-z channel is

\[
 \sum_{\substack{\{a,b\}\subset V\\
 T=V-\{a,b\}\in I\\S_T=\{a,b\}}}1\ge1.              \tag{3.3}
\]

Thus the only possible fixed-`x` interaction is the shared rank-eight
capacity ledger (3.1).  The full-q1 artifact realizes (3.1)--(3.3), so this
possible interaction is not an obstruction for the fixed path.

## 4. Exact residence objective and calibrated scope

For the fixed path with `N=3432` vertices, let `x_i` select path edge
`i(i+1)` and put

\[
 c_{-1}=c_{N-1}=1,\qquad c_i=1-x_i.
\]

For `ell in {2,3}`, define

\[
 w_{s,\ell}=c_{s-1}c_{s+\ell-1}
             \prod_{j=s}^{s+\ell-2}x_j.               \tag{4.1}
\]

It equals one exactly when an AA component of `ell` vertices begins at `s`.
Isolated vertices are impossible by (2.7).  Therefore

\[
 D(x)=\sum_s w_{s,2}+\sum_s w_{s,3}                   \tag{4.2}
\]

is exactly the number of z-residence defects.  The source uses 3,431
length-two and 3,430 length-three exact conjunction variables, including
the two virtual boundary cuts.

The retained log SHA

```text
5399609f9a94055555778f2d0369334b84aca3f30d4af71ffc1e16b745107836
```

records model fingerprint `0x1f36fd04ef9d386c`, `OPTIMAL`, objective 17,
and best bound 17 after 62.55 seconds.  The JSON witness independently
replays as 429 AA paths, degree histogram `858 x 1 + 2574 x 2`, and short
histogram `13 x 2 + 4 x 3`.  Both upper flags were skipped.  Consequently:

\[
 \min\{D(x):(2.1)\text{--}(2.4)\text{ on this fixed path}\}=17.     \tag{4.3}
\]

This is a trusted-solver finite optimum, not a solver-independent
combinatorial lower-bound certificate.  The JSON alone does not prove the
bound because the old source overwrote raw status and omitted
`BestObjectiveBound`.  No independently checkable `D<=16` UNSAT core was
exported; the exact objective formulation and retained CP-SAT optimum/bound
are the available certificate boundary.

Hard residence is `D=0`.  Artifact `diag_res.json` is `INFEASIBLE` with
both (2.5) and (2.6) skipped.  This proves the residence obstruction is
already in the lower/degree system, not in either upper channel.

## 5. Exact minimal chronology change

The 17 short components in the displayed optimum occupy 55 distinct path
cuts: every motif contributes its internal selected edges and its two
bracketing cuts.  A nontrivial Hamilton path with the same endpoints must
delete at least two old edges and add at least two new ones.  Equality is a
2-opt reversal

\[
 (v_0,\ldots,v_i,v_j,v_{j-1},\ldots,v_{i+1},v_{j+1},\ldots,v_{N-1}),
                                                                    \tag{5.1}
\]

where `j>=i+2` and the two new seams satisfy

\[
 v_i\sim v_j,\qquad v_{i+1}\sim v_{j+1}.               \tag{5.2}
\]

Indeed, the symmetric difference of two same-endpoint Hamilton paths is a
union of alternating cycles; its smallest nonempty member has two edges of
each path, and cutting/rejoining one interval gives (5.1).

Exact enumeration restricted to reversals deleting at least one of the 55
motif cuts gives 278 moves.  Their partner palette contains 304 cuts.  This
278-way disjunction is the smallest nontrivial exact same-endpoint LNS.  It
is an exact declared neighbourhood, but targeting those 55 cuts is heuristic
relative to all possible path changes because motif positions need not be
invariant across fixed-path optima.

## 6. The 305-segment path theorem

Cut the base path at the 304-cut palette.  This leaves 305 intact segments,
98 singletons and 207 nonsingletons.  Give a singleton one orientation state
and every other segment two.  Hence there are

\[
 98+2(207)=512                                             \tag{6.1}
\]

states.  A directed state arc is allowed exactly when the exit mask of the
first state and entry mask of the second state are Johnson-adjacent.  There
are 6,408 raw arcs; after fixing the original first segment forward as source
and the original last segment forward as sink, 6,359 remain active.

### Theorem 6.1 (exact segment chronology)

The orientation, predecessor/successor, and order constraints in the new
source are feasible if and only if there is a same-endpoint rank-seven
Hamilton path obtained by ordering and orienting all 305 palette segments.

#### Proof

Exactly one orientation is selected for every segment.  Each selected state
except the fixed source has one incoming arc; each except the fixed sink has
one outgoing arc.  Unselected states have neither.  If an arc goes from
segment `s` to `t`, its order variables satisfy

\[
                         pi_t=pi_s+1.                    \tag{6.2}
\]

The 305 segment orders are all different in `[0,304]`, with source zero and
sink 304.  Equation (6.2) forbids every directed subtour and forces one path
through all segments.  Allowed arcs make every new seam Johnson-legal;
internal segment edges were already path edges.  Concatenation therefore
gives the asserted literal Hamilton path.  Conversely, any such ordered and
oriented segment path sets exactly those states, arcs, and order values and
satisfies all constraints.  ∎

The raw arc projection contains 3,204 distinct physical seam edges.  The
segments retain 3,127 internal edges, disjoint from the seam set.  Hence the
AA candidate graph has 6,331 physical edges.

For every palette cut `c`, let `b_c` indicate retention of its original
physical seam.  Then

\[
                         Delta=\sum_c(1-b_c)             \tag{6.3}
\]

is exactly the number of deleted base edges and, because endpoints and edge
counts are fixed, the number of new seams.  `Delta<=2` plus at least one
changed motif cut projects exactly to the 278 reversals.  Larger seam budgets
give exact compound segment-braid neighbourhoods without freezing AA
selection.

## 7. Exact chronology-independent short-component objective

Let `a_e` select a candidate AA edge and

\[
 d_T=\sum_{e\ni T}a_e=1+p_T,qquad p_T\in\{0,1\}.       \tag{7.1}
\]

Thus `p_T=0` exactly at an AA-path endpoint.  For each candidate edge
`e=uv`, define

\[
 L^2_e=a_e(1-p_u)(1-p_v).                               \tag{7.2}
\]

For every unordered wedge `u-v-w`, define

\[
 L^3_{u,v,w}=a_{uv}a_{vw}(1-p_u)(1-p_w).                \tag{7.3}
\]

Because the selected AA graph is a spanning subgraph of one Hamilton path,
it is a path forest.  Equation (7.2) counts each two-vertex component once;
(7.3) counts each three-vertex component at its unique centre.  Neither can
fire on a longer component.  Therefore

\[
 D=\sum_eL^2_e+\sum_{u-v-w}L^3_{u,v,w}                 \tag{7.4}
\]

is the exact short-AA count for every variable chronology in the segment
neighbourhood.  The candidate graph has 50,977 wedges.  Setting `D=0`
imposes hard z-residence.  The implementation uses the smaller equivalent
edge/wedge inequalities when only `D=0` is needed and exact conjunction
variables only for optimization or a positive upper bound.

## 8. Fail-closed implementation boundary

The frozen fixed-path solver SHA is

```text
b2549f2bfa0fdf9444f81f9e4b72262eda8111ebbf969510f89697c67848b9b1.
```

The later full-q1 run came from the evolving root source rather than that
frozen snapshot.  Its positive mathematical content does not depend on
source reconstruction: the audit rechecks every cross containment, BB
intersection/union label, physical-edge distinctness, owner degree, lower
colour, upper colour, and resulting factor cycle directly from the saved
selection.  Its `OPTIMAL 3003/3003` search-history claim retains the frozen
result/log hashes stated in Section 1.

Its equations are correct, but its negative/status interface has these exact
defects:

1. critical validation and postsolve checks are `assert` statements and
   disappear under `python -O`;
2. path validation does not explicitly prove equality with the entire
   rank-seven deck or reject out-of-universe masks;
3. `--minimize-z-defects` without `--no-z-residence` minimizes an empty
   objective on top of hard residence;
4. successful JSON replaces `OPTIMAL`/`FEASIBLE` by
   `FEASIBLE_VERIFIED_FACTOR` and omits the best bound;
5. a single active upper channel is not separately postverified;
6. no `model.Validate()`, source/path/proto hashes, OR-Tools version, hostname,
   or normalized negative scope are recorded;
7. there is no H100-only guard.

The new AD segment source closes all seven for its own model.  It never uses
`assert` for exactness, checks the complete deck, rejects incompatible flags,
guards host `arboghast`, calls `model.Validate()`, stores raw solver status,
objective and bound, hashes all artifacts and the proto, decodes the literal
Hamilton path, verifies selected AA edges against that path, and rechecks all
active braid channels.  Any `INFEASIBLE` result remains scoped to the frozen
path-derived 304-cut palette and declared seam/upper/residence bounds; it is
not a global k14 chronology obstruction.

The companion solver-free reproducer is

```text
scratch/audit_ad_generalized_pascal_braid_and_segment_lns_20260729.py.
SHA-256 1811d21e4b3823077b9abbac699979a658d2bcfa81c2df4363b75684be30fb77
```

It independently replays equations (2.1)--(2.4) for every stored positive
artifact, verifies both upper sectors in the full-q1 artifact, parses the two
retained optimality logs, and reconstructs every segment catalogue count and
canonical catalogue SHA

```text
960ca7cb27a38b33d44c88ea02f8b2ae67392ff0fb2b3d7019f37a609fcb6380.
```

It contains no Python `assert`; ordinary and `python -O` executions produce
byte-identical `PASS` reports.

## 9. H100 run boundary

**Later audited update.**  The launch plan below is historical.  The exact
no-seam-budget hard-residence job PID 3123570 terminated raw `UNKNOWN` after
7,214.8 solver seconds and proved neither feasibility nor infeasibility.  Do
not treat that timeout as a palette closure.  The separate fixed-path s15106
minimization terminated raw `FEASIBLE`, objective 29, best bound 17.
Literal replay verifies both upper sectors, but 29 is not optimal.  The
authoritative follow-up, including the stronger solver-free edit-radius-five
bound, is

```text
MATH_CODE_AUDIT_AD_PASCAL_LIVE305_AND_EDIT5_CEGAR_20260729.md.
```

No segment-LNS worker was launched in this audit because H100 was explicitly
reported saturated.  The next exact sequence, once existing batches finish,
is:

1. AA-only, `Delta<=2`, motif change required, minimize `D`; this tests the
   complete 278-reversal neighbourhood with globally free AA selection.
2. If it reaches `D<=16`, keep the decoded path and test the complete
   cross/BB controller with both q1 channels.
3. Increase the seam budget to three and four, then remove the budget within
   the 305-segment palette.
4. Test `D=0` only after a strict objective improvement, because the fixed
   path lower/degree system already proves that endpoint impossible.

The first full-q1 command is, schematically,

```text
python3 scratch/solve_k15_generalized_pascal_segment_lns_ad.py \
  --z-upper --noz-upper --minimize-short \
  --seam-budget 2 --require-motif-change \
  --path scratch/k14_common_colour_3opt_best_20260729.json \
  --hint-factor scratch/k15_generalized_pascal_braid/full_q1_s15105.json \
  --output UNIQUE_RESULT.json
```

It preserves both exact lower decks through (2.1)--(2.4) and both complete
upper decks through (2.5)--(2.6) while changing chronology and AA selection
jointly.  No AA Hamming-radius constraint is present.

The now-completed fixed-path full-q1 minimization is separate: it returned a
feasible incumbent 29 with bound 17 after one hour.  This does not change the
fixed-path hard-residence infeasibility or the exactness of the variable-path
model.

## 10. Claude c-space transfer audit

The inspected c-space source is

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/cword.py
SHA-256 0ef27d86befe5e3d0b2598ce371a22a35d9709c4b7898e6dff0c82b272003ab4
```

Its central reduction is exact only inside an odd, cyclic,
coordinate-shift-equivariant voltage spiral.  In that class one binary trace
`c` determines every coordinate trace by shifts; residue-class sums enforce
middle rank, forbidden cyclic patterns `0 1^j 0` enforce residence, and one
representative seam's XOR count enforces all rotated Johnson seams.  Orbit
coverage plus the fixed number of columns then gives a Hamilton cycle.

None of the single-trace, residue-class, orbit-representative, or
"connectivity free" reductions is valid for the unrestricted even k14
Hamilton path or the 305-segment chronology.  Importing any of them would
silently replace the requested path-changing neighbourhood by a highly
symmetric subclass.

Three generic Boolean devices are transferable and exact:

1. a forbidden-run clause is an exact residence constraint once a literal
   coordinate trace chronology is already fixed;
2. a Hamming-radius inequality is an exact *declared neighbourhood* bound,
   never a validity-preserving global cut;
3. an OR of exact selector conjunctions is an exact existential fixed-window
   cover constraint, provided every legal window/width is included.

The segment model already uses the first idea in its sharper
chronology-independent edge/wedge form and uses physical seam distance
`Delta` instead of an arbitrary bit radius.  Its q1 channels are direct
complete equations, so selector expansion adds nothing.  The c-space upper
CEGAR source tests only a chosen finite width list; that is a scoped
restriction, not a transferable all-interval theorem.  The stochastic
`anneal2.cpp` machinery supplies no exact constraint.  Accordingly no
c-space symmetry constraint was added to the AD model.
