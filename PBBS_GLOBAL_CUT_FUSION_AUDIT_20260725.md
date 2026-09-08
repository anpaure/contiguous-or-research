# PBBS global cut fusion after the same-phase compiler obstruction

Date: 2026-07-25

> **Superseded local verdict.**  After this audit isolated the lower
> two-threshold system (2.6), that system was solved exactly in
> `MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md`.  Floor
> correctness excludes extent points strictly southwest of a query, and a
> Pareto staircase gives a literal lower word of length \(2H-1\).  Together
> with Proposition 1.1, the complete one-cut chart has length \(4H-1\), and
> endpoint-capped initialization gives \(5H-1\) per cut.  I independently
> audited the southwest-exclusion injection, rectangle interception,
> physical ordering, nonzero letters, multi-cut provenance, and the
> resulting coefficient-one reduction; they pass.  Sections 1--2 below
> record the pre-staircase obstruction and should now be read only as an
> explanation of why the generic cut-halo lemma alone was insufficient.

## 0. Verdict

This note audits the surviving global-fusion fallback to Theorem 22.2 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.

There are four rigorous conclusions.

1.  At one cut, all **upper** crossing targets through depth \(H\) are
    covered by one owner halo of length at most \(2H\).  Thus the upper
    half of the literal \(H(H+1)\) repair ledger is genuinely compressible.

2.  The same halo argument does **not** cover the lower crossing targets.
    A short positive coordinate run crossing the cut is absent from every
    cyclic \((H+1)\)-fold erosion entry, although it belongs to some
    shallower crossing intersections.  Consequently the general cut-halo
    lemma cannot be invoked until a new raw factor-word provenance theorem
    has first been proved.  The presently proved local bound improves only
    from \(H(H+1)\) to

    \[
       \frac{H(H+1)}2+2H,
    \]

    before the separate endpoint-initialization charge.

3.  Cross-phase age interleaving can remove the **idle spacing** loss in
    the necessary age-only scheduler, conditional on the spatial deck
    lifts furnishing distinct source-phase labels.  Then, for a fixed
    depth \(q\), the \(Nq\) crossing requests can be ordered at unit
    density, because the \(N=2m+1\) phases may be used round-robin and
    \(N>H+q\).  This does not compress the number \(q\) of depth-\(q\)
    requests per cut.  It yields the optimal age-only scale \(Nq\), not
    \(N\).  The identification of deck phase with a legal compiler source
    phase is itself part of the missing physical construction.

4.  Even granting a hypothetical \(O(H)\)-entry physical compiler per cut,
    the best unconditional quotient packing bound

    \[
      \overline\nu_H
      =O\!\left(B_m\sqrt{\frac{\log m}{m}}\right)
    \]

    gives only an \(O(W\sqrt{\log m})\) repair estimate at
    \(H=A\sqrt m\), not \(o(W)\).  Endpoint throughput shows precisely
    what is missing: at every fixed rank the *distinct* unrepaired target
    family must be \(o(W)\).  The packing bound controls occurrences/cuts,
    not this distinct-target union.

Thus the same-phase obstruction is not repaired by a formal phase shuffle.
A successful global theorem needs new PBBS information: a cut-avoiding
support selection, a strong collision theorem for the crossing target
orbits, or a genuinely noncanonical factor-word in which one endpoint
simultaneously carries an age-compatible tower across many depths.

## 1. Exact crossing families at one cut

Let

\[
  \ldots,X_{-2},X_{-1}\mid X_0,X_1,\ldots
\]

be the rank-\((m+1)\) owner trajectory, with the cut between \(X_{-1}\)
and \(X_0\).  At depth \(q\), the owner windows crossing this cut are
indexed by \(1\le s\le q\):

\[
  L_{q,s}=\bigcap_{i=-s}^{q-s}X_i,
  \qquad
  U_{q,s}=\bigcup_{i=-s}^{q-s}X_i.                 \tag{1.1}
\]

When the occurrence has the intended rank, these lie in ranks
\(m+1-q\) and \(m+1+q\), respectively.  There are at most \(q\) lower
and \(q\) upper occurrences, which is the ledger used in (22.8).

### Proposition 1.1 (the upper halo is linear)

The word

\[
   X_{-H},X_{-H+1},\ldots,X_{H-1}                 \tag{1.2}
\]

has length \(2H\) and represents every \(U_{q,s}\) with
\(1\le s\le q\le H\).

#### Proof

The interval of (1.2) beginning at \(-s\) and ending at \(q-s\) is
exactly the owner window in (1.1), so its OR is \(U_{q,s}\).  The index
bounds follow from \(-q\ge-H\) and \(q-s\le H-1\).  \(\square\)

Appending the lower targets literally and using Proposition 1.1 therefore
costs at most

\[
   \sum_{q=1}^Hq+2H=\frac{H(H+1)}2+2H             \tag{1.3}
\]

per cut.  Including the \(H\) endpoint-capped erosion entries charged in
Theorem 22.2 gives

\[
   \frac{H(H+1)}2+3H                               \tag{1.4}
\]

per cut, in place of \(H^2+2H\).  This is an exact constant-factor
improvement, but it remains quadratic.

## 2. Why the generic cut-halo lemma does not compress the lower half

The cut-halo lemma says that length-at-most-\(H\) OR windows crossing a
cut of an **already existing word** can be retained in \(O(H)\) entries.
For the lower targets in (1.1), the missing premise is exactly that they
are OR windows of the raw erosion word.

Let a coordinate \(x\) have a positive owner run crossing the cut,

\[
  x\in X_{-a},X_{-a+1},\ldots,X_b,
  \qquad a\ge1,\quad b\ge0,                         \tag{2.1}
\]

and suppose its run has at most \(H\) owners:

\[
  a+b+1\le H.                                      \tag{2.2}
\]

For the cyclic erosion entries

\[
  D_j=\bigcap_{h=0}^H X_{j+h},                     \tag{2.3}
\]

no \((H+1)\)-owner window is contained in (2.1).  Hence

\[
  x\notin D_j\quad\hbox{for every }j.              \tag{2.4}
\]

On the other hand, whenever \(s\le a\) and \(q-s\le b\), (1.1) gives

\[
  x\in L_{q,s}.                                    \tag{2.5}
\]

Thus the natural erosion interval assigned to this \(L_{q,s}\) cannot
equal it: every erosion entry in that assigned interval omits \(x\).  In
particular, merely copying the usual raw seam neighbourhood does not prove
the required lower provenance.  (An unrelated erosion entry elsewhere on
the cycle may contain \(x\), but no theorem identifies a suitable interval
using it without adding other coordinates.)  The owner halo does not help
either, since every nonempty OR of rank-\((m+1)\) owners has rank at least
\(m+1\), while \(L_{q,s}\) has rank \(m+1-q\).

This is a provenance obstruction, not merely an accounting omission.  An
\(O(H)\) lower seam word might still exist by a materially different
noncanonical encoding, but it is not supplied by endpoint-capped erosion
or by the general cut-halo lemma.

There is a useful exact description of that new local problem.  A
coordinate run (2.1) belongs to the crossing lower target precisely when

\[
   x\in L_{q,s}
   \quad\Longleftrightarrow\quad
   s\le a\ \hbox{ and }\ q-s\le b.                 \tag{2.6}
\]

So the exceptional coordinates form a two-threshold dominance incidence
system.  Proving an \(O(H)\) lower compiler is equivalent to giving this
incidence system a length-\(O(H)\) contiguous-OR representation compatible
with the nonexceptional erosion entries.  No such theorem is currently in
the PBBS ledger.

## 3. Cross-phase interleaving removes idle time, not request count

The same-phase age theorem requires starts at one depth \(q\) and one
source phase to be separated by

\[
   D_q=H+q.                                         \tag{3.1}
\]

Take one quotient cut and all of its \(N=2m+1\) spatial lifts.  Suppose,
as an explicit additional hypothesis, that a proposed physical compiler
assigns these lifts to \(N\) distinct source-phase labels.  At depth
\(q\), each such phase has \(q\) crossing offsets.  In the age-only projection,
order the requests by

\[
  0,1,\ldots,N-1,
  0,1,\ldots,N-1,
  \ldots                                             \tag{3.2}
\]

for \(q\) rounds.  Consecutive uses of a phase are exactly \(N\) positions
apart.  For fixed \(A\), \(H=\lceil A\sqrt m\rceil\) gives

\[
   N>2H\ge H+q                                      \tag{3.3}
\]

for all sufficiently large \(m\).  Therefore (3.2) is a feasible age-only
schedule of length exactly \(Nq\), with no idle positions.

This is the strongest conclusion available from phase interleaving alone.
At rank \(m+1-q\), one endpoint represents at most one distinct target.
Consequently \(Nq\) distinct lower targets already force \(Nq\) endpoints.
Round-robin scheduling reaches this endpoint-throughput scale; it cannot
turn \(q\) requests per cut into one request per cut.

Moreover, (3.2) is only a schedule of requested starts.  The PBBS spatial
deck by itself does not prove the source-phase hypothesis, nor does (3.2)
show that the overlapping Boolean owner towers prescribed by different
phases are mutually compatible.  A physical compiler must establish both
facts and construct one actual owner trace realizing the starts.

## 4. The best unconditional packing estimate is still too large

Write

\[
  N=2m+1,\qquad B_m=\operatorname{Cat}_m,
  \qquad W=NB_m.
\]

The proved quotient estimate is

\[
  \overline\nu_H
  =O\!\left(B_m\sqrt{\frac{\log m}{m}}\right).      \tag{4.1}
\]

The deck transversal theorem gives a physical cut set of size

\[
  T_H\le2N\overline\nu_H+NZ_H
  =O\!\left(W\sqrt{\frac{\log m}{m}}\right)+o(W),  \tag{4.2}
\]

because \(NZ_H=\exp(o(m))=o(W)\) in a fixed Gaussian window.

Even if the unresolved local lower problem were solved with a complete
\(CH\)-entry compiler per physical cut, (4.2) would give

\[
  CH T_H
  =O_A(W\sqrt{\log m})+o(W),                       \tag{4.3}
\]

at \(H=\lceil A\sqrt m\rceil\); the short-cycle term remains \(o(W)\)
after multiplication by the polynomial factor \(H\).  The principal term
is not \(o(W)\).
Thus an \(O(H)\)-per-cut theorem would be mathematically useful, but it
would not combine with the best unconditional residence packing estimate
to prove constant one.

## 5. Exact endpoint obstruction to a count-only global theorem

Let \(B\) be the already constructed main word and append a repair word
\(C\) of length \(R\).  For a fixed rank \(r\), every target newly covered
by \(B\mid C\) has a witness ending in \(C\).  Suffix ORs ending at one
endpoint form an inclusion chain, and hence contain at most one rank-\(r\)
set.  Therefore

\[
  \#\bigl(\mathcal R_r(B\mid C)\setminus\mathcal R_r(B)\bigr)
  \le R.                                            \tag{5.1}
\]

For a cut set \(\mathcal C\), let \(\mathcal D_q^-(\mathcal C)\) be the
distinct rank-\((m+1-q)\) targets whose designated surviving witnesses
still require the global fusion/repair stage.  Then every appended repair
satisfies

\[
   R\ge\max_{1\le q\le H}
        |\mathcal D_q^-(\mathcal C)|,               \tag{5.2}
\]

and the analogous statement holds for upper targets.

The cut-count estimate (4.2) bounds the number of crossing *occurrences* by
at most \(qT_H\) at depth \(q\).  It gives no sublinear bound on the union
\(\mathcal D_q^-(\mathcal C)\).  At \(q=H=A\sqrt m\), the ambient rank has

\[
  \binom{2m+1}{m+1-H}=e^{-A^2+o(1)}W,              \tag{5.3}
\]

so a linear-size distinct defect family is fully consistent with all the
present cut-count bounds.  Equation (5.1) would then force a linear repair.

This proves that neither (4.1) nor (4.2), even supplemented by perfect
age-only interleaving, is sufficient data for an \(o(W)\) global compiler.

## 6. The precise surviving global theorem

A viable fusion route must add at least one of the following genuinely new
statements.

1. **Cut-avoiding support.**  Choose one correct PBBS occurrence for every
   band target so that only \(o(W)\) chosen occurrences cross the residence
   transversal.

2. **Distinct-defect collapse.**  Prove, for a suitable transversal, that

   \[
     |\mathcal D_q^-(\mathcal C)|+
     |\mathcal D_q^+(\mathcal C)|=o_A(W)
   \]

   at every fixed Gaussian depth, together with a summable or vertically
   factorable multidepth version.

3. **Physical tower fusion.**  Construct one actual cross-phase owner word
   whose endpoints carry the nested lower/upper towers, at essentially the
   endpoint-throughput optimum.  The round-robin order (3.2) proves that the
   old same-phase age cut would not obstruct such a word, but it supplies
   neither owner compatibility nor the lower dominance compiler (2.6).

4. **Stronger residence packing.**  Prove \((\mathrm{RP}_A)\) itself; then
   Theorem 22.2 already finishes constant one without this fusion lane.

The unconditional contribution of this audit is therefore a separation:
the upper seam is linear and phase idle time is removable, but lower
factorability and distinct-target collapse remain independent mathematical
gates.  Treating all crossing windows as if they were already OR windows of
one raw halo is invalid.
