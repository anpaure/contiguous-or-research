# Logarithmic coordinate cuts in exact wreath factors

## 1. Outcome and theorem ledger

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac Wn=\operatorname {Cat}_m.
\]

This note attacks the existence side of the multidepth coordinate-cut
criterion.  It separates two notions which behave completely differently.

* A **full depth-\(q\) covering cut** at \(z\) says that every
  \((m-q)\)-set avoiding \(z\) occurs as a cyclic interval in the factor.
* At depth one, a **core-rainbow cut** says that the internal cut slots
  enumerate the \((m-1)\)-sets avoiding \(z\) exactly once.

The second condition had been proposed as a convenient certificate for the
first.  It cannot be used logarithmically.

### New proved results

1. **Five-rainbow-cut theorem.**  An exact middle wreath factor has at most
   five simultaneous depth-one core-rainbow coordinates.  The constant five
   is attained when \(m=2\).
2. **Exact local compatibility.**  Occurrences of one first-shadow colour
   carry a matching of boundary pairs.  Simultaneous rainbow cuts impose an
   exact degree equation on that matching.  This gives, in particular, an
   exact pairwise double-colour ledger.
3. **Full-cut kernel theorem.**  The full depth-\(q\) covering coordinates
   are exactly the common intersection of all missing depth-\(q\) masks,
   with the convention that every coordinate covers when there are no
   holes.
4. **Gap-surplus theorem.**  For a set of full covering coordinates, the
   number of coordinate-free short-window occurrences beyond the exact
   middle count is controlled by an explicit gap functional.  Its maximum
   under the gap-sum constraint is computed exactly.
5. **Symmetry dichotomy.**  In a point-transitive exact factor, at any fixed
   depth either the shadow is complete or there are no full covering
   coordinates at all.

### Consequence for the proposed logarithmic target

The sufficient condition

\[
 \sum_{q\le H}2^{-t_q}e^{-q^2/(2m)}=o(1)
\]

cannot take \(t_1\) to mean the number of core-rainbow cuts: the first term
is then at least \(2^{-5}+o(1)\).  It remains viable with the weaker full-cut
meaning.  In that meaning the construction problem is a **kernelization of
the hole families**: at depth \(q\), all holes must contain a prescribed
set of \(t_q\) coordinates.

No such all-depth exact factor is constructed here.  The note proves a
structural obstruction to the strongest route and isolates a corrected
algebraic/absorption target for the weaker route.

## 2. First-shadow occurrences and their boundary matching

Let \(\mathcal F\) be an exact middle wreath factor.  Thus it consists of
\(B\) cyclic orders, and their length-\(m\) cyclic intervals partition
\(\binom{[n]}m\).

Fix an \((m-1)\)-set \(S\).  An occurrence of \(S\) in a cyclic order has
the form

\[
             \cdots,a,\ S,\ b,\cdots ,
\]

where \(a,b\notin S\) are the two symbols immediately adjacent to the
interval.  Attach the unordered boundary edge \(ab\) to this occurrence,
and let \(\Gamma(S)\) be the resulting multigraph on \([n]\setminus S\).

### Lemma 2.1 (boundary matching)

For every \(S\), \(\Gamma(S)\) is a simple matching.  In particular, if
\(\mu(S)\) is the total number of occurrences of \(S\), then

\[
 0\le \mu(S)\le \left\lfloor\frac{m+2}{2}\right\rfloor.
\]

#### Proof

The two length-\(m\) intervals adjacent to the displayed occurrence are
\(S\cup\{a\}\) and \(S\cup\{b\}\).  If two boundary edges for \(S\)
shared a vertex \(a\), then the middle set \(S\cup\{a\}\) would occur in
two wreath positions.  This contradicts exact middle factorization.  The
same argument rules out a repeated edge.  Hence the boundary edges form a
matching.  \(\square\)

Cut one row at a coordinate \(z\), and write it as

\[
 (z,y_0,y_1,\ldots,y_{2m-1}).
\]

The depth-one core slots are

\[
 \{y_i,y_{i+1},\ldots,y_{i+m-2}\},\qquad 1\le i\le m.
\]

An occurrence of \(S\) is a core slot for the cut at \(z\) if and only if

\[
              z\notin S\quad\hbox{and}\quad
              z\notin \partial S,
\]

where \(\partial S\) is its boundary edge.  Therefore the number of core
occurrences of a fixed \(z\)-free colour is

\[
 c_z(S)=\mu(S)-d_{\Gamma(S)}(z).                 \tag{2.1}
\]

Since \(\Gamma(S)\) is a matching, its degree is zero or one.

### Corollary 2.2 (exact rainbow compatibility)

If \(z\) is a core-rainbow coordinate, then for every \(S\) avoiding \(z\),

\[
 \boxed{\ \mu(S)-d_{\Gamma(S)}(z)=1.\ }          \tag{2.2}
\]

Consequently \(\mu(S)\in\{1,2\}\).  It equals two precisely when one of
the two boundary edges is incident with \(z\).

More generally, if every coordinate in \(Z\) is rainbow and
\(R=Z\setminus S\ne\varnothing\), then

* if \(\mu(S)=1\), the unique boundary edge avoids every member of \(R\);
* if \(\mu(S)=2\), the two disjoint boundary edges cover every member of
  \(R\), and hence \(|R|\le4\).

This is an occurrence-level compatibility law, not merely a count of slots.

## 3. At most five simultaneous rainbow cuts

### Theorem 3.1 (five-rainbow-cut theorem)

For \(m\ge2\), an exact middle wreath factor on \(2m+1\) coordinates has at
most five simultaneous depth-one core-rainbow coordinates.

#### Proof

Let \(Z\) be the set of rainbow coordinates and put \(t=|Z|\).  Fix a row
and a member \(z\in Z\).  After cutting at \(z\), write the row in the
five-block form

\[
 z\ \big|\ F_+\ \big|\ u\ \big|\ v\ \big|\ F_- ,       \tag{3.1}
\]

where

\[
 F_+=\{y_0,\ldots,y_{m-2}\},\quad
 u=y_{m-1},\quad v=y_m,\quad
 F_-=\{y_{m+1},\ldots,y_{2m-1}\}.
\]

Both \(F_+\) and \(F_-\) are \((m-1)\)-shadow occurrences.  They are the
two fringe, rather than core, slots for the cut at \(z\).  Their current
boundary edges are respectively

\[
                  \{z,u\},\qquad \{v,z\}.          \tag{3.2}
\]

Apply (2.2) to \(F_+\).  The displayed occurrence is incident with \(z\),
so \(\mu(F_+)=2\).  Every rainbow coordinate missing from \(F_+\) must be
an endpoint of one of its two boundary edges.  Apart from the current edge
\(\{z,u\}\), only the two endpoints of the other occurrence remain.
The special coordinates missing from \(F_+\) and not already in
\(\{z,u\}\) are exactly those in \(F_-\), together with \(v\) when
\(v\in Z\).  Hence

\[
             |Z\cap F_-|+\mathbf1_{v\in Z}\le2.    \tag{3.3}
\]

The symmetric argument applied to \(F_-\) gives

\[
             |Z\cap F_+|+\mathbf1_{u\in Z}\le2.    \tag{3.4}
\]

The four terms on the left of (3.3)--(3.4) partition \(Z\setminus\{z\}\).
Adding the inequalities gives

\[
                        t-1\le4,
\]

and therefore \(t\le5\).  \(\square\)

### Equality rigidity

If \(t=5\), both inequalities in the proof are equalities in every row and
at every marked coordinate.  Equivalently, for every \(z\in Z\), the next
\(m\) positions and the preceding \(m\) positions in the cyclic order each
contain exactly two members of \(Z\setminus\{z\}\).  The tournament on
\(Z\) obtained by orienting \(z\to w\) when \(w\) lies in the next
\(m\) positions is therefore regular in every wreath.

Moreover, the second boundary occurrence of each fringe colour is forced
to use precisely the two still-uncovered marked endpoints in (3.3) or
(3.4).  Thus equality is a highly rigid finite-state condition, not merely
a numerically possible endpoint count.

### Sharpness of the universal constant

For \(m=2\), take the two cyclic orders

\[
 (0,1,2,3,4),\qquad (0,2,4,1,3).                  \tag{3.5}
\]

Their length-two intervals partition all ten pairs: they are the two
complementary Hamilton cycles of \(K_5\).  At a cut \(z\), the two core
singletons in one cycle are its two non-neighbours of \(z\); in the other
cycle they are the two neighbours from the first cycle.  Hence all four
singletons other than \(z\) occur exactly once.  Every one of the five
coordinates is rainbow.

Thus five is the best universal constant.  Whether five can occur for an
unbounded sequence of \(m\) is a separate open question.

## 4. Additional exact multi-rainbow ledgers

For a rainbow coordinate \(z\), define

\[
 \mathcal D_z=\{S:z\notin S,\ \mu(S)=2\}.
\]

The two fringe occurrences in each of the \(B\) rows are pairwise distinct
as colours, by the boundary-matching lemma.  Conversely, every member of
\(\mathcal D_z\) has exactly one boundary edge incident with \(z\).  Hence

\[
                         |\mathcal D_z|=2B.          \tag{4.1}
\]

Now let \(z,w\) both be rainbow.  Let \(a_{zw}\) be the number of wreath
orders in which the circular distance between \(z\) and \(w\) is \(m\)
(equivalently, the two oriented distances are \(m\) and \(m+1\)).

### Proposition 4.1 (pairwise double-colour law)

\[
 \boxed{
 |\mathcal D_z\cap\mathcal D_w|=B+a_{zw}.
 }
\tag{4.2}
\]

Among these common double colours, exactly \(a_{zw}\) have \(z,w\) on the
same boundary edge; the remaining exactly \(B\) have them on the two
different boundary edges.

#### Proof

In one row, the two \(z\)-fringe sets are disjoint.  If \(w\) occupies one
of the two central positions \(u,v\) in (3.1), then it lies in neither
fringe; otherwise it lies in exactly one fringe.  Thus the number of
\(z\)-fringe colours avoiding \(w\), summed over the rows, is
\(B+a_{zw}\).  Since \(w\) is rainbow, these and only these colours belong
to both double families.  In an antipodal row exactly one of the two
fringes has boundary edge \(zw\), while no non-antipodal row does.  This
proves both assertions.  \(\square\)

For comparison, exact middle factorization alone already forces

\[
 \sum_{\pi\in\mathcal F}
       \bigl(m-\operatorname {dist}_\pi(z,w)\bigr)
 =\binom{2m-1}{m-2}=\frac{m-1}{2}B.               \tag{4.3}
\]

Thus the average circular distance is \((m+1)/2\) for every coordinate
pair.  Equation (4.3) is a horizontal exactness identity, not an additional
consequence of rainbowness.

## 5. Full covering cuts are hole kernels

For \(1\le q\le m-1\), put \(r=m-q\), let \(\mu_q(S)\) be the number of
cyclic length-\(r\) occurrences of \(S\), and let

\[
 \mathcal H_q=\{S\in\tbinom{[n]}r:\mu_q(S)=0\}
\]

be the depth-\(q\) hole family.

### Theorem 5.1 (full-cut kernel identity)

The set \(C_q\) of full depth-\(q\) covering coordinates is

\[
 C_q=
 \begin{cases}
  \displaystyle\bigcap_{S\in\mathcal H_q}S,&\mathcal H_q\ne\varnothing,\\[6pt]
  [n],&\mathcal H_q=\varnothing.
 \end{cases}                                      \tag{5.1}
\]

#### Proof

Every occurrence of an \(r\)-set avoiding \(z\) is one of the full cut
slots at \(z\).  Thus \(z\) is covering exactly when no missing \(r\)-set
avoids \(z\), or equivalently when every hole contains \(z\).  \(\square\)

This theorem explains why full cuts evade Theorem 3.1.  If the first shadow
is globally complete, then all \(n\) coordinates are full covering cuts,
even though there may be no core-rainbow cut at all.  The certified
\(m=4\) perfect-first-shadow factor has exactly this behaviour.

It also gives a useful symmetry warning.

### Corollary 5.2 (point-transitive dichotomy)

If the automorphism group of an exact factor is transitive on coordinates,
then at every fixed depth \(q\) either \(\mathcal H_q=\varnothing\), in
which case every coordinate covers, or \(C_q=\varnothing\).

Indeed, \(C_q\) is an invariant subset.  Transitivity makes it empty or all
of \([n]\); the latter is impossible for a nonempty hole of size \(r<n\).

Therefore a group-transitive algebraic construction cannot produce an
intermediate logarithmic family of covering cuts.  It must either solve the
whole depth exactly or deliberately break point transitivity and mark a
small coordinate kernel.

## 6. Exact gap-surplus law for full cuts

Let \(Z\subseteq[n]\), \(|Z|=t\ge1\).  In one cyclic order, let

\[
 g_1,\ldots,g_t\ge0,\qquad \sum_i g_i=2m+1-t=:N,
\]

be the numbers of unmarked symbols in the cyclic gaps between consecutive
members of \(Z\).  The number of cyclic length-\(s\) intervals avoiding
\(Z\) is

\[
 A_s(\pi,Z)=\sum_{i=1}^t(g_i-s+1)_+.              \tag{6.1}
\]

### Lemma 6.1 (pointwise shortening surplus)

For \(1\le q\le m-1\),

\[
 \begin{aligned}
 A_{m-q}(\pi,Z)-A_m(\pi,Z)
 &=\sum_{i=1}^t
   \min\{q,(g_i-m+q+1)_+\}                       \tag{6.2}\\
 &=qt-\sum_{i=1}^t\min\{q,(m-1-g_i)_+\}.          \tag{6.3}
 \end{aligned}
\]

In particular it is at most \(qt\).

#### Proof

For one gap, the difference is zero below length \(m-q\), grows by one per
additional gap position until it reaches \(q\) at gap length \(m-1\), and
then remains \(q\).  This is exactly the summand in (6.2), and (6.3) is its
complement to \(q\).  \(\square\)

The crude bound \(qt\) ignores the fixed total gap mass.  The exact maximum
is also elementary.

### Lemma 6.2 (exact maximum gap surplus)

Define

\[
 P_q(m,t)=
 \max_{0\le \ell\le
   \min\{t,\lfloor N/(m-q)\rfloor\}}
 \min\{\ell q,\ N-\ell(m-q-1)\}.                 \tag{6.4}
\]

Then the maximum of (6.2), over all cyclic \(t\)-gap vectors of total
\(N\), is exactly \(P_q(m,t)\).

#### Proof

Call a gap active when it has length at least \(m-q\).  If there are
\(\ell\) active gaps, their activation consumes
\(\ell(m-q-1)\) positions before any surplus is counted.  The remaining
positions contribute at most one unit each, and every gap caps at \(q\),
giving the upper bound in (6.4).  Conversely, allocate the indicated number
of surplus positions among \(\ell\) active gaps, up to \(q\) each.  Any
leftover positions may be placed beyond saturation in an active gap without
changing its contribution.  This realizes the bound.  \(\square\)

Assume now that every coordinate in \(Z\) is a full depth-\(q\) covering
cut.  Then every \((m-q)\)-set disjoint from \(Z\) occurs.  Let
\(E_{q,Z}\) denote total multiplicity beyond one among just these disjoint
targets.  Exact middle factorization and (6.2) give the equality

\[
 \boxed{
 E_{q,Z}
 =\binom Nm-\binom N{m-q}
  +\sum_{\pi\in\mathcal F}
     \bigl(A_{m-q}(\pi,Z)-A_m(\pi,Z)\bigr).
 }
\tag{6.5}

Indeed, the aggregate number of \(Z\)-free middle intervals is
\(\binom Nm\), while the aggregate number of \(Z\)-free short intervals is
obtained by adding the row surpluses.  Since all \(\binom N{m-q}\) targets
are occupied, the remainder is exactly \(E_{q,Z}\).

Nonnegativity yields the necessary arithmetic condition

\[
 \boxed{
 \binom N{m-q}-\binom Nm\le B P_q(m,t).
 }
\tag{6.6}

The same condition holds with every nonempty subset of \(Z\) in place of
\(Z\).

### The first-depth specialization

At \(q=1\), the row surplus is simply the number of marked gaps of length at
least \(m-1\).  The exact maximum is

\[
 P_1(m,t)=
 \begin{cases}
  1,&t=1,\\
  2,&2\le t\le3,\\
  1,&4\le t\le m+2,\\
  0,&m+3\le t\le2m+1.
 \end{cases}                                      \tag{6.7}
\]

In particular, for \(4\le t\le m+1\), at most one such gap exists, so

\[
                         P_1(m,t)=1.
\]

Moreover, for \(t\le m+1\),

\[
 \binom N{m-1}-\binom Nm
 =\binom Nm\frac{t-2}{m+2-t}.                      \tag{6.8}
\]

At the excluded endpoint \(t=m+2\), the denominator in the ratio form
vanishes, while the unnormalised difference on the left is exactly \(1\).
This endpoint is irrelevant to the logarithmic regime below but must not be
read through (6.8).

For \(t=o(\sqrt m)\), division by \(B\) gives

\[
 \frac1B\left(\binom N{m-1}-\binom Nm\right)
 =2(t-2)2^{-t}\exp(O(t^2/m)).                      \tag{6.9}
\]

Thus \(t\asymp\tfrac12\log_2m\) has enormous arithmetic slack: the left
side is \(o(1)\), whereas a single row of surplus is available.  The gap
count proves no obstruction to logarithmically many **full** covering cuts.

It is important not to overread (6.6).  It counts only targets disjoint from
all of \(Z\).  Simultaneous covering of the coordinates in \(Z\) requires
coverage of every target which omits at least one member of \(Z\), a family
of size

\[
 \binom n{m-q}-\binom{n-t}{m-q-t},                 \tag{6.10}
\]

which is almost the whole layer.  The small family in the second term of
(6.10) is the allowed hole reservoir, not the family that must be covered.

## 7. The algebraic matching formulation

Let \(\mathscr W_m\) be the \((2m+1)\)-uniform hypergraph whose vertices
are the middle \(m\)-sets and whose hyperedges are wreaths.  An exact middle
wreath factor is a perfect matching of \(\mathscr W_m\).

Every wreath also carries its \(n\) cyclic depth-\(q\) colours.  Under the
uniform fractional perfect matching on all wreaths, coordinate symmetry
gives every depth-\(q\) colour the same fractional load

\[
 \lambda_q=\frac{W}{\binom n{m-q}}
 =\frac{(m+2)^{\overline q}}{(m)_q}\ge1.           \tag{7.1}
\]

For \(q=o(\sqrt m)\),

\[
                 \log\lambda_q
                 =\frac{q(q+1)}m+O(q^3/m^2).       \tag{7.2}
\]

Thus all full-cut lower quotas are feasible in the symmetric fractional
relaxation, even if one asks for complete coverage of every depth colour.
There is no fractional or aggregate-count obstruction.  This does not rule
out an integral divisibility or trade-lattice obstruction; the unresolved
issue is critical integral rounding while simultaneously preserving the
exact middle perfect matching.

The logarithmic cut target has the following exact matching form.

> **Kernelized vertical matching problem.**  Choose sets
> \(Z_q\subseteq[n]\).  Find a perfect matching in \(\mathscr W_m\) such
> that, at every controlled depth \(q\), every \((m-q)\)-set not containing
> all of \(Z_q\) occurs in at least one selected wreath.

This is equivalent to saying that the hole family at depth \(q\) is
contained in

\[
              \{S:Z_q\subseteq S\}.               \tag{7.3}
\]

If the weighted sizes of the kernels satisfy the audited cut criterion,
the weak vertical wreath lemma follows.

An especially clean, stronger target uses one common set \(Z\) for all
controlled depths.  If

\[
 |Z|\ge\tfrac12\log_2m+\omega(1),
\]

then forcing every central-band hole to contain \(Z\) gives

\[
 \sum_{q\le H}\frac{M_q}{W}
 \le 2^{-|Z|}\sum_{q\ge1}e^{-q^2/(2m)}=o(1),       \tag{7.4}
\]

in the inherited tail-compatible range for \(H\).  This common-kernel form
is stronger than necessary but is more natural for recursion.

## 8. Assessment of sparse dedicated wreaths and completion

A tempting proposal is to reserve \(o(B)\) wreaths, put the marked
coordinates consecutively in them, and cover all targets avoiding the
marked set by long Johnson paths.  There are two separate problems.

### 8.1 It covers the wrong family

The family of targets disjoint from a logarithmic \(Z\) has only about a
\(2^{-|Z|}\) fraction of the layer.  But simultaneous full cuts require the
much larger family (6.10), namely every target which fails to contain all of
\(Z\).  Hence \(o(B)\) dedicated wreaths cannot establish the cut property
from scratch.  The \(2^{-|Z|}\) sector is where holes may be parked.

The corrected absorber picture is the reverse: first construct a factor
whose shadow already covers almost everything, then use a sparse family of
trades to move all residual holes into the kernel-containing reservoir.

### 8.2 Sparse middle support is not enough for exact completion

Even a family of only \(o(B)\) prescribed wreaths consumes \(o(W)\) middle
sets, but cardinality alone does not imply extendability to an exact factor.
For a middle set \(A\), every wreath through \(A\) also uses two members of
its odd-graph neighbourhood

\[
 \{[n]\setminus(A\cup\{x\}):x\in[n]\setminus A\},
\]

which has size \(m+1\).  Deleting that small neighbourhood blocks every
wreath through \(A\).  Therefore any robust completion theorem must impose
local resilience or quasirandomness conditions, not merely an
\(o(W)\)-vertex bound.

No audited theorem currently says that an arbitrary \(o(B)\)-sized partial
wreath packing extends.  A valid absorption theorem would have to be proved
for a specially generated partial packing and would need at least:

1. local odd-neighbourhood resilience at every uncovered middle set;
2. control of the large codegrees between almost-complementary middle sets;
3. an absorber which preserves the marked shadow quotas while completing
   the middle perfect matching.

Thus sparse completion is a credible programme, but not yet a lemma that can
be invoked.

## 9. Recursive and algebraic directions which survive

### 9.1 Exact first-shadow coverage

The mathematically cheapest way around Theorem 3.1 is to prove

\[
                         M_1(\mathcal F_m)=0        \tag{9.1}
\]

for an exact factor in every dimension.  Then every coordinate is a full
covering cut, while no core-rainbow cut is needed.  This is known to be
feasible at \(m=2\), and an explicit exact factor with perfect first shadow
is certified at \(m=4\).  No all-\(m\) construction is presently proved.

In the Johnson-graph language, (9.1) asks for a wreath 2-factor whose edge
colour multiplicities are all positive.  The average multiplicity is only

\[
                         \lambda_1=1+\frac2m,
\]

so this is a critical lower-quota 2-factor problem rather than a consequence
of generic random factorization.

### 9.2 Kernel-preserving two-coordinate lift

The useful recursive statement is not preservation of rainbow cores.  It is
the following weaker target.

> Given an exact factor whose depth-\(q\) holes all contain \(Z_q\), lift it
> from \(2m+1\) to \(2m+3\) so that every new uncorrected hole projects to
> an old hole and therefore still contains the embedded kernel; repair the
> remaining seam holes with a sub-Catalan absorber.

The audited MSW peak-insertion projection gives the correct occurrence
table for such a lift, but a missing child target has no canonical parent.
The absent ingredient is exactly a kernel-respecting capacitated Hall flow
on deletion presentations.  Merely projecting covered occurrences does not
prove this recursion.

### 9.3 Trade-lattice formulation

Start from one exact factor.  A trade replaces a small family of wreaths by
another family with the same middle-set union.  Its first- and deeper-shadow
changes are integer vectors.  A sufficient algebraic theorem would show that
these trade vectors can eliminate every hole outside chosen kernels while
using only a sparse absorber family and maintaining nonnegative colour
multiplicities.

This avoids the false demand for logarithmically many rainbow cores.  It
also makes the exact obstruction visible: the relevant trade lattice must
be saturated at a load only \(1+O(1/m)\) above one in the first shadow.

## 10. Multidepth conclusion and next theorem targets

The rigorous hierarchy is now:

\[
 \text{core-rainbow cut}
 \quad\Longrightarrow\quad
 \text{full covering cut}
 \quad\Longleftrightarrow\quad
 \text{coordinate lies in every hole}.
\]

At depth one the first implication is strict, and its source is bounded:

\[
 \boxed{\text{at most five simultaneous core-rainbow cuts}.}
\]

Therefore the following proposed route is impossible:

> obtain \(\tfrac12\log_2m+\omega(1)\) core-rainbow coordinates at every
> controlled depth and invoke cut amplification.

The following two routes remain mathematically coherent.

1. **Exact shallow shadows plus kernelized deeper shadows.**  Prove exact
   coverage for the first few depths, then arrange common kernels for the
   remaining depths.  Exact depth one is the first clean target.
2. **Common-kernel vertical factor.**  Construct one exact middle factor for
   which every hole through the whole controlled band contains one marked
   set \(Z\) of size
   \(\tfrac12\log_2m+\omega(1)\).

The smallest genuinely new existence theorem would be either:

* an all-\(m\) perfect-first-shadow wreath theorem; or
* a kernel-preserving absorption theorem for the wreath hypergraph, with
  explicit local resilience hypotheses and a proof that the recursive
  partial packing satisfies them.

The first is a fixed-depth exact design problem.  The second is a
multidepth critical-rounding theorem.  What has been ruled out is the
apparently simpler intermediate shortcut of obtaining logarithmically many
independent rainbow coordinate cores.
