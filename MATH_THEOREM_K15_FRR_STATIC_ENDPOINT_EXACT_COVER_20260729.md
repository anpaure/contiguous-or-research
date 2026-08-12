# Source-relative `FRR(7,4)`: a static 2,426-variable endpoint exact cover

> **Verdict update.**  The arbitrary-budget extension of this system is now
> closed: compatible endpoint/upper closure supports at most 41
> four-separated cut orbits, whereas the bad-run collars require at least
> 60.  See `MATH_NOGO_K15_FRR_EQUIVARIANT_60_VS_41_20260729.md` for the
> audited 41 witness and verified DRAT upper certificate.  The formulation
> below remains the exact reduction from which that no-go is derived.

## 0. Result

For the saved `6390+45` source factor, the exact minimum-collar,
`Z_15`-equivariant instance of Theorem 4B.1 can be written as one **static**
zero-one feasibility system with

\[
                 426+2000=2426
\]

primary variables and 2,987 rows.  It simultaneously chooses the 60 cut
edge orbits and the residence-compatible rethreading seams.  It is exact at
this scale: a feasible point is a source-relative `FRR(7,4)` certificate,
and every 60-orbit equivariant certificate covered by Theorem 4B.1 gives a
feasible point.

This removes the need for residence CEGAR for this lane.  The capped endpoint
traces are source-fixed once retained paths are required to have length at
least four.

The deterministic audit is

```text
scratch/audit_k15_frr_static_endpoint_exact_cover_20260729.py
scratch/k15_frr_static_endpoint_exact_cover_20260729.audit.json
scratch/k15_frr_static_endpoint_exact_cover_20260729.opb
```

with SHA-256 values

```text
3f7d27bf55b5538b80d3aefa9bfaf0bc5d0083055628b8246aaad59366df7d00  script
da9880eee49fbadf8899f64601a94c9d15106bcb2dd7b09c14263014efedb2b2  output
b1148b8231c1eae6c0394d0736f6ad552df140459891d28e41a5043478d9eea8  OPB
```

This note gives the reduction and the first fixed-witness obstruction.  The
subsequent `60>41` theorem gives the feasibility verdict for the entire
equivariant source-relative class.

## 1. Static endpoint types

Index the 426 edge orbits of the voltage-four large facet component by
`h in Z_426`.  Cutting orbit `h` exposes two endpoint orbits:

\[
 L_h=X_h,\qquad R_h=X_{h+1}.
\]

The inward direction at `L_h` is backward on the source cycle and the inward
direction at `R_h` is forward.  Let

\[
 \tau_x(L_h),\tau_x(R_h)\in\{1,2,3,4\}
\]

be the capped length of the constant source trace in that direction.

If two cut orbits have cyclic distance at least four, their retained path has
at least four vertices.  Therefore the first four inward source states at
every endpoint remain present regardless of the other cuts.  In particular,
all `tau` values are functions of the source and `(h,side)` alone.

For endpoint types `e,f` and relative physical rotation `delta in Z_15`, put
`v_f^delta=rho^delta(v_f)`.  The triple `(e,f,delta)` is an admissible seam
orbit when

1. `v_e` and `v_f^delta` are Johnson adjacent;
2. their union is one of the 426 large-component upper-colour orbits; and
3. the exact compatibility inequalities hold:

\[
\begin{cases}
 \tau_x(e)+\tau_x(f^\delta)\ge4,
   &1_{x\in v_e}=1_{x\in v_f^\delta},\\
 \tau_x(e)=\tau_x(f^\delta)=4,
   &1_{x\in v_e}\ne1_{x\in v_f^\delta}.
\end{cases}                                      \tag{1.1}
\]

These are exactly (4.8).  The source audit finds **2,000** admissible seam
orbits on the 852 endpoint types.  This includes a cut old edge when its
re-addition itself passes (1.1); such a nominal cut cannot fake the collar
condition, because cut spacing permits only one selected edge in a bad
four-edge collar.

The catalogue already contains useful unary information:

* 23 endpoint types have degree zero;
* 11 of the 426 upper colours occur on no admissible seam; and
* of the 335 rank-six rotation orbits, 14 occur on no admissible seam.

Six of the last 14 have old load one.  Consequently the cut owners

\[
                 83,86,150,175,255,408             \tag{1.2}
\]

are forbidden in every feasible minimum-collar solution: cutting one deletes
its unique lower-colour orbit and no compatible seam in the entire catalogue
can restore it.

## 2. Exact Boolean system

Use variables

\[
 z_h\in\{0,1\}\quad(h\in\mathbb Z_{426}),
 \qquad y_s\in\{0,1\}\quad(s\in\mathcal S),
\]

where `z_h=1` means that old edge orbit `h` is cut and `y_s=1` means that
compatible seam orbit `s` is selected.

For a seam `s`, write

* `partial s={e_s,f_s}` for its two endpoint types;
* `o(e_s),o(f_s)` for their cut owners;
* `u(s)` for its upper-colour orbit; and
* `a_s(R)` for its contribution to one physical member of rank-six orbit
  `R`.

For an old cut orbit `h`, let `c_h(R)` be the load removed from one physical
member of `R`, and let `lambda_0(R)` be its old load.  The exceptional
rank-six orbits have size five; accordingly the only coefficients are one
and three.  The audit gives

\[
\begin{array}{c|cc}
 &1&3\\ \hline
 c_h(R)\ne0&425&1\\
 a_s(R)\ne0&1996&4.
\end{array}                                      \tag{2.1}
\]

The system is:

\[
 \sum_hz_h=60,                                    \tag{2.2}
\]

\[
 \sum_{h\in C}z_h\ge1
       \quad\hbox{for each of the 95 bad-run collars }C,      \tag{2.3}
\]

\[
 z_h+z_{h+j}\le1
       \quad(h\in\mathbb Z_{426},\ 1\le j\le3),             \tag{2.4}
\]

\[
 \sum_{s:e\in\partial s}y_s=z_{o(e)}
       \quad\hbox{for every one of the 852 endpoint types }e,\tag{2.5}
\]

\[
 \sum_{s:u(s)=h}y_s=z_h
       \quad(h\in\mathbb Z_{426}),                           \tag{2.6}
\]

and

\[
 \lambda_0(R)-\sum_hc_h(R)z_h+\sum_sa_s(R)y_s\ge1
       \quad\hbox{for all 335 rank-six orbits }R.             \tag{2.7}
\]

There are no hidden phase variables.  Selecting one seam orbit matches all
15 physical endpoints in that orbit.  Equation (2.5) is the endpoint perfect
matching, (2.6) is the upper rainbow, and (2.7) is the exact lower rainbow.

### Theorem 2.1 (exactness)

The zero-one solutions of (2.2)--(2.7) are in bijection with the
`Z_15`-equivariant, 60-cut-orbit repairs of `B_0` satisfying all five
hypotheses of Theorem 4B.1.

#### Proof

Given a solution, let `H={h:z_h=1}`.  Equations (2.3) and (2.4) say that
`H` hits every old length-three collar and every retained path has at least
four vertices.  By (2.5), the selected seam orbits match every exposed
endpoint exactly once and use no unexposed endpoint.  Every selected seam
passes (1.1).  Equation (2.6) says that its upper colours are precisely the
cut colours, once each.  Equation (2.7) is the literal post-switch lower
load, including the two exceptional size-five orbits.  Theorem 4B.1 now
gives the repaired factor.

Conversely, take an equivariant repair from Theorem 4B.1 and set `z_h` and
`y_s` to its cut and seam orbits.  The five hypotheses give (2.3)--(2.7),
and the minimum cut cardinality gives (2.2).  QED.

The audited row count is

\[
1+95+1278+852+426+335=2987.                       \tag{2.8}
\]

Thus the complete source-relative minimum-collar search has 2,426 primary
bits and 2,987 sparse rows.  For comparison, the unrestricted quotient turn
selector has `429*28=12012` primary choices before its trace clauses.  The
new reduction is about five times smaller and searches the cut set and the
rethreading together, unlike the earlier 1,620-variable fixed-`H` model.

## 3. What fails for the existing minimum witnesses

The 60-orbit witness which minimizes the number of cut load-one colours in
the earlier frontier audit is not a candidate for Theorem 4B.1:

1. its minimum cyclic cut gap is three, producing exactly 60 physical
   retained paths of length three; and
2. even ignoring those short paths, 47 of its 60 selected upper colours
   have no compatible seam whose two endpoint owners and upper colour all
   lie in that witness.

The latter domain histogram is

\[
                   0^{47}\,1^{12}\,3^1.            \tag{3.1}
\]

This is an explicit obstruction to that fixed minimum transversal, before
degree balance or lower-colour restoration is considered.

The path-length requirement does **not** increase the collar transversal
number.  A second exact width-three cyclic DP finds a spacing-safe
60-orbit transversal.  But an arbitrary such witness is still far from a
rethread: the audited witness has seam-colour domain histogram

\[
                   0^{45}\,1^{13}\,2^2.            \tag{3.2}
\]

So the correct problem is not "find a collar transversal, then match its
endpoints."  The cut bits and seam bits must be solved simultaneously by
(2.2)--(2.7).

Finally, the old frontier theorem remains active inside (2.7): every
60-orbit collar transversal cuts at least 12 globally load-one lower-colour
orbits.  Hence at least 12 selected seam orbits must restore 12 prescribed
distinct lower colours.  This is the exact lower-rainbow tax, not an
objective-function heuristic.

## 4. Capped H100 CPU run and outcome

The finite verdict was run as one static CP-SAT model, not as residence
CEGAR:

1. generate the catalogue and coefficients locally with the audited script;
2. instantiate (2.2)--(2.7) as 2,426 Boolean variables and 2,987 linear
   rows;
3. first solve (2.2)--(2.6), then add (2.7) to distinguish endpoint-rainbow
   infeasibility from the forced lower-colour obstruction;
4. on SAT, materialize all 6,435 physical edges and independently replay
   degree, both q1 palettes, component length, and every coordinate trace.

The H100 run used four CPU workers, a hard 4 GiB address-space cap, and a
one-hour solver limit.  The endpoint/upper stage returned exact INFEASIBLE
in presolve in 0.0117 seconds; no resource limit was hit.  A separate
arbitrary-budget maximization plus a verified DRAT certificate strengthened
this to the exact closure ceiling 41.  The full lower stage is unnecessary.

## 5. Meaning for `FRR(7,4)`

The source-relative lane is now one sharply bounded exact-cover problem.
The deterministic facts are mixed:

* the minimum collar size 60 survives the retained-path constraint;
* the minimum-load-one witness itself is decisively incompatible;
* seam compatibility is sparse enough to create 23 dead endpoint types and
  11 dead upper colours; but
* no collar is supported only on dead owners, so these unary obstructions do
  not prove global infeasibility.

Accordingly, (2.2)--(2.7) was the smallest justified finite target, and its
arbitrary-budget endpoint relaxation supplies the stronger no-go.  Larger
equivariant cut sets do not help.  Nonequivariant rethreads and unrelated
`RTR(7,4)` factors remain open.
