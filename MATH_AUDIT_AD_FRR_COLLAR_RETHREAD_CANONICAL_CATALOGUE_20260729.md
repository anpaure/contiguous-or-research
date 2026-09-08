# FRR collar rethreading inside the canonical even edge-orbit catalogue

Date: 2026-07-29  
Status: exact encoding equivalence and scope audit; no solver was run.

## 0. Verdict

The new joint-`H` facet-rail repair model is not a second combinatorial
catalogue.  It is exactly the `BB` no-cross part of the canonical `K=16`
edge-orbit catalogue, written in source-relative change coordinates.

More precisely, the fixed-label `K=16` catalogue splits as

\[
  12012\ \mathrm{AA}+3432\ \mathrm{AB}+12012\ \mathrm{BB}=27456.
  \tag{0.1}
\]

The independent-rail construction freezes the whole `AA` factor and all
`AB` variables.  On the `BB` shore it freezes the three upper-colour blocks
belonging to the old 45-cycle and leaves the other 426 blocks free.  Every
free upper block has 28 possible Johnson edges.  Hence the number of free
canonical edge bits is exactly

\[
                         426\binom82=11928.       \tag{0.2}
\]

Equivalently, `12012+3432+3*28=15528` members of the full 27,456-bit array
are fixed.  These are unit assignments, not structural rows; direct
presolve leaves precisely (0.2).

The current joint model uses one cut bit `x_q` and 27 non-old pair bits
`y_(q,p)` in each block, again

\[
                         426+426\cdot27=11928.    \tag{0.3}
\]

There is a literal affine bijection

\[
 z_{q,p_0}=1-x_q,\qquad z_{q,p}=y_{q,p}\quad(p\ne p_0),       \tag{0.4}
\]

where `z` is the canonical selected-edge bit and `p_0` is the old pair.
Thus a direct use of the canonical one-hot catalogue is **isomorphic**, not
smaller, at the primary-variable level.  It does, however, make a separate
cut channel unnecessary.

For a standalone source-relative model, `x_q` is redundant.  Eliminating it
and the old-edge bit gives the exact delta chart

\[
             h_q:=\sum_{p\ne p_0}y_{q,p}\in\{0,1\},\qquad
             z_{q,p_0}=1-h_q,                              \tag{0.5}
\]

with only

\[
                         426\cdot27=11502                 \tag{0.6}
\]

Boolean edit variables.  This is a real but modest saving of 426 bits,
about 3.57 percent.  No larger variable reduction is proved here: binary
five-bit pair selectors are possible as state encodings, but the degree and
lower-turn rows then require an exact pair decoder.  No theorem shows that
such a decoded CNF/PB model has smaller total size.

The default implementation has two material sufficient-only restrictions:

1. the 45-cycle, hence three upper-colour orbits, is frozen; and
2. changed old edge orbits have cyclic separation at least four.

It is exact for this **separated, small-component-frozen,
`Z_15`-equivariant source-relative collar-rethread subclass**.  It is not
WLOG for `FRR(7,4)`, `RTR(7,4)`, or arbitrary equivariant `K=16` factors.
Within that subclass, the decoded factor may have arbitrary successor
permutation, quotient component structure, and component voltages.

## 1. The `BB` block is the odd turn-selector catalogue

Let `S=Z_15`, and write a `BB` middle owner as `X+z` with

\[
                         X\in\binom S7.
\]

A `BB` Johnson edge is uniquely

\[
 (U\setminus\{a\})+z\;--\;(U\setminus\{b\})+z,
 \qquad U\in\binom S8,\quad \{a,b\}\in\binom U2.          \tag{1.1}
\]

Its upper and lower `q1` colours are respectively

\[
                 (U+z),\qquad (U\setminus\{a,b\})+z.      \tag{1.2}
\]

The cyclic action is free on ranks seven and eight.  Consequently there are
429 upper-set orbits, and every upper orbit has exactly 28 candidate edge
orbits.  This proves

\[
                     |\mathcal E_{BB}|=429\cdot28=12012.  \tag{1.3}
\]

### Theorem 1.1 (exact `BB` turn-factor formulation)

For one Boolean `z_(U,p)` per orbit in (1.1), the
`Z_15`-equivariant rank-seven factors which are upper-`q1` perfect are
exactly the integral solutions of

\[
       \sum_{p\in\binom U2}z_{U,p}=1
       \qquad\text{for every upper orbit }U,              \tag{1.4}
\]

and

\[
       \sum_{e\in\mathcal E_{BB}}m_V(e)z_e=2
       \qquad\text{for every rank-seven owner orbit }V.  \tag{1.5}
\]

Here `m_V(e)` is zero or one for a nonloop quotient edge and is two for a
quotient loop based at `V`.

The factor is lower-`q1` complete exactly when the lower rows in Section 2
also hold.

#### Proof

Equation (1.4) selects one physical edge at every rank-eight union colour,
so the upper palette is perfect.  Equation (1.5) is precisely physical
degree two after lifting; a selected quotient loop supplies the two
distinct phase neighbours at every lifted owner.  Thus the lift is a
spanning 2-factor.  Conversely an equivariant factor with perfect upper
palette selects one member of every block (1.1), and physical degree two
projects to (1.5).  The fixed-section phase labels on the selected edges
decode its quotient cycles and voltages; no topology or voltage hypothesis
was used.  QED.

Under the independent-rail lemma, the fixed `AA` factor supplies the two
even colours avoiding `z`, while this `BB` factor supplies the two colours
containing `z`.  Thus the odd FRR variables embed literally in the even
catalogue; no complement identification is required.

## 2. Exceptional lower-colour orbits and their coefficients

For a physical rank-six target `R`, the provider edges are

\[
             (R+a)--(R+b),\qquad \{a,b\}\in
             \binom{S\setminus R}{2},                    \tag{2.1}
\]

so every physical target has 36 providers.  Let `O` be its rotation orbit
and put `s_O=|O|`.  At rank six,

\[
                     s_O\in\{15,5\};                     \tag{2.2}
\]

there are 333 ordinary orbits and two exceptional size-five orbits.  The
number of distinct provider edge orbits is

\[
             |P_O|=\frac{s_O\,36}{15}
              =\begin{cases}36,&s_O=15,\\12,&s_O=5.
                \end{cases}                              \tag{2.3}
\]

One selected provider orbit contributes physical load

\[
                         c_O=\frac{15}{s_O}
              =\begin{cases}1,&s_O=15,\\3,&s_O=5
                \end{cases}                              \tag{2.4}
\]

to every target in `O`.  Hence the exact physical load equation is

\[
                         \ell_R=c_O\sum_{e\in P_O}z_e.   \tag{2.5}
\]

For Boolean coverage, (2.5) is equivalent to the clean row

\[
                         \sum_{e\in P_O}z_e\ge1.         \tag{2.6}
\]

The coefficient three must nevertheless be retained in load objectives,
excess ledgers, and any physical-occurrence equality.  Treating an
exceptional selected orbit as one physical occurrence is wrong by a factor
of three.  The present joint script avoids that error: it expands all
physical lower rows first.  In an exceptional row the same selector can
therefore occur three times; duplicate literals do not alter its Boolean OR
semantics, but they record the correct occurrence multiplicity before CNF
deduplication.

In the delta chart, let `ell^0_R` be the old physical load and let
`lambda(q,p)` be the lower orbit of the candidate pair.  Then the exact
signed load row is

\[
 \ell_R^0+
 c_O\sum_{q}\sum_{p\ne p_0(q)}
 \bigl(1_{\lambda(q,p)=O}-1_{\lambda(q,p_0)=O}\bigr)y_{q,p}
 \ge1.                                                   \tag{2.7}
\]

This formula also shows why the cut bits contain no independent
information.

## 3. Exact source-relative delta model

Let `B_0` be the saved `6390+45` facet factor.  Its large component has
quotient length 426 and voltage four.  For each large upper orbit `q`, let
`e_q^0` be its old edge and let `e_(q,p)` be the 27 non-old candidates.

### Theorem 3.1 (cut-bit elimination)

The following model is projection-bijective to the current joint `x/y`
model.

Use only the 11,502 bits `y_(q,p)`, and impose

\[
                         \sum_{p\ne p_0(q)}y_{q,p}\le1
                         \qquad(q\in Z_{426}).            \tag{3.1}
\]

Decode selected edges by

\[
 z_{e_q^0}=1-\sum_{p\ne p_0(q)}y_{q,p},\qquad
 z_{e_{q,p}}=y_{q,p}.                                    \tag{3.2}
\]

Starting from the old factor, impose the signed degree equations

\[
 \sum_{q,p\ne p_0}
       \bigl(m_V(e_{q,p})-m_V(e_q^0)\bigr)y_{q,p}=0
 \qquad(V\in\binom S7/\rho),                             \tag{3.3}
\]

with loop multiplicity two, and the 335 lower rows (2.7).  The upper
palette remains perfect automatically.  Then (3.1)--(3.3) and (2.7) are
exactly the static factor-and-both-`q1` part of the joint model.

#### Proof

Given a joint solution, put `y` equal to its non-old selectors.  The
channel equation `sum_p y_(q,p)=x_q` gives (3.1)--(3.2).  Subtracting the
old degree and lower-load rows gives (3.3) and (2.7).

Conversely, define `x_q=sum_p y_(q,p)`.  By (3.1), `x_q` is Boolean and the
joint channel equation holds.  Equations (3.2)--(3.3) reconstruct one edge
per upper block and degree two; (2.7) reconstructs every lower row.  The two
maps are inverse.  QED.

### Collar and path-length rows

The 1,425 old length-three runs project to 95 closed four-edge collar
orbits.  Every repair must change at least one old edge in each collar, so

\[
       \sum_{q\in C}\sum_{p\ne p_0(q)}y_{q,p}\ge1
       \qquad(C\in\mathcal C_0),\quad |\mathcal C_0|=95. \tag{3.4}
\]

The default separated subclass additionally imposes

\[
       \sum_p y_{q,p}+\sum_p y_{q',p}\le1
       \quad\text{when }1\le d_{C_{426}}(q,q')\le3.      \tag{3.5}
\]

There are exactly `3*426=1278` unordered rows in (3.5).  These rows ensure
that every retained source path has at least four vertices.  Equation (3.4)
is necessary for every source-relative repair; (3.5) is a sufficient
collar-rethread restriction and is not WLOG.

Using one pseudo-Boolean row for each displayed constraint, the fixed
semantic base has

\[
\begin{array}{c|r}
\text{family}&\text{rows}\\ \hline
\text{one non-old choice at most}&426\\
\text{weighted owner degree}&429\\
\text{lower orbit coverage}&335\\
\text{old collar hit}&95\\
\text{cut separation}&1278\\ \hline
\text{total before residence}&\boxed{2563}.
\end{array}                                             \tag{3.6}
\]

Some rows become tautological after the frozen small cycle is substituted;
(3.6) is an exact uniform installed-family count, not a claim about a
particular presolver's deduplicated row count.  With the optional separation
rows removed but the necessary collars retained, the base has 1,285 rows.
If an implementation materializes the whole 27,456-bit even array rather
than substituting the fixed rail, it also has 15,528 unit assignments.  They
do not change the projected model.

The raw canonical form uses 11,928 free edge bits and the same semantic
rows.  The joint `x/y` form also uses 11,928 primary bits.  Only the affine
delta form (3.2) reduces the standalone primary count to 11,502.

## 4. Short physical runs are finite labelled quotient-walk cuts

Every undirected edge orbit has two directed fixed-section darts

\[
                         a=(i,j,p),\qquad \bar a=(j,i,-p). \tag{4.1}
\]

For a compatible directed quotient walk

\[
 a_h=(i_h,i_{h+1},p_h),\qquad 0\le h<L,                  \tag{4.2}
\]

and initial phase `s`, its physical lift is

\[
 X_h=\rho^{s+P_h}U_{i_h},\qquad
 P_h=\sum_{j<h}p_j.                                     \tag{4.3}
\]

This formula uses the actual phase on each edge and therefore remains exact
for zero, nonunit, and unit component voltages.

### Theorem 4.1 (motif lift/project equivalence)

Fix positive residence threshold four.  A selected equivariant 2-factor has
a nonconstant coordinate-one run of length `ell in {1,2,3}` if and only if
it contains a physical lift (4.3) of a labelled quotient walk of
`ell+1<=4` edges whose vertex trace in some coordinate is

\[
                         0,1^\ell,0.                    \tag{4.4}
\]

For every such valid physical path `P`, let `supp(P)` be the set of distinct
undirected edge-orbit variables used by it.  The exact forbidden-motif cut is

\[
                  \sum_{e\in\operatorname{supp}(P)}z_e
                  \le |\operatorname{supp}(P)|-1.       \tag{4.5}
\]

Physical components of length below four are excluded by the analogous cut
on the support of the whole decoded lifted cycle.

#### Proof

The bordering edges of a physical short run give the walk and trace (4.4).
Projection through the fixed section records unique successive dart phases,
so it gives (4.2)--(4.3).  If every edge orbit in `supp(P)` is selected,
every physical edge of `P` is selected.  At each internal physical vertex
the two path edges exhaust factor degree two, so the path is consecutive in
the factor and the short run persists.  Thus (4.5) is valid.

Conversely every short run in a selected factor supplies its bordering
path, hence violates its member of (4.5).  A short whole component is
similarly forced when all its cycle edges are retained.  QED.

Rotation sends a motif in coordinate `a` to one in coordinate `a+1`, so one
may normalize the coordinate to zero while retaining the initial phase in
(4.3).  Thus the family is finite and lives entirely on labelled quotient
walks of at most four edges.  It needs neither a width selector nor a
component-voltage selector.  It is best separated lazily: an integral
factor is decoded, every physical component is traversed, and only the
actually violated members of (4.5) are installed.

After substitution (3.2), (4.5) becomes the signed source-relative clause

\[
 \sum_{e_q^0\in P}\sum_{p\ne p_0}y_{q,p}
 +\sum_{e_{q,p}\in P}(1-y_{q,p})\ge1,                   \tag{4.6}
\]

which is exactly the clause generated by the joint CEGAR implementation.

## 5. Decode and FRR splice theorem

### Theorem 5.1 (exact separated collar-rethread decode)

Suppose an integral solution of Sections 2--4 also satisfies (3.4)--(3.5),
and freeze the old 45-cycle.  Let `H` be the old large-component edge
orbits for which `h_q=1`.  Then:

1. deleting `H` leaves the safe 45-cycle and large-component paths of at
   least four vertices;
2. the selected non-old edges form a perfect matching of all exposed path
   endpoints;
3. every cut upper colour is restored exactly once;
4. every lower colour remains covered; and
5. the physical factor obtained by inserting the matching is positive-
   resident through four and has no component shorter than four.

Conversely every `Z_15`-equivariant rethread satisfying these five
conditions and freezing the 45-cycle gives a unique integral solution.

Hence the model is an exact implementation of the separated version of the
rainbow collar-rethread theorem.  Its quotient cycles may be oriented after
decoding; their phase sums give arbitrary emergent voltages.

#### Proof

Separation (3.5) gives item 1.  No two cut old edges share an endpoint, so
each exposed endpoint has degree deficit one.  Signed degree conservation
(3.3) therefore says precisely that the new edges form a perfect matching,
proving item 2.  The block decode (3.2) and lower rows prove items 3--4.
The complete motif family (4.5), including the short-component cuts, proves
item 5.  All decoding operations are reversible, proving the converse.
QED.

The no-cross union of this decoded `BB` factor with the frozen certified
`AA` factor is then a `Z_15`-equivariant `K=16` factor with both even `q1`
palettes and the positive-residence property supplied by the independent-
rail theorem.  This conclusion is sufficient-only: cross-shore factors and
repairs of the small component lie outside the model.

## 6. Audit of the current joint implementation

File audited:

```text
scratch/solve_k15_frr_joint_h_selector_cegar_20260729.py
```

The following parts are exact.

* Its 426 `x` and 11,502 `y` primaries realize (0.4).
* Physical endpoint expansion correctly retains loop coefficient two before
  quotient-row deduplication.
* Physical lower-row expansion correctly handles the two short target
  orbits; repeated literals are harmless for a cover clause.
* A retained old path edge contributes the blocking literal `x_q`, while a
  selected new path edge contributes `-y_(q,p)`.  This is exactly (4.6).
* Literal reconstruction and traversal audit the actual lifted components,
  so arbitrary component voltage is not silently replaced by unit voltage.

The following scope qualifications are mandatory.

1. The default spacing clauses are the extra condition (3.5).  Therefore a
   default UNSAT result would be a no-go only for the separated subclass,
   not for all source-relative `FRR(7,4)`.
2. The output scope string mentions the frozen small component but does not
   presently name the separation restriction.  The mathematical scope must
   include it whenever the default rows are enabled.
3. `--omit-collar-spacing` removes both the optional spacing rows and the
   necessary old-collar rows.  The latter can eventually be rediscovered by
   complete CEGAR, but separating these two switches would make the proof
   boundary clearer.
4. `--pin-old` contradicts the default collar-hit rows.  It is meaningful
   as an old-factor regression only when those rows are omitted.
5. CEGAR is complete only after it reaches PASS or solver UNSAT with all
   accumulated cuts.  A finite round cap ending in timeout or UNKNOWN is not
   a theorem.

These qualifications do not invalidate the implemented clauses.  They
prevent a sufficient subclass or an incomplete CEGAR run from being
reported as a general FRR no-go.

## 7. Proved boundary

Proved:

* the joint `x/y` model and the free canonical `BB` edge variables are
  projection-bijective;
* `x` can be eliminated exactly, giving 11,502 source-relative edit bits;
* the exact base has 2,563 semantic rows with separation, before lazy
  residence cuts;
* exceptional lower orbits have 12 provider variables and physical
  coefficient three;
* every physical short run projects to, and lifts from, a finite labelled
  quotient walk of at most four edges; and
* decoding yields precisely the separated frozen-small collar-rethread
  subclass, with arbitrary emergent topology and voltage.

Not proved:

* that cut separation or freezing the 45-cycle is WLOG;
* that 11,502 is a globally smallest SAT encoding rather than the smallest
  immediate delta form obtained by eliminating the derived cut bits;
* that the separated FRR model is feasible; or
* any existence theorem for unrestricted equivariant or nonequivariant
  `K=16` factors.

No SAT, CP, C++, Python search, remote job, or sustained local computation
was run for this audit.
