# Z22: bounded-displacement line arrangements at the cleared degree scale

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Exact verdict

The real-line loose-intersection construction has two sharply different
consequences.

1. It is not merely an abstract geodesic construction.  Every one of its
   buffered chunks extends to the ordinary cyclic gap schedule

   \[
             \rho(c)=c+H,
\tag{0.1}
   \]

   so its displacement bound is exactly zero.  It therefore lies in every
   bounded-displacement catalogue which contains the ordinary schedule.

2. It can be amplified to the actual polynomial retained-fibre scale.
   For any even

   \[
       \mu=m^{O(1)}
       \quad\hbox{with}\quad
       \mu\le (Q!)^2/2,
\tag{0.2}
   \]

   one can put \(\mu/2\) line variants and \(\mu/2\) fillers over each of
   \(n=(1/2+o(1))\ell\) distinct tags, each with rational weight
   \(1/\mu\).  Every tag has mass one and every target has load at most
   one.  After clearing by any denominator \(\mathfrak D\) divisible by
   \(\mu\), the ambient maximum tag/target degree is \(\mathfrak D\), but
   the line copies form a clique of size

   \[
             {n\mathfrak D\over2}.
\tag{0.3}
   \]

   Equivalently, the weighted matching cut fails by the factor \(n/2\).
   This is a genuine counterexample to any catalogue-wide theorem saying
   that literal bounded-displacement geometry, calibrated star
   capacities, and protected three-antichain pruning imply a
   \((1+o(1))\mathfrak D\) weighted matching resolution.

3. This does not yet refute the particular uniform fractional point
   produced by isolated random pruning.  The completions of one fixed
   central line skeleton occupy at most

   \[
       {2\over
       \binom{m+H}{m}(m)_{\ell-1}(H)_{\ell-1}}
       =
       \exp[-\Omega(\ell\log m)]
\tag{0.4}
   \]

   of that fibre.  If \(pA=\mu_{\rm iso}\) is the isolated-sampling mean,
   with

   \[
       \mu_{\rm iso}=m^{11/6-o(1)}
\tag{0.5}
   \]

   in the pointwise construction, then with probability \(1-o(1)\) every
   line bundle of the displayed type has retained mass

   \[
             o(1/(Qn)).
\tag{0.6}
   \]

   Hence the total mass of one \(n\)-tag line system is
   \(o(1/Q)\) in that chosen point.  Clearing denominators does not change
   this normalized mass.

4. A single line system is coefficient-negligible for the weaker goal of
   constructing one cyclic-interval near-design.  It uses only
   \(O(\ell^2)\) crossing owners and \(n=O(\ell)\) tags.  Quarantining all
   its anchors costs \(O(\ell^2)=o(W)\), and quarantining all its protected
   claims costs

   \[
             O(Q\ell^2)=o(W).
\tag{0.7}
   \]

   A coefficient-scale obstruction would require a global packing of
   \(\Omega(W/\ell^2)\) essentially disjoint line systems.  No such
   packing is constructed here.

Thus the universal hereditary weighted-colouring route is false, but the
single-near-design route and the weighted cut for the specifically chosen
isolated-pruning point remain open.  The exact missing positive property
for that point is an odd-clique dispersal theorem, not a geometric Helly
theorem.

## 1. Parameters and the line-covector paths

Assume

\[
       Q=o(\ell),\qquad
       g=\ell+2Q-1\le H-Q,\qquad
       H\le m-2.
\tag{1.1}
\]

These hold in the calibrated return-free regime.  Put

\[
       n=\left\lceil{\ell\over2}\right\rceil,
       \qquad
       \epsilon_\ell=\mathbf 1_{\{\ell\ {\rm even}\}}.
\tag{1.2}
\]

Then

\[
       2(n-1)+\epsilon_\ell=\ell-1.
\tag{1.3}
\]

Take the \(n\) real lines

\[
             \Lambda_i:\ y=ix+i^2
             \qquad(1\le i\le n).
\tag{1.4}
\]

They are pairwise nonparallel.  Their pairwise intersection is

\[
       p_{ij}=(-i-j,-ij).
\tag{1.5}
\]

Moreover, \(p_{ij}\in\Lambda_k\) if and only if

\[
       k^2-k(i+j)+ij=(k-i)(k-j)=0.
\tag{1.6}
\]

Thus there is no triple point.

For every \(k\), introduce a four-coordinate block

\[
       B_k=\{a_k,b_k,c_k,d_k\}
\tag{1.7}
\]

and encode signs relative to \(\Lambda_k\) by

\[
       -\longmapsto A_k=\{a_k,b_k\},\qquad
       0\longmapsto N_k=\{b_k,c_k\},\qquad
       +\longmapsto D_k=\{c_k,d_k\}.
\tag{1.8}
\]

Along \(\Lambda_i\), the signed vertical difference from \(\Lambda_k\)
is

\[
       ix+i^2-(kx+k^2)
          =(i-k)(x+i+k).
\tag{1.9}
\]

It changes sign exactly once, at \(p_{ik}\).  Realize this sign change
through

\[
       A_k\longrightarrow N_k\longrightarrow D_k
\tag{1.10}
\]

or in the reverse direction.  Each arrow is one Johnson exchange:

\[
\begin{array}{c|c|c}
\hbox{arrow}&\hbox{departure}&\hbox{arrival}\\
\hline
A_k\to N_k&a_k&c_k\\
N_k\to D_k&b_k&d_k\\
D_k\to N_k&d_k&b_k\\
N_k\to A_k&c_k&a_k.
\end{array}
\tag{1.11}
\]

The two exchanges in one block use distinct departures and arrivals, and
different blocks are disjoint.

### Lemma 1.1 (exact constant-weight realization)

There are \(n\) length-\(g\) monotone Johnson geodesics
\(P_1,\ldots,P_n\) whose physical central interval has \(\ell\) owner
states and for which the owner at the crossing of paths \(i,j\) is the
same \(m\)-set \(X_{ij}\).

#### Proof

Put

\[
       d_0=2n+2Q+\epsilon_\ell=g+2.
\tag{1.12}
\]

Besides the \(n\) four-coordinate sign blocks, take
\(2Q+\epsilon_\ell\) disjoint two-coordinate padding blocks.  Their total
active ground size is

\[
       4n+2(2Q+\epsilon_\ell)=2d_0.
\]

Partition the remaining coordinates into two common sets

\[
       C_0,\ Z,\qquad |C_0|=|Z|=m-d_0.
\tag{1.13}
\]

Every owner contains \(C_0\), two coordinates from every sign block, and
one coordinate from every padding block.  Its size is therefore

\[
       (m-d_0)+2n+(2Q+\epsilon_\ell)=m.
\]

Path \(P_i\) keeps its own block \(B_i\) fixed at \(N_i\).  Orient
\(\Lambda_i\) by increasing \(x\), and process its \(n-1\) crossings in
that order, performing the two exchanges (1.11) in the appropriate
direction.  Before these exchanges perform \(Q\) common padding swaps.
After the line exchanges perform the optional
\(\epsilon_\ell\)-swap and then \(Q\) common suffix swaps.  The total
number of transitions is

\[
       Q+2(n-1)+\epsilon_\ell+Q
          =\ell+2Q-1=g.
\tag{1.14}
\]

The \(Q\) prefix and \(Q\) suffix transitions are exactly the certificate
buffers.  The \(\ell\) states between them are the physical central
owners.

At \(p_{ij}\), blocks \(i\) and \(j\) are neutral.  Every other block
\(k\) records the geometric sign of \(p_{ij}\) relative to
\(\Lambda_k\).  This sign is independent of whether the point is
approached on \(\Lambda_i\) or on \(\Lambda_j\).  Hence the complete
encoded owner is the same on both paths; call it \(X_{ij}\).

Every coordinate which departs on one path is distinct, every coordinate
which arrives is distinct, and no arrival later departs.  Thus the
sequence is a global monotone Johnson geodesic, not merely a walk.
\(\square\)

### Lemma 1.2 (exact carriers and distinct tags)

Every \(P_i\) lies on a size-\((m+H)\) carrier \(U_i\), and the carriers
are pairwise distinct.

#### Proof

The intersection of all owners of \(P_i\) is

\[
             C_0\cup N_i,
\]

of size

\[
             m-d_0+2=m-g.
\tag{1.15}
\]

Its union contains \(C_0\), both coordinates from every padding block,
all four coordinates from each \(B_k\), \(k\ne i\), and only
\(b_i,c_i\) from \(B_i\).  It therefore has size \(m+g\).

Choose one common set

\[
             R\subseteq Z,\qquad |R|=H-g,
\tag{1.16}
\]

and put

\[
             U_i=\bigcup_tX_i(t)\cup R.
\tag{1.17}
\]

Then \(|U_i|=m+H\).  Carrier \(U_i\) omits \(a_i,d_i\), whereas every
\(U_j\), \(j\ne i\), contains all four coordinates of \(B_i\).  Hence
the carriers, and therefore their tags, are distinct. \(\square\)

## 2. Complete protected-intersection audit

Let \(\mathcal S_Q(P)\) be the complete raw protected support:

\[
 \mathcal S_Q(P)
 =
 \{X_t:Q\le t\le g-Q\}
 \cup
 \{L_q(t),U_q(t):
      1\le q\le Q,\ Q\le t\le g-Q\}.
\tag{2.1}
\]

For a monotone owner sequence,

\[
       L_q(t)=\bigcap_{h=0}^qX_{t+h},
       \qquad
       U_q(t)=\bigcup_{h=0}^qX_{t-h}.
\tag{2.2}
\]

### Theorem 2.1 (singleton protected intersections)

For \(i\ne j\),

\[
       \boxed{
       \mathcal S_Q(P_i)\cap\mathcal S_Q(P_j)
          =\{X_{ij}\}.}
\tag{2.3}
\]

#### Proof

Ranks first separate the three flag types:

\[
       |L_q|=m-q,\qquad |X|=m,\qquad |U_q|=m+q.
\tag{2.4}
\]

Block \(B_i\) is \(N_i=\{b_i,c_i\}\) in every owner of \(P_i\), including
both buffer collars.  It is therefore exactly \(N_i\) in every
intersection or union in (2.2).

On \(P_j\), \(j\ne i\), block \(B_i\) is a side state except at the one
owner corresponding to \(p_{ij}\), and its two transitions through
neutrality are consecutive.  A positive-length consecutive intersection
in this block is one of

\[
       A_i,\quad D_i,\quad\{b_i\},\quad\{c_i\},
       \quad\varnothing,
\tag{2.5}
\]

never \(N_i\).  A positive-length consecutive union is one of

\[
       A_i,\quad D_i,\quad
       \{a_i,b_i,c_i\},\quad
       \{b_i,c_i,d_i\},\quad
       B_i,
\tag{2.6}
\]

again never \(N_i\).

Therefore a target common to \(P_i\) and \(P_j\) must be a depth-zero
owner of \(P_j\) at its crossing with \(P_i\).  Its total rank is \(m\),
so the target on \(P_i\) is also an owner.  Applying the same argument to
block \(B_j\) forces that owner to be the mutual crossing owner
\(X_{ij}\).  Conversely \(X_{ij}\) occurs on both paths. \(\square\)

In particular, no three paths contain one common target, every target
star in this \(n\)-path family has size at most two, and

\[
       \tau_{\rm star}(\{P_1,\ldots,P_n\})
          =\left\lceil{n\over2}\right\rceil.
\tag{2.7}
\]

The lower bound follows because one star covers at most two paths.  For
the upper bound, pair the paths and use their \(X_{ij}\)'s.  Since
\(Q=o(\ell)\),

\[
       {\tau_{\rm star}\over Q}\longrightarrow\infty.
\tag{2.8}
\]

Every pair survives protected three-antichain pruning, because its
complete protected intersection is a singleton.

Priority calibration cannot create another common target: claimed
supports are subsets of the raw supports.  All \(X_{ij}\) are middle
owners and are claimed independently of the priority order.

## 3. Exact embedding in the bounded-displacement catalogue

The following check is decisive.  A return-free geodesic is already a
segment of the ordinary cyclic packet after a suitable carrier labelling.

### Lemma 3.1 (ordinary-cycle extension)

Let

\[
 U=C\ \dot\cup\
 \{a_1,\ldots,a_g\}\ \dot\cup\
 \{b_1,\ldots,b_g\}\ \dot\cup R
\tag{3.1}
\]

with \(|C|=m-g\), \(|R|=H-g\), and \(g\le H\).  Then the owner geodesic

\[
 X_t=C\cup\{a_{t+1},\ldots,a_g\}
        \cup\{b_1,\ldots,b_t\}
\tag{3.2}
\]

is a consecutive segment of the ordinary cyclic schedule
\(\rho(c)=c+H\) on \(U\).

#### Proof

Choose a cyclic labelling \(U=\{u_c:c\in\mathbb Z_{m+H}\}\).  At a
chosen phase \(s\), set

\[
       u_{s+t}=a_{t+1},\qquad
       u_{s-H+t}=b_{t+1}
       \qquad(0\le t<g).
\tag{3.3}
\]

The two phase intervals are disjoint because \(g\le H\).  Put the
remaining \(H-g\) labels in the hole interval \([s-H,s)\) equal to
\(R\), and fill the remaining owner positions with \(C\).

For \(\rho(c)=c+H\), the arrival at transition \(c\) is \(u_{c-H}\).
Thus transitions \(s,\ldots,s+g-1\) depart
\(a_1,\ldots,a_g\) and arrive \(b_1,\ldots,b_g\).  The owner at phase
\(s\) is \(C\cup\{a_1,\ldots,a_g\}\), and the recurrence is exactly
(3.2). \(\square\)

The displacement permutation in Lemma 3.1 is the identity, so the
bounded-displacement parameter is zero.  Since (1.1) also gives
\(g\le H-Q\), the radius-\(Q\) rotor lift and both certificate collars
are legal.  All carrier labellings occur in the symmetrized catalogue.
Thus the line paths are actual bounded-displacement catalogue columns,
not external geodesic additions.  Here a tag fixes its carrier-copy and
physical chunk position.  If one instead treats a whole \(M\)-cycle as
one indivisible edge, Lemma 3.1 controls the displayed chunk but does not
assert anything about targets outside that chunk.

## 4. Amplification to the cleared degree scale

### Lemma 4.1 (many variants on one fixed tag)

Over each tag \(U_i\), the central line trajectory has at least

\[
             {(Q!)^2\over2}
\tag{4.1}
\]

distinct simple protected geodesic variants with all crossing owners
\(X_{ij}\) unchanged.

#### Proof

Keep every sign-block transition fixed.  Independently permute the
\(Q\) prefix padding swaps and the \(Q\) suffix padding swaps.  Their
coordinate sets, the owner union, and the carrier remain unchanged.

At the first physical phase, the nested upper chain through depths
\(1,\ldots,Q\) recovers the reverse prefix order.  At the last physical
phase, the nested lower chain recovers the suffix order.  Thus two
different ordered pairs of permutations give different raw protected
supports.  Reversal can identify at most two oriented presentations of
one simple geodesic support, which gives (4.1). \(\square\)

The calibrated counts satisfy \(c_Q\to\infty\), so one may put the two
boundary phases inside the common claimed-priority prefix at every depth.
Alternatively, the catalogue retains labelled column multiplicities, in
which case even coincident claimed supports remain distinct legal
columns.  Hence (4.1) is valid in either convention relevant to rational
clearing.

### Lemma 4.2 (polynomial finite avoidance)

Fix one size-\((m+H)\) carrier and a polynomial-size target family
\(\mathcal Z\) in the protected ranks.  There are polynomially many
geodesic columns on the carrier whose complete raw protected supports
avoid \(\mathcal Z\).

#### Proof

A fixed grid slot of rank \(r\) is uniform on
\(\binom{U}{r}\) under coordinate relabelling.  One path has at most
\((2Q+1)\ell=m^{O(1)}\) protected slots.  Therefore a uniform path hits
\(\mathcal Z\) with probability at most

\[
 { (2Q+1)\ell|\mathcal Z|
   \over
   \min_{|r-m|\le Q}\binom{m+H}{r}}
       =o(1).
\tag{4.2}
\]

The denominator is superpolynomial, whereas the numerator and the number
of requested paths are polynomial. \(\square\)

### Theorem 4.3 (actual degree-\(\mathfrak D\) weighted-cut obstruction)

Let \(\mu\) be even and satisfy (0.2).  There is a rational multicover on
the actual line tags with all of the following properties.

\[
\begin{array}{ll}
\text{tag mass}&=1,\\
\text{maximum target load}&=1,\\
\text{weight of every path atom}&=1/\mu,\\
\text{every cross-tag protected intersection}&\text{is empty or a
singleton.}
\end{array}
\tag{4.3}
\]

After clearing by any \(\mathfrak D\) divisible by \(\mu\), tag and
target degrees are at most \(\mathfrak D\), some target degrees equal
\(\mathfrak D\), and the weighted matching cut has value at least
\(n\mathfrak D/2\).

#### Proof

Above each tag \(i\), take \(\mu/2\) line variants from Lemma 4.1.
Their complete central trajectory, and in particular every \(X_{ij}\),
is common.

Use Lemma 4.2 sequentially to choose \(\mu/2\) fillers above every tag.
Require every filler to avoid every line target and require fillers on
different tags to be target-disjoint.  Only polynomially many targets
have been exposed at every stage, so the lemma applies.  Same-tag filler
intersections are harmless.

Give every selected path weight \(1/\mu\).  One tag contains \(\mu\)
paths, so its total is one.  At \(X_{ij}\), the line half of tag \(i\)
and the line half of tag \(j\) contribute

\[
             {1\over2}+{1\over2}=1.
\tag{4.4}
\]

Every other line target receives mass from only one half-tag and has
load at most \(1/2\).  The same holds for filler targets.  This proves
(4.3).

After clearing, every path has \(\mathfrak D/\mu\) labelled copies.
Let \(\mathcal L\) be all copies of all line variants.  Copies over one
tag conflict at their tag.  Copies over different tags share the
corresponding \(X_{ij}\).  Hence \(\mathcal L\) is a clique and

\[
       |\mathcal L|
       =n{\mu\over2}{\mathfrak D\over\mu}
       ={n\mathfrak D\over2},
       \qquad
       \nu(\mathcal L)=1.
\tag{4.5}
\]

Putting unit dual weight on \(\mathcal L\) gives

\[
       {w(E)\over\nu_w}
          ={n\mathfrak D\over2}.
\tag{4.6}
\]

The anchors have degree exactly \(\mathfrak D\), so
\(\mathfrak D\) is the ambient degree scale rather than a degree
renormalized inside \(\mathcal L\). \(\square\)

At the rational type level, (4.6) is

\[
       \sum_{P\in\mathcal L}x_P={n\over2},
       \qquad
       \max_{M\ {\rm matching}}
          \sum_{P\in M\cap\mathcal L}1\le1.
\tag{4.7}
\]

Thus the failure is an odd/clique matching-polytope cut, not target
overload.

## 5. Why this does not occur at half-fibre scale in the uniform isolated point

The absolute inequality \((Q!)^2\gg\mu\) is not the relevant test for the
uniform fractional point.  The relevant quantity is the fraction of the
entire raw tag fibre occupied by a line skeleton.

Let \(A\) be the raw oriented tag degree before isolated sampling.
Independently decorating every support by priorities multiplies both the
numerator and denominator below by the same factor.

### Lemma 5.1 (central-skeleton relative mass)

Fix the owner at the first physical phase and its complete ordered
sequence of \(\ell-1\) central departures and arrivals.  The relative
raw tag degree of all buffered completions of this skeleton is at most

\[
       \xi_{\rm skel}
       \le
       {2\over
       \binom{m+H}{m}(m)_{\ell-1}(H)_{\ell-1}}.
\tag{5.1}
\]

In particular,

\[
       \xi_{\rm skel}
          \le
       \exp[-(1-o(1))\ell\log m].
\tag{5.2}
\]

Allowing both two-step interpolations between consecutive crossing
owners multiplies (5.1) by at most \(2^n\), which does not change (5.2).

#### Proof

At a fixed physical phase, coordinate symmetry makes the owner uniform
on the \(\binom{m+H}{m}\) owner sets in the carrier.  Conditional on that
owner, the next \(\ell-1\) return-free departures form a uniform ordered
tuple of distinct owner coordinates, and the corresponding arrivals form
a uniform ordered tuple of distinct hole coordinates.  Hence fixing all
three data costs exactly the denominator in (5.1), up to the factor two
for reversal.  Prefix and suffix completions remain free and are already
included.

Finally,

\[
       \log(m)_{\ell-1}
          =(\ell+o(\ell))\log m,
\]

which alone proves (5.2); the other two denominator factors only improve
it. \(\square\)

### Proposition 5.2 (isolated sampling disperses the line bundle)

Suppose paths are marked independently with probability \(p\), retained
paths are a subset of the marked paths, and

\[
             pA=\mu_{\rm iso}.
\tag{5.3}
\]

Assume

\[
             {\mu_{\rm iso}\over Q}\gg m\log m.
\tag{5.4}
\]

This holds for the pointwise protected-pruning value
\(\mu_{\rm iso}=m^{11/6-o(1)}\).

With probability \(1-o(1)\), simultaneously for every tag and every
central line skeleton of the form above, its retained fraction in a good
tag fibre is at most

\[
             {2\over Qn\log m}.
\tag{5.5}
\]

Consequently the total normalized mass of all \(n\) bundles in one line
system is

\[
             O(1/(Q\log m))=o(1/Q).
\tag{5.6}
\]

#### Proof

Put

\[
             \theta={1\over Qn\log m}.
\tag{5.7}
\]

For a raw bundle \(\mathcal B\) of relative size at most
\(\xi_{\rm skel}\), its marked count \(Y_{\mathcal B}\) has mean at most
\(\mu_{\rm iso}\xi_{\rm skel}\).  The elementary binomial upper tail
gives

\[
 \Pr(Y_{\mathcal B}\ge\theta\mu_{\rm iso})
 \le
 \left({e\xi_{\rm skel}\over\theta}\right)^{
          \theta\mu_{\rm iso}}
 \le
 \exp[-(1-o(1))\mu_{\rm iso}/Q].
\tag{5.8}
\]

The number of tags times the number of central skeletons is at most the
number of raw labelled catalogue columns, hence at most

\[
             \exp[O(m\log m)].
\tag{5.9}
\]

Condition (5.4) makes the union bound in (5.8)--(5.9) tend to zero.
Isolation can only delete marked paths.  A good retained tag has size at
least \(\mu_{\rm iso}/2\), so its line-skeleton mass is at most
\(2\theta\).  Summing over \(n\) line tags gives (5.6). \(\square\)

The same high-probability event may be imposed when selecting the
isolated-pruning outcome used by the fractional-overload theorem.
Indeed, conditioning on an event of probability \(1-o(1)\) changes the
expectation of every nonnegative pruning ledger by only a
\((1+o(1))\) factor.  Thus the existence proof can choose a balanced
outcome which also avoids the displayed half-fibre line obstruction.

This proposition is specific to the exact line-skeleton amplification.
It is not a general weighted matching theorem; other distributed odd
systems remain possible.

## 6. Coefficient-one ledger for one near-design

The cleared weighted-colouring theorem asks for much more than one
coefficient-safe selection.  A local weighted cut can fail while its
entire physical support remains negligible.

One line system has

\[
       n=O(\ell)
\tag{6.1}
\]

tags and

\[
       \binom n2=O(\ell^2)
\tag{6.2}
\]

crossing anchors.  Declaring every anchor exceptional costs
\(O(\ell^2)=o(W)\) scalar middle targets.  Alternatively, discarding all
line tags removes at most

\[
       n(2Q+1)\ell=O(Q\ell^2)=o(W)
\tag{6.3}
\]

protected claims.  Both operations preserve literal integrality: one
deletes whole legal chunks or repairs literal target holes.

Therefore the line construction becomes a coefficient-scale obstruction
only if one proves a packing of

\[
             \Omega(W/\ell^2)
\tag{6.4}
\]

essentially anchor-disjoint line systems.  This is the scale at which
their middle exceptional-target ledger ceases to be \(o(W)\).  Packing
only \(o(W/\ell^2)\) systems is removable by the allowed scalar repair.

No such global packing follows from the local real-line encoding.  Its
construction would itself be a near-design theorem coupling almost all
carrier tags and almost all middle targets.  In particular, taking the
full coordinate orbit gives a fractional average but not an integral
anchor-disjoint packing.

## 7. Precise proved and conditional boundary

The claims surviving audit are:

* **Proved:** the \(n\)-line family consists of literal radius-\(Q\)
  chunks, and every pairwise protected intersection is exactly one middle
  owner.
* **Proved:** all chunks extend to displacement-zero cyclic schedules, so
  bounded displacement does not exclude the construction.
* **Proved:** for an adversarial rational point on these actual catalogue
  fibres, polynomial atomization gives maximum target load one but a
  cleared clique of size \(n\mathfrak D/2\).  Hence no universal weighted
  matching theorem follows from the currently recorded geometric and
  degree hypotheses.
* **Proved:** the exact skeleton is exponentially thin in a uniform raw
  fibre, and the isolated-pruning point can be chosen so its total line
  mass is \(o(1/Q)\).
* **Proved:** one local line system is removable at \(o(W)\) literal
  scalar cost.
* **Unproved:** an \(\Omega(W/\ell^2)\) anchor-disjoint packing of line
  systems in one global cyclic-interval near-design.
* **Unproved:** the weighted matching cut for the particular
  isolated-pruning point.
* **Unproved:** a direct matching covering all but the coefficient-safe
  exceptional tags for the single-near-design target.

Accordingly, the line arrangement definitively closes the universal
weighted-colouring lane, but not the coefficient-one existence lane.  A
successful continuation must exploit the chosen-point distribution or
work directly with one large matching; star-cover geometry alone cannot
do it.
