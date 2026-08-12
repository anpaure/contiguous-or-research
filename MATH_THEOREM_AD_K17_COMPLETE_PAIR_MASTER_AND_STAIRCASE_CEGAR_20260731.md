# K17 fixed-tripleflow complete pair master and exact staircase CEGAR

Date: 2026-07-31  
Status: proved encoding and solver-free census; 21-component q1 factor replayed; no K17 word  
Scope: completions containing the authenticated fixed tripleflow path bank

## 0. Verdict

The arbitrary 989-cycle tripleflow output is only a feasibility witness.  It
does prove that the integrated path bank can be completed to an exact
lower-rainbow 2-factor, but it does not solve any of the decisive chronology
gates.

There is, however, an exact next master which is both smaller and cleaner than
an occurrence-level direct-formula model.  Freeze the 1,430 authenticated
paths.  For every unused rank-eight colour, use one Boolean for each possible
unordered pair of residual rank-nine endpoints.  Exact-one colour rows and
exact residual owner-degree rows describe **all** lower-rainbow 2-factor
completions containing the frozen bank.  Eager rank-ten union ALOs impose the
complete immediate upper shadow.

The complete fixed-core master has

\[
 524642\text{ variables},\qquad
 34320\text{ nontrivial equality rows},\qquad
 13541\text{ upper ALO rows}.
\]

Thus it has 47,861 substantive initial rows.  Every variable upper row has
between 2 and 44 providers.  In particular, the reported 1,916 combined
singleton provider rows are all already-fixed internal edges and force no
decision variable.

Connectivity has the exact ordinary subtour separator

\[
  \sum_{e\in\delta(S)}x_e\ge2
\]

for every incumbent component shore.  Residence must **not** be replaced by
global minimum-run-four cuts: the fixed bank already contains sealed internal
length-three runs.  For a connected candidate, one compact CP model chooses
the orientation, cyclic opening, and the exact K17 arbitrary-start
\(\delta/\tau\) staircase.  By default it also requires the removed edge's
rank-ten union to have another selected provider, so the opened path retains
upper q1.  If both orientations are rigorously infeasible, the whole residual
factor is excluded by one exact no-good.  This gives a finite, complete CEGAR
scheme for the frozen-core, q1-safe-opening subclass.  Q1 safety is sufficient,
not WLOG if a later boundary/compiler cell is allowed to restore the deleted
rank-ten colour; the checker has a scalar-only mode for that broader ledger.

An independently replayed upper-q1-complete factor with 21 components now
exists.  No connected such factor, staircase-feasible chronology, envelope,
deeper upper certificate, or compiler is claimed here.

## 1. Frozen data

Let

\[
 V_9=\binom{[17]}9,\quad V_8=\binom{[17]}8,\quad
 V_{10}=\binom{[17]}{10}.
\]

The fixed source is

```text
scratch/k17_pbbs_u_yaux_tripleflow_bridge_20260731.fragments
SHA256 0f6267a487916ff2ee2aa04b3656d4a2b24aa7a72a057e87c39b381cfddfa25d
```

It is a vertex-disjoint union \(F\) of 1,430 nontrivial Johnson paths.  Exact
replay gives:

\[
 |V(F)|=9295,\qquad |E(F)|=7865.
\]

The 7,865 intersections \(u\cap v\), \(uv\in E(F)\), are pairwise distinct.
The fixed edges have 5,907 distinct rank-ten unions, with multiplicity
histogram

\[
 1^{4127},\quad2^{1606},\quad3^{170},\quad4^4.
\]

For every owner \(v\in V_9\), put

\[
 d(v)=2-\deg_F(v).
\]

The exact demand histogram is

\[
 d=0:6435,\qquad d=1:2860,\qquad d=2:15015.
\]

There are 16,445 unused lower colours and

\[
 \sum_{v\in V_9}d(v)=2(16445).
\]

## 2. Complete residual-pair theorem

For every unused colour \(c\in V_8\), define

\[
 \mathcal P_c=
 \left\{
  \{u,v\}: u,v\in V_9, u\ne v, c\subset u,v, d(u),d(v)>0
 \right\}.
\]

Because \(|c|=8\) and \(|u|=|v|=9\), every member of \(\mathcal P_c\)
is a Johnson edge with

\[
 u\cap v=c.
\]

Introduce \(x_{c;u,v}\in\{0,1\}\) for each such unordered pair.

### Theorem 2.1 (exact fixed-core factor master)

The solutions of

\[
 \sum_{\{u,v\}\in\mathcal P_c}x_{c;u,v}=1
 \qquad(c\in V_8\setminus\{a\cap b:ab\in E(F)\}),                 \tag{2.1}
\]

and

\[
 \sum_{c}\sum_{\substack{\{u,v\}\in\mathcal P_c\\w\in\{u,v\}}}
 x_{c;u,v}=d(w)
 \qquad(w\in V_9, d(w)>0)                                      \tag{2.2}
\]

are in bijection with all spanning simple 2-factors \(H\supseteq F\) which
use every rank-eight Johnson colour exactly once.

#### Proof

Given a solution, add the selected pair edge for every unused colour.
Equation (2.1) supplies every missing colour exactly once.  The fixed colours
were already distinct, so every colour in \(V_8\) occurs exactly once.
Equation (2.2), together with the definition of \(d\), makes every owner
degree two.  An edge cannot be duplicated under two colours because its
intersection is unique.  Hence the result is a simple spanning 2-factor.

Conversely, let \(H\) be such a completion.  Every residual edge \(uv\) has
the unique unused colour \(u\cap v\).  Neither endpoint can have zero residual
demand.  Thus \(uv\in\mathcal P_{u\cap v}\).  The lower-rainbow property gives
(2.1), and degree two gives (2.2).  The two constructions are inverse.
\(\square\)

For \(T\in V_{10}\), put

\[
 \mathcal P(T)=\{(c;u,v):\{u,v\}\in\mathcal P_c, u\cup v=T\}.
\]

### Corollary 2.2 (eager upper-q1 equivalence)

For every \(T\) not already equal to the union of a fixed edge, add

\[
 \sum_{(c;u,v)\in\mathcal P(T)}x_{c;u,v}\ge1.                    \tag{2.3}
\]

Then (2.1)--(2.3) describe exactly the lower-rainbow 2-factor completions of
\(F\) whose componentwise cyclic immediate upper shadow is complete.

#### Proof

An adjacent pair with union \(T\) is a literal length-two witness.  Conversely,
any interval of rank-nine owners whose union has rank ten contains an adjacent
change between two distinct rank-nine subsets of that same \(T\); their union
is \(T\).  Therefore a rank-ten target occurs if and only if some selected or
fixed edge has that union.  This is precisely (2.3). \(\square\)

This is an ALO, never an exact-one constraint.  Opening a future Hamilton
cycle can delete a sole provider edge, so boundary restitution remains a
separate linear-word ledger.

## 3. Exact census

The option count by lower-row arity is

\[
 3^1, 6^4, 10^{63}, 15^{458}, 21^{1703},
 28^{3803}, 36^{10413}.
\]

Consequently

\[
 \sum_c|\mathcal P_c|=524642.                                    \tag{3.1}
\]

There are 17,875 positive owner rows, so (2.1)--(2.2) have

\[
 16445+17875=34320                                                 \tag{3.2}
\]

nontrivial equalities.  Exactly 13,541 rank-ten targets are not fixed-covered.
Their ALOs contain 442,396 literal occurrences, with support range

\[
 2\le |\mathcal P(T)|\le44.                                      \tag{3.3}
\]

There is no lower-row singleton, no variable upper-row singleton, and no
initial equality/ALO propagation.  The 1,916 combined-support-one targets are
exactly the targets with one fixed provider and zero variable providers; they
are tautologically discharged.

The solver-free audit is

```text
scratch/audit_ad_k17_tripleflow_complete_pair_master_20260731.py
scratch/ad_k17_tripleflow_complete_pair_master_20260731.audit.json
```

It reconstructs all counts above without instantiating a solver.

### 3.1 Exact incidence projection

The pair master is the cleanest eager proof model, but its lower equations
have an exact smaller projection.  For every admissible incidence
\(c\subset u\), introduce \(y_{c,u}\in\{0,1\}\) and impose

\[
 \sum_{u\supset c}y_{c,u}=2,
 \qquad
 \sum_{c\subset u}y_{c,u}=d(u).                                  \tag{3.4}
\]

The two selected owners in a colour row determine its unordered pair, so
(3.4) is bijective with (2.1)--(2.2), not a relaxation.  The frozen core has
139,144 admissible incidences.  Upper decoration can be separated lazily:
for provider pair \(\{u,v\}\) use a witness

\[
 z_{c;u,v}\Longrightarrow y_{c,u},y_{c,v},
\]

and one ALO over the witnesses of each missing target.  Reverse channeling is
unnecessary for satisfiability because an actual provider can always choose
one witness.  This gives the smaller exact component-search route documented
in `MATH_REDUCTION_K17_DECORATED_INCIDENCE_BMATCHING_20260731.md`; the eager
524,642-variable pair master remains the simplest independent reference and
decoder.

## 4. The smaller structured model is not WLOG

If one additionally forces unattached A owners to use AA and attached A
owners to use their prescribed AX/AY channel, the catalogue shrinks to
349,860 variables.  In that restricted model there are seven singleton AA
rows and one singleton XX row.  Equality/ALO propagation sets exactly those
eight variables true, sets none false, satisfies seven previously missing
upper rows, and stops.  The remaining 13,534 active upper rows have arity
2--36.

This is a legitimate sufficient subclass, but it omits 174,782 residual
Johnson edges and is not equivalent to Theorem 2.1.  In particular the
1,916 combined upper singletons still do not create choice units.

The structured provider audit file has a provenance wrinkle: its full file
replays byte-for-byte, but the embedded payload hash was formed with integer
dictionary keys before JSON serialization.  Re-parsing turns them into
strings and changes the sorted-key hash order.  Use its full-file SHA, or
normalize keys before a future payload freeze.

The eight-unit propagation statement is independently frozen in

```text
scratch/audit_ad_k17_tripleflow_structured_pair_propagation_20260731.py
  SHA256 3e60b95cc6066877d41e5e24ab6a38cb4ca8d77514988d31fad404188a13d971
scratch/ad_k17_tripleflow_structured_pair_propagation_20260731.audit.json
  SHA256 ffb5f18ae2bcac4fda172582215db96d05a9b7754832a47d9e569227a4b73f84
  payload 71939577d67ecc8ad53267aa079a727ea2331965b19423f44e5c5a95b349ffcf
```

## 5. Exact connectivity separator

Let \(H_0\) be an incumbent 2-factor and let
\(S\subsetneq V_9\) be one of its connected components.

### Theorem 5.1 (component shore cut)

Every connected 2-factor completion of the same fixed bank satisfies

\[
 |E(F)\cap\delta(S)|+
 \sum_{c;u,v:\,|\{u,v\}\cap S|=1}x_{c;u,v}\ge2.                 \tag{5.1}
\]

For an incumbent component, every fixed edge is internal, so the constant is
zero.

#### Proof

For any 2-regular graph \(G\),

\[
 |\delta_G(S)|=2|S|-2|E_G[S]|
\]

is even.  If \(G\) is connected and \(S\) is proper and nonempty, the cut is
positive, hence at least two.  Each pair variable represents one physical
edge and therefore has coefficient one. \(\square\)

For an incumbent partition into \(c\ge2\) components, summing (5.1) gives the
weaker but valid aggregate

\[
 \sum_{e\text{ crossing incumbent components}}x_e\ge c.         \tag{5.2}
\]

The individual shore rows are stronger.  Iteratively separating (5.1) is
exact for connectivity under degree two.

## 6. Exact orientation/opening staircase model

Assume the factor master returns one Hamilton cycle

\[
 C=(v_0,v_1,\ldots,v_{W-1}),\qquad W=24310.
\]

Let \(m(T)\) be the number of cycle edges with rank-ten union \(T\).  Opening
before \(v_c\) removes the edge \(v_{c-1}v_c\).  The opening retains the full
upper-q1 palette exactly when

\[
 m(v_{c-1}\cup v_c)\ge2.                                           \tag{6.0}
\]

Fix one orientation temporarily.  Let a cyclic positive coordinate run have
cyclic start \(s\) and length \(\ell\le3\).  If the cycle is opened at index
\(c\), define

\[
 a=(s-c)\bmod W.                                                   \tag{6.1}
\]

The run is a boundary run exactly when

\[
 a=0\quad\text{or}\quad a\ge W-\ell.                              \tag{6.2}
\]

Otherwise it is the interior linear run

\[
 [a,b],\qquad b=a+\ell-1.                                         \tag{6.3}
\]

Choose integers

\[
 7401\ge\delta_1\ge\delta_2\ge\delta_3\ge0,qquad
 0\le\tau_1\le\tau_2\le\tau_3\le7401                            \tag{6.4}
\]

with

\[
 \sum_j\delta_j+\sum_j\tau_j\le7401.                            \tag{6.5}
\]

For an interior run define

\[
 g_{b+1}=\#\{j:\delta_j\ge W-b-1\},qquad
 h_{a-1}=\#\{j:\tau_j<a\}.                                      \tag{6.6}
\]

### Theorem 6.1 (compact exact cycle-staircase test)

For the fixed orientation, a cut and a scalar-feasible exact K17
arbitrary-start staircase exist if and only if (6.1)--(6.6) have an integral
solution satisfying

\[
 h_{a-1}<\ell+g_{b+1}                                              \tag{6.7}
\]

for every interior cyclic run of length at most three.  Adding (6.0) is
necessary and sufficient for the same opening to retain cyclic upper-q1
coverage in the resulting linear path.

#### Proof

Equation (6.0) is exact because the removed adjacent edge is the only cyclic
edge absent from the opened path, and every rank-ten interval contains an
adjacent edge with the same union.  Equation (6.2) is the exact boundary
condition: opening at the run start, inside the run, or at its following zero
removes one of its two bounding zero rows.  Otherwise (6.3) is its literal
position in the opened word.  With
\(b=a+\ell-1\), the start-activation threshold in Theorem 3.2 is

\[
 W-b-1=W-a-\ell,
\]

so (6.6) is exactly its \(g_{b+1}\) and \(h_{a-1}\).  Inequality (6.7) is
the exact run-replay inequality.  Runs of length at least four satisfy it
automatically.  Finally, the K17 separation lemma makes (6.5) equal to the
full loss and automatically gives deadline/start legality and chain
alignment.  Hence these constraints are precisely Theorem 3.2 for a variable
cyclic opening. \(\square\)

Coordinate identity does not occur in (6.7), so coincident pairs
\((s,\ell)\) may be deduplicated.  Repeating the model for the reversed cycle
covers both orientations; arbitrary cuts absorb the one-position convention
change under reversal.

The implementation

```text
scratch/solve_ad_k17_cycle_arbitrary_staircase_20260731.py
```

reconstructs the full loss including the cross term, the explicit thresholds,
all \(s_i,q_i\), chain alignment, every interior-run inequality, and linear
upper-q1 coverage on a SAT output.  It does not test nonempty envelopes.

## 7. Exact finite CEGAR consequence

Let \(R(H)\) be the 16,445 selected residual variables of a connected
candidate \(H\).  If the exact model of Theorem 6.1, including (6.0), is
infeasible in both orientations, then

\[
 \sum_{x\in R(H)}x\le16444                                       \tag{7.1}
\]

is a valid no-good for the simultaneous connected/q1-safe-opening/staircase
target: it excludes exactly that residual factor.  Combining eager (2.3),
component cuts (5.1), and (7.1) gives a finite CEGAR procedure.  It either
returns a connected factor with a q1-safe opening and replayed scalar
staircase, proves no such completion of the frozen bank exists, or reports
UNKNOWN when an inner solve is not certified.

Row (7.1) must not be imported into a broader model which permits loss and
later boundary restitution of the cut's rank-ten colour unless the separate
restoration alternative has first been ruled out.

The pair driver implementing this loop is

```text
scratch/solve_k17_pbbs_u_decorated_residual_factor_cegar_20260731.py
```

It also has an optional all-upper induced-component separator.  Its legacy
`010/0110` motif mode is explicitly opt-in and is not the exact staircase.
Global min-run four cannot be used here: the fixed tripleflow bank has 182
immutable internal length-three occurrences in 157 fixed paths.

A CP-SAT `INFEASIBLE` status is an exact solver result but is not by itself a
DRAT/LRAT proof artifact.  Any published impossibility claim must retain an
independently checkable proof/certificate or state solver scope precisely.

## 8. Baseline measurements and remaining boundary

The original materialized arbitrary residual flow has:

\[
 \begin{array}{c|c}
 \text{components}&989\\
 \text{upper-q1 holes}&4413\\
 \text{all-upper holes}&9103\\
 \text{cyclic run length 2}&7887\\
 \text{cyclic run length 3}&7940.
 \end{array}
\]

Its upper-q1 holes split as

\[
 (00,x,y,xy)=(0,1465,1457,1491).
\]

It is therefore only a historical feasibility hint.

The stronger current hint is

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_20260731.components
SHA256 6b24e8ab4c77e3e5711cacab233db29733e1b27c74b735a8fb84c9a1c3643702
```

It is an exact lower-rainbow and upper-q1-complete factor with 21 components,
component lengths

\[
 9652,7457,3689,2093,1158,114,55,25,14,11,7,6,5,3^8,
\]

and short-run counts

\[
 (N_1,N_2,N_3)=(0,3705,2268).
\]

Its deeper upper deficit is 1,937 in the originating audit.  The core
vertex/edge/lower/q1/run claims have a separate lightweight replay:

```text
scratch/audit_ad_k17_double_rainbow_q1_core_20260731.py
  SHA256 4fb808edb2d7a431fc1b68c781ac24fb9390591edb3a0a482c253226f6c31c36
scratch/ad_k17_double_rainbow_q1_core_20260731.audit.json
  SHA256 d68373c8b32197aa10115f9c784760991f7bf62a1473dafdf22f552861061c2b
  payload dc53daadfb0a2ef2654bf4a514bbb8f57d48e1c456b06093a534e765a5ff5caa
```

This closes feasibility of the immediate upper rows and supplies the correct
component-CEGAR warm start.  It does not close 21-to-1 connectivity.

The exact proved boundary after this note is:

1. the complete fixed-core lower/upper-q1 factor model is exact, has no static
   provider obstruction, and is now known feasible already in the structured
   subcatalogue;
2. connectivity and the scalar staircase now have sound exact CEGAR
   interfaces;
3. no connected solve of the 524,642-variable master is reported here;
4. even a connected/staircase-positive result would still need complete
   deeper upper replay, nonempty envelopes, the lower boundary-hole ledger,
   and the generalized lower common-cap compiler;
5. the frozen fixed bank is itself a restriction on K17 carrier space.

No value of \(\nu(17)\) is claimed.

## 9. Frozen implementation manifest

```text
scratch/solve_k17_pbbs_u_decorated_residual_factor_cegar_20260731.py
  SHA256 7cf106cd951f8eb30ec227e20d2be7caa2296d4816af57b9a4b667801037af31
scratch/solve_ad_k17_cycle_arbitrary_staircase_20260731.py
  SHA256 8b22f99e2207d20a1bfc0819dd96d47220b513c8da7124a78720107b880bb391
scratch/solve_k17_pbbs_u_tripleflow_upper_q1_factor_20260731.py
  SHA256 1185d8d8508d9e465d9a5deec54187ed398f05f580cb891964bf9e1da23967f2
scratch/audit_ad_k17_tripleflow_complete_pair_master_20260731.py
  SHA256 9b6b2a411aa96afafa6f4b2c03c74b4e2f7f0c4a3f8533ec833f7160debe6087
scratch/ad_k17_tripleflow_complete_pair_master_20260731.audit.json
  SHA256 a64686ab481f9d7433e16dc19f1270c6c886e88e8838815a041f4d1b5dce09b9
  payload 51f9385ae98afc173b443c6e3df6395ee8de988e216e4c37284a6f8fcc2cb97a
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_20260731.audit.json
  SHA256 c9284dcb1be52464b994636b7d594ee09b21dfbc1706abac228892d64cb92596
  payload 8dbc822e6cf3ed4349baa92159b9b7badd36b6e0eeed339f6490f714466bc567
```

The Python sources above passed AST parsing after their final edits.  The
three solver-free AD audits were rerun after the final theorem edits.  No
large local solve and no H100 solve was launched by this lane.
