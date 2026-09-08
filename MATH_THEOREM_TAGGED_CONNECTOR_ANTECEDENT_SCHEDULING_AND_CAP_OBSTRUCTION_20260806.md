# Exact antecedent scheduling for tagged connectors, and the cap obstruction

**Date:** 2026-08-06  
**Method:** coordinate-run scheduling and strict-gammoid rank; no computation
or search  
**Status:** unconditional local source theorem and sharp obstruction.  A
Johnson connector has a depth-`delta` antecedent exactly when two unit-job
schedules and one common-coordinate inequality hold.  Sliding-collar
positive flags are absorbed at zero positional charge when the connector
distance is at least `delta+1`; positive and zero flags are absorbed
simultaneously when it is at least `2delta+1`.  Without a distance aperture,
a graph-valid tagged connector can have `Omega(delta)` residence violations.
Missing-tag privacy also does not imply a bounded typed-cap sidecar.

## 1. Boundary ages

Let

\[
 V_0=A,V_1,\ldots,V_\ell=B
\tag{1.1}
\]

be a shortest path in the Johnson graph on rank-`R` owners.  Attach a fixed
left exterior ending at `A` and a fixed right exterior beginning at `B`.
For `x in A`, let `lambda(x)` be the number of consecutive owners containing
`x` immediately before and including `A`.  For `y in B`, let `rho(y)` be
the analogous number beginning at and including `B`.  Truncate both at
`delta+1`; a constant coordinate may be assigned age `delta+1`.

Every shortest Johnson path exchanges each member of `A-B` once for one
member of `B-A`.  Write

\[
 p_x\in[\ell]\quad(x\in A-B)
\tag{1.2}
\]

for the edge on which `x` is deleted, and

\[
 q_y\in[\ell]\quad(y\in B-A)
\tag{1.3}
\]

for the edge on which `y` is inserted.  Both `p` and `q` are permutations
of `[ell]`, and they may be chosen independently.

### Theorem 1.1 (exact seam-residence criterion)

Assume all positive coordinate runs wholly inside the two exteriors already
have length at least `delta+1`.  The joined trace is `delta`-resident at the
connector if and only if

\[
 \lambda(x)+p_x-1\ge\delta+1
       \qquad(x\in A-B),
\tag{1.4}
\]

\[
 \ell-q_y+\rho(y)\ge\delta+1
       \qquad(y\in B-A),
\tag{1.5}
\]

and

\[
 \lambda(z)+\ell-1+\rho(z)\ge\delta+1
       \qquad(z\in A\cap B)
\tag{1.6}
\]

for every nonconstant run meeting the seam.

#### Proof

Before its deletion, `x in A-B` occurs in `lambda(x)` exterior owners and
in the additional connector owners `V_1,...,V_(p_x-1)`.  Its seam run has
length `lambda(x)+p_x-1`, giving (1.4).  Dually, an inserted coordinate
`y` occurs in `V_(q_y),...,V_(ell-1)` and then in `rho(y)` right-exterior
owners, giving (1.5).  A common coordinate occurs throughout the connector;
after counting the two endpoint ages, only the `ell-1` internal connector
owners remain, giving (1.6).  These are all coordinate types on a shortest
path. \(\square\)

By the maximal-antecedent criterion, if the rest of the completed cyclic
trace is resident as well, these inequalities are exactly what is needed
for a nonempty depth-`delta` antecedent.  They are not merely sufficient
run estimates.

## 2. Hall collapses to two one-dimensional schedules

Define deletion release times and insertion deadlines by

\[
 r_x=\delta+2-\lambda(x),
 \qquad
 u_y=\ell+\rho(y)-\delta-1.
\tag{2.1}

Then (1.4) is `p_x>=r_x`, while (1.5) is `q_y<=u_y`.

### Theorem 2.1 (exact geodesic-ordering test)

Let

\[
 r_{(1)}\le\cdots\le r_{(\ell)},
 \qquad
 u_{(1)}\le\cdots\le u_{(\ell)}
\tag{2.2}

be the sorted release and deadline lists.  A shortest connector ordering
satisfying every deletion and insertion residence condition exists if and
only if

\[
 r_{(i)}\le i\le u_{(i)}
       \qquad(1\le i\le\ell).
\tag{2.3}

Together with (1.6), this is an exact test for a resident shortest
connector.

#### Proof

Unit jobs with release times `r_x` fill the slots `1,...,ell`.  Earliest
release order is feasible exactly when `r_(i)<=i`.  Equivalently, for every
cut `t`, at most `ell-t` jobs have release greater than `t`.  The insertion
jobs are the dual deadline problem and are feasible exactly when
`i<=u_(i)`.  A deletion permutation and an insertion permutation can be
paired arbitrarily edge by edge, so the two schedules do not create a
third coupling. \(\square\)

The minimum numbers of failed deletion and insertion runs are therefore

\[
 \eta_-=
 \max_{0\le t\le\ell}
 \bigl(|\{x:r_x>t\}|-(\ell-t)\bigr)_+,
\tag{2.4}
\]

\[
 \eta_+=
 \max_{1\le t\le\ell+1}
 \bigl(|\{y:u_y<t\}|-(t-1)\bigr)_+.
\tag{2.5}

The number of unavoidable short common-coordinate runs is

\[
 \eta_0=
 |\{z\in A\cap B:
   \lambda(z)+\ell-1+\rho(z)\le\delta\}|.
\tag{2.6}

Thus `eta_-+eta_++eta_0` is the exact minimum number of residence rows
violated by a shortest geodesic between the fixed boundary owners.

## 3. Sliding collars need only a distance aperture

Say that a boundary has the **unit clipped-age property** when

\[
 |\{x:\lambda(x)\le s\}|\le s
       \qquad(1\le s\le\delta),
\tag{3.1}

and use the analogous condition for right ages.  A sliding Johnson collar
has this property: at most one coordinate enters on each edge, so its last
`s` clipped owners contain at most `s` coordinates of age at most `s`.
The repeated labels in the synchronized PBBS collar are separated by more
than the collar window, so they do not change this conclusion at the far
endpoint.  A one-edge port whisker adds only the single age-one flag and
also obeys (3.1).

### Corollary 3.1 (zero-charge collar absorption)

Suppose both boundary ports have the unit clipped-age property and

\[
                         \ell\ge\delta+1.
\tag{3.2}

Then the shortest connector can be ordered so that it is resident.  No
source position is added.

#### Proof

For the deletion jobs,

\[
 |\{x:r_x>t\}|
 =|\{x:\lambda(x)\le\delta+1-t\}|.
\tag{3.3}

For `t=0` the needed bound is the trivial `|{x:r_x>0}|<=ell`.  For
`1<=t<=delta`, the unit-age property bounds (3.3) by
`delta+1-t<=ell-t`.  For `t>=delta+1` the set is empty.  This is the cut
form of the first half of (2.3).  The right-age calculation has the same
three cases and gives the deadline half.  Finally every common coordinate has ages
at least one, so

\[
 \lambda(z)+\ell-1+\rho(z)\ge\ell+1\ge\delta+2,
\]

which proves (1.6). \(\square\)

In the pair-tag connector, the exit tag deleted on the first edge belongs
to the fixed core of the outgoing collar and hence has left age
`delta+1`.  The entrance tag inserted on the last edge belongs to the fixed
core of the incoming collar and has right age `delta+1`.  A feasible
release schedule may put the first tag at position one, and a feasible
deadline schedule may put the second at position `ell`, without disturbing
feasibility.  Hence Corollary 3.1 is compatible with the exact two-tag
resource-separation construction.

### 3.1 Exact two-sided (positive/zero) scheduling

The same calculation controls zero gaps.  For `x in A-B`, let
`rho_0(x)` be its clipped zero age beginning at `B`; for `y in B-A`, let
`lambda_0(y)` be its clipped zero age ending at `A`.  A deletion position
must lie in

\[
 \delta+2-\lambda(x)
       \le p_x\le
 \ell+\rho_0(x)-\delta-1,
\tag{3.5}
\]

and an insertion position must lie in

\[
 \delta+2-\lambda_0(y)
       \le q_y\le
 \ell+\rho(y)-\delta-1.
\tag{3.6}

The left inequality pays the run or gap before the event; the right
inequality pays the complementary gap or run after it.

For unit jobs with nonempty allowed intervals
`[r_j,u_j] subseteq [ell]`, Hall's condition is exactly

\[
 |\{j:r_j\ge a,\ u_j\le b\}|\le b-a+1
       \qquad(1\le a\le b\le\ell).
\tag{3.7}

Indeed the job neighbourhoods are intervals, so every minimal failed Hall
shore is an interval of slots.

### Theorem 3.2 (biresident aperture)

At every Johnson cut, both positive ages and zero ages have the unit
clipped-age property.  If

\[
                         \ell\ge2\delta+1,
\tag{3.8}

then the deletion jobs (3.5) and insertion jobs (3.6) both satisfy (3.7).
Consequently a shortest connector ordering can preserve positive runs and
zero gaps simultaneously.

#### Proof

First, every allowed interval is nonempty: its release is at most
`delta+1`, while its deadline is at least
`ell-delta>=delta+1`.  For a deletion job counted on the left of (3.7),

\[
 \lambda(x)\le\delta+2-a,
 \qquad
 \rho_0(x)\le\delta+1+b-\ell.
\tag{3.9}

The unit-age bounds make the number of such jobs at most the smaller of
these two right sides whenever that side lies in `[1,delta]`, with a
nonpositive bound interpreted as zero.  If `b>=delta+1` and `a>=2`, the
first bound lies at most at `delta` and is at most

\[
 \delta+2-a\le b-a+1.
\]

If `b>=delta+1` and `a=1`, use the second bound instead.  When it lies in
`[1,delta]`, it is at most

\[
 \delta+1+b-\ell\le b=b-a+1.
\]

When it is nonpositive there are no counted jobs; when it equals
`delta+1`, necessarily `b=ell`, and the trivial bound `ell=b` suffices.
This separate `a=1` case is necessary because the unit-age inequality is
stated only up to clipped age `delta`.

If `b<=delta`, then (3.8) makes the second bound at most

\[
 \delta+1+b-(2\delta+1)=b-\delta\le0.
\]

Thus (3.7) holds.  The insertion jobs are identical with positive and zero
ages interchanged.  Coordinates common to `A,B` have a positive run
crossing all `ell+1` connector owners; coordinates absent from both have a
zero run crossing them.  Both are longer than `delta`. \(\square\)

For a pair-tag connector, the first deleted foreign tag was present through
the whole exit arm and is absent through the whole entrance arm; the last
inserted foreign tag has the dual property.  Hence the prescribed extreme
events also satisfy (3.5)--(3.6).

The only extra positive-source premise is the aperture (3.2); the stronger
two-sided premise is (3.8).  Set-theoretic
port supply is not a problem: if the global tag set has size
`O(sqrt R)` and `delta=O(sqrt R)`, then the family of rank-`R` owners with
one prescribed missing tag contains `exp(Theta(R))` members, whereas a
Johnson ball of radius `2delta` has size at most

\[
 (2\delta+1)R^{4\delta}=\exp(O(\sqrt R\log R)).
\tag{3.4}

Greedy selection therefore supplies `O(sqrt R)` abstract coded
one-missing-tag port owners at
pairwise distance at least `2delta+1`.  What is not proved by this counting
argument is a resident, resource-disjoint extension from every literal
PBBS component endpoint to its coded port.

## 4. Sharp obstruction to the unqualified graph lift

The distance hypothesis cannot be deleted.  Let
`s=floor(delta/2)` and suppose `s` deleted non-tag coordinates have clipped
left ages `1,2,...,s`.  Such a boundary is a literal suffix of a sliding
Johnson collar; its original positive runs may all continue on the old
side to length `delta+1`.  Give the two endpoints distinct port tags, so
the connector has length `ell=s+1`, the extra deletion being the old
fixed-core tag.  Every young-coordinate release time is at least

\[
 \delta+2-s>\ell.
\]

No deletion can meet its release.  Hence

\[
                         \eta_-=s=\Omega(\delta).
\tag{4.1}

The right-hand dual example gives `eta_+=Omega(delta)`.  Thus the
graph-level tagged connector theorem, by itself, admits an
unbounded clipped-history defect.  A bounded sidecar cannot be inferred
without either the distance aperture, a resident detour, or a different
source crossover.

## 5. Typed cap: exact condition and independent obstruction

Missing-tag signatures separate owner and lower-facet resources.  They do
not certify suffix capacity in the occurrence-labelled common cap.

After fixing the compensation linkage and every phase/guard state, let
`P_conn` be the physical port set exported by the connector histories and
let `Gamma_suf^type` be the residual typed strict gammoid.  A full private
suffix router is exactly

\[
 r_{\Gamma_{\rm suf}^{\rm type}}(P_{\rm conn})
       =|P_{\rm conn}|.
\tag{5.1}

More generally the smallest cap sidecar allowed by this port set is at
least, and in the one-system router model exactly,

\[
 \kappa_{\rm cap}
 =|P_{\rm conn}|-
   r_{\Gamma_{\rm suf}^{\rm type}}(P_{\rm conn}).
\tag{5.2}

For two occurrence coordinates one must use the common Rado/Edmonds
all-subset formula rather than (5.2) separately on the two shores.

There is no bound on (5.2) from the tagged owner theorem.  Give every one
of `q` tagged connector claims a private prefix and a distinct physical
port, but force all port suffixes through one common unit-capacity vertex.
All owner, tag, geodesic, and prefix-privacy statements remain true, while

\[
 r_{\Gamma_{\rm suf}^{\rm type}}(P_{\rm conn})=1,
 \qquad
 \kappa_{\rm cap}=q-1.
\tag{5.3}

For the full deadline-scale PBBS bank `q=Theta(sqrt R)`, this is unbounded.
Therefore a bounded
typed-cap sidecar requires a new all-cut suffix-router theorem; it is not a
formal consequence of component synchronization or source residence.

## 6. Revised PBBS source frontier

The graph-level connector theorem removes forced orientation and simple
factor compatibility.  The exact source lift now separates into:

1. **Distance aperture or resident detour.**  Ensure (2.3) and (1.6) at
   every forced connector.  The clean sufficient forms are
   `ell>=delta+1` for positive residence and `ell>=2delta+1` for simultaneous
   positive/zero residence.
2. **Resident completion.**  The unprotected cycles added by the
   polynomial factor theorem must themselves admit depth-`delta`
   antecedents, and their source histories must fuse with bounded charge.
3. **Literal history transport.**  The old/new PBBS phases must share the
   required common-history cells, not merely the same owner sets.
4. **Typed suffix rank.**  After the histories are materialized, the
   residual two-coordinate Rado/gammoid deficiency must be `O(1)`.

The first item has now been reduced to explicit one-dimensional Hall
inequalities.  Items 2--4 remain genuine correlated theorems.  In
particular, the phrase “literal history/cap lift” cannot currently be
replaced by a bounded-sidecar corollary of the tagged graph construction.
