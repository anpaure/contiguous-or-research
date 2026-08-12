# Audit of the full internal-quartet Hall cut and dense cross-axis scheduling

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, finite search, or
web input is used.

## 0. Verdict

The principal theorem in
`MATH_THEOREM_FULL_INTERNAL_QUARTET_ATLAS_GAUSSIAN_HALL_CUT_20260726.md`
is correct.

For a fixed quartet decomposition of \([2m]\), every window all of whose
Johnson axes lie inside individual quartets preserves the number of full
quartets between a middle owner and its lower intersection.  At

\[
                         q=\lfloor A\sqrt m\rfloor
\]

the profile

\[
                         k={m\over32}-{A\over4}\sqrt m+O(1)
\]

has the exact source/target asymptotic

\[
 {\#\{X:|X|=m,\ F(X)=k\}
  \over
  \#\{T:|T|=m-q,\ F(T)=k\}}
 =e^{-A^2/11+o(1)}<1.                              \tag{0.1}
\]

A \(\Theta_A(\sqrt m)\)-window of these profiles has positive target
density, so every entirely internal middle-owner factor has
\(\Omega_A(W)\) lower holes.  The empty-quartet version gives the same
upper conclusion.

The conversion to cross-quartet occurrences is also valid: any successful
factor must have \(\Omega_A(W)\) based depth-\(q\) windows containing a
cross-quartet axis.  For an owner-disjoint decomposition into physical
\(Q_r\) packets factored by isometric \(C_{2r}\)'s, with \(q<r\), this
implies

\[
 {1\over W}\sum_Ps(P)|P|=\Omega_A(r/q),             \tag{0.2}
\]

where \(s(P)\) is the number of cross-quartet axes in packet \(P\).

The packet hypothesis in the preceding implication is essential.  The
Hall theorem itself is architecture-free, but (0.2) uses the facts that an
axis occurs twice in a length-\(2r\) direction word and that each owner is
one cyclic start.  For overlapping packet rounds or nonisometric compilers,
one must charge actual marked direction occurrences instead.

There is a further scheduling requirement absent from the original note.
If the \(2s\) occurrences of the crossing axes have cyclic gaps
\(g_1,\ldots,g_{2s}\), then the exact fraction of depth-\(q\) starts which
see a crossing is

\[
 \boxed{
 \phi_q={1\over2r}\sum_{i=1}^{2s}\min(g_i,q).}       \tag{0.3}
\]

Thus \(s=\Theta(r/q)\) is only the correct quantity scale.  To realize the
optimal occurrence mass, the crossing axes must also be dispersed around
the direction word.  Quasi-uniform placement in the permutation half of a
standard \(\pi\pi\) isometric word is optimal up to rounding.  This is the
correct dense-cross-axis scheduling target; bounded one-axis rounds give
only \(O(q/r)=o(1)\) crossing fraction per round.

## 1. The invariant is atlas-independent

Partition \([2m]\) into \(c=m/2\) quartets.  For a set \(S\), put

\[
                         F(S)=\#\{B:B\subseteq S\}.
\]

### Lemma 1.1 (full-quartet invariance)

Let

\[
                         X_0,X_1,\ldots,X_q
\]

be any Johnson path such that every changed coordinate pair is contained in
one quartet.  Put \(T=\bigcap_{i=0}^qX_i\).  Then

\[
                         F(T)=F(X_i)                 \tag{1.1}
\]

for every \(i\).  No return-free, fixed-one-factor, or fixed-product-cell
hypothesis is needed for this equality.

#### Proof

An internal Johnson move preserves the number of selected coordinates in
each quartet separately.  Hence every owner in the path has the same local
rank vector.  If one quartet has local rank four, no coordinate in it can
be inserted and an internal Johnson move cannot delete one of its
coordinates: there is no absent coordinate in that quartet to insert.
Thus it remains full throughout and is full in the intersection.

If a quartet has local rank at most three, it is not full in any owner and
cannot be full in their intersection.  This proves (1.1).  \(\square\)

This proves the claimed invariant for the complete internal atlas, including
all one-factors of \(J(4,1),J(4,2),J(4,3)\), arbitrary changes of those
one-factors, and arbitrary internal axis orders.  Changing the internal
local frame cannot escape it.

For the upper union \(U=\bigcup_iX_i\), the dual invariant is the number of
empty quartets.  It also follows by complementing every owner in Lemma 1.1.

## 2. Exact profile enumeration

Let

\[
 h(z)=1+4z+6z^2+4z^3=(1+z)^4-z^4.                 \tag{2.1}
\]

After choosing the \(k\) full quartets, the other \(c-k\) quartets are
proper subsets.  Therefore

\[
 |\mathcal T_{q,k}|
 =\binom ck[z^{m-q-4k}]h(z)^{c-k},                 \tag{2.2}
\]

\[
 |\mathcal X_k|
 =\binom ck[z^{m-4k}]h(z)^{c-k}.                   \tag{2.3}
\]

The common binomial factor cancels.

Normalize the coefficients by the random variable

\[
 \Pr(J=j)={\binom4j\over15},\qquad0\le j\le3.
\]

Direct moment calculation gives

\[
 \mu=\mathbb EJ={28\over15},
 \qquad
 \sigma^2=\operatorname{Var}J={176\over225}.        \tag{2.4}
\]

Indeed, the sums of \(j\binom4j\) and \(j^2\binom4j\) over all subsets
are \(32\) and \(80\); removing the full set subtracts \(4\) and \(16\).

## 3. Independent check of the Gaussian exponent

Write

\[
 q=A\sqrt m+O(1),
 \qquad
 k={m\over32}+y\sqrt m+O(1),
 \qquad
 d=c-k.
\]

Then

\[
 d={15m\over32}-y\sqrt m+O(1),
 \qquad
 \sigma^2d={11m\over30}+O(\sqrt m).                \tag{3.1}
\]

For

\[
 s_T=m-q-4k,\qquad s_X=m-4k=s_T+q,
\]

one obtains

\[
 s_T-\mu d
 =\left(-A-{32y\over15}\right)\sqrt m+O(1),         \tag{3.2}
\]

\[
 s_X-\mu d
 =-{32y\over15}\sqrt m+O(1).                       \tag{3.3}
\]

The span-one lattice local central limit theorem is uniform for bounded
\((A,y)\), and hence

\[
\begin{aligned}
 \log{|\mathcal X_k|\over|\mathcal T_{q,k}|}
 &=-{(s_X-\mu d)^2-(s_T-\mu d)^2\over2\sigma^2d}+o(1)\\
 &={15A^2+64Ay\over11}+o(1).                        \tag{3.4}
\end{aligned}
\]

At \(y=-A/4\), this is \(-A^2/11+o(1)\), proving (0.1).
Moreover, throughout

\[
 \left|y+{A\over4}\right|\le {A\over128},          \tag{3.5}
\]

the exponent is at most \(-A^2/22+o(1)\).

## 4. The hard profile window has positive mass

This step can be made quantitative rather than leaving the conditional
variance implicit.  Under an independent Bernoulli-\(p\) law in one
quartet, let

\[
 K=\mathbf1_{\{\text{quartet full}\}},
 \qquad L=\text{local rank}.
\]

Then

\[
 \mathbb EK=p^4,\qquad \mathbb EL=4p,
\]

\[
 \operatorname{Var}K=p^4(1-p^4),
 \qquad
 \operatorname{Var}L=4p(1-p),                     \tag{4.1}
\]

and

\[
 \operatorname{Cov}(K,L)=4p^4(1-p).                \tag{4.2}
\]

The conditional Gaussian variance per quartet is therefore

\[
 v(p)=p^4(1-p^4)-4p^7(1-p),                        \tag{4.3}
\]

so at \(p=1/2\),

\[
                         v(1/2)={11\over256}.        \tag{4.4}
\]

With \(c=m/2\) quartets, the conditional variance of \(F\), given total
rank \(m-q\), is

\[
                         {11m\over512}+O(\sqrt m).  \tag{4.5}
\]

Choose

\[
 p={m-q\over2m}
 ={1\over2}-{A\over2\sqrt m}+O(m^{-1}).
\]

The conditional centre of the full-quartet count is

\[
 cp^4={m\over32}-{A\over8}\sqrt m+O(1).            \tag{4.6}
\]

The profile centre used in (0.1) is only another fixed number of conditional
standard deviations away, and the window (3.5) has a fixed positive width
on that scale.  The bivariate lattice local central limit theorem therefore
gives a constant \(c_A>0\) for its target-layer mass.  This verifies the
positive-density step.

## 5. Hall deficit and the physical-crossing consequence

Let \(\mathcal K_A\) be the integer \(k\)-window from (3.5).  By Lemma 1.1,
every internal source for \(\mathcal T_{q,k}\) lies in \(\mathcal X_k\).
The source classes are disjoint as \(k\) varies.  Hence internal windows
miss at least

\[
 \sum_{k\in\mathcal K_A}
 \left(|\mathcal T_{q,k}|-|\mathcal X_k|\right)
 \ge(c_A-o(1))(1-e^{-A^2/22})N_q.                  \tag{5.1}
\]

Since

\[
                         {N_q\over W}\to e^{-A^2}, \tag{5.2}
\]

this is \((\delta_A-o(1))W\) for some \(\delta_A>0\).

Now take an arbitrary middle-owner factor and split its based depth-\(q\)
windows into internal and noninternal windows.  The internal windows can use
at most the source capacity in (5.1).  Each noninternal based window supplies
at most one further target.  Therefore covering the deficient profile
window requires at least

\[
                         (\delta_A-o(1))W            \tag{5.3}
\]

noninternal based windows.  A window is noninternal only if at least one of
its physical Johnson axes meets two distinct quartets.  This proves the
\(\Omega_A(W)\) crossing-occurrence claim without comparing to one frozen
baseline factor.

## 6. Exact marked-direction scheduling

The occurrence-to-axis conversion can be sharpened.

### Lemma 6.1 (exact cyclic marked-window count)

Let a cyclic direction word have length \(2r\), and mark \(2s\) positions.
Let

\[
                         g_1,\ldots,g_{2s}\ge1,
 \qquad \sum_{i=1}^{2s}g_i=2r,
\]

be the cyclic distances between consecutive marked positions.  The number
\(M_q\) of cyclic starts whose next \(q\) directions contain a mark is

\[
 \boxed{
 M_q=2r-\sum_{i=1}^{2s}(g_i-q)_+
     =\sum_{i=1}^{2s}\min(g_i,q).}                  \tag{6.1}
\]

Consequently

\[
                         {M_q\over2r}
 \le\min\left(1,{sq\over r}\right).                \tag{6.2}
\]

#### Proof

The open gap between two marked positions at cyclic distance \(g_i\)
contains \(g_i-1\) unmarked directions.  Exactly \((g_i-q)_+\) length-\(q\)
windows lie wholly in that unmarked run.  Summing the disjoint unmarked
windows gives the first expression in (6.1); the second follows from
\(g-(g-q)_+=\min(g,q)\).  Finally each summand is at most \(q\), while
their sum is also at most \(\sum g_i=2r\).  \(\square\)

The bound is sharp as a marking statement.

* If \(sq\le r\), equality \(M_q=2sq\) holds exactly when all marked gaps
  are at least \(q\).
* If \(sq\ge r\), full coverage \(M_q=2r\) holds exactly when all marked
  gaps are at most \(q\).

### Lemma 6.2 (isometric direction words)

The direction word of an isometric \(C_{2r}\subset Q_r\) is

\[
                         \pi\pi                    \tag{6.3}
\]

for a permutation \(\pi\) of the \(r\) axes, after a cyclic shift.

#### Proof

Every length-\(r\) arc of an isometric \(C_{2r}\) joins antipodal cube
vertices, so its directions are all distinct.  Thus every consecutive
length-\(r\) block of the direction word is a permutation of all axes.
Comparing two consecutive such blocks removes direction \(d_i\) and adds
direction \(d_{i+r}\); equality of their multisets forces
\(d_{i+r}=d_i\) for every \(i\).  \(\square\)

If \(s\) axes are physically crossing, their marked positions in
\(\pi\pi\) occur in two identical copies.  Choosing their positions in
\(\pi\) as evenly as possible makes all marked gaps equal to
\(\lfloor r/s\rfloor\) or \(\lceil r/s\rceil\).  Hence the union-bound
scale in (6.2) is attainable, up to the unavoidable integer rounding.

## 7. Weighted packet toll

Let \(\mathcal P\) be an owner-disjoint packet family covering
\((1-o(1))W\) owners.  Assume every \(P\in\mathcal P\) is a physical
\(Q_r\), every installed cycle is an isometric \(C_{2r}\), and \(q<r\).
Let \(s(P)\) be its number of cross-quartet axes.  Lemma 6.1, or just
(6.2), gives at most

\[
                         {s(P)q\over r}|P|           \tag{7.1}
\]

crossing based windows in \(P\).  Combining (5.3) and (7.1) proves

\[
 \boxed{
 {1\over W}\sum_{P\in\mathcal P}s(P)|P|
 \ge(\delta_A-o(1)){r\over q}.}                     \tag{7.2}
\]

This is a weighted average.  It does not force every packet to be dense;
the required mass may be concentrated on a positive owner fraction.
However, splitting the weighted sum over exceptional and nonexceptional
owner mass shows that an architecture with \(s(P)=o(r/q)\) on all but
\(o(W)\) owner mass cannot succeed.

If a construction is assembled from \(L\) one-cross-axis rounds and no
later operation merges their crossing directions into denser final packets,
then its final crossing count is at most \(L\) per owner occurrence.  Thus

\[
                         L=\Omega_A(r/q).            \tag{7.3}
\]

In particular bounded \(L\) fails whenever \(q=o(r)\).

## 8. Dense scheduling target

The audited theorem changes the constructive target.  At the fixed
Gaussian depth \(q=A\sqrt m\), a viable packet architecture must provide:

1. **axis density:** weighted crossing count
   \(\Omega_A(r/q)\) per owner occurrence;
2. **direction dispersion:** marked gaps in the compiler word arranged so
   that (6.1) supplies a positive fraction of all starts;
3. **owner closure:** the cross-quartet axes must coexist in one resolved
   owner tiling, rather than in incompatible overlapping rounds;
4. **all-depth chronology:** the same compiler must retain legal lower and
   upper traces at every protected depth; and
5. **profile transport:** the crossing windows must actually move mass
   between the deficient full/empty-quartet profiles, not merely cross a
   boundary physically.

There is no one-packet geometric obstruction to the required axis count.

### Lemma 8.1 (local dense-axis packet)

If

\[
                         r+s\le {m\over2},           \tag{8.1}
\]

then there is a physical middle-layer \(Q_r\) packet having exactly \(s\)
pairwise coordinate-disjoint cross-quartet axes and \(r-s\) internal axes.

#### Proof

Choose \(2s\) distinct quartets and one coordinate in each; pair these
coordinates across the quartets to make \(s\) crossing axes.  Choose
\(r-s\) further quartets and one internal coordinate pair in each.  The
condition (8.1) provides all required distinct quartets, and all \(r\) axes
are coordinate-disjoint.

From the remaining \(2m-2r\) coordinates choose a fixed
\((m-r)\)-set \(Z\).  The family obtained by taking \(Z\) together with
one endpoint of each active pair is a physical \(Q_r\) contained in the
middle layer, with exactly the asserted crossing axes.  \(\square\)

In the intended regime \(r=o(m)\) and \(s=\Theta(r/q)\), condition (8.1)
is automatic.  The obstruction is therefore global owner resolution and
signed scheduling, not the existence of one dense packet.

A natural sharp scheduling specification for one packet is

\[
                         s=\left\lceil\eta_A{r\over q}\right\rceil
\tag{8.2}
\]

crossing axes placed quasi-uniformly in \(\pi\).  Then (6.1) gives

\[
                         \phi_q=\eta_A+o(1)          \tag{8.3}
\]

in the sparse regime \(\eta_A<1\).  This meets the occurrence-scale toll
with the smallest possible order of crossing axes.  Constructing an exact
owner near-tiling with these densely accumulated physical axes, and proving
that their signed profile transports balance rather than reinforce, is the
remaining theorem.  Another bounded one-axis trade round cannot address it.

## 9. Audited boundary

Verified without additional assumptions:

1. the full-quartet invariant for every all-internal path;
2. the exact coefficient counts;
3. the exponent \(-A^2/11\);
4. positive target mass in the hard profile window;
5. a linear lower and upper Hall deficit; and
6. the necessity of \(\Omega_A(W)\) physically cross-quartet based windows.

Verified under the explicit isometric-packet hypotheses:

1. the weighted average toll \(\Omega_A(r/q)\); and
2. the exact marked-gap scheduling law (6.1).

Not proved:

1. a dense cross-axis owner resolution;
2. a compiler realizing the optimal gap schedule simultaneously at all
   depths; or
3. signed lower/upper profile cancellation and floor balance after the
   crossings are installed.
