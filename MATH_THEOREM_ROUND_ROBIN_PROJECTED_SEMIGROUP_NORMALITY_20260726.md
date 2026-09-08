# The \(\mathbb Z_4^r\) round-robin cycle semigroup is normal after shallow macroprofile projection—and therefore rigid

Date: 2026-07-26

Method: pure mathematics.  No search or solver input is used.

## 0. Outcome

Inside one canonical tensor packet, orient every local \(Q_2\) as a
four-cycle and identify its phase with \(\mathbb Z_4\).  The product phase
space is \(\mathbb Z_4^r\).  Use the round-robin physical direction word

\[
 \alpha_1,\ldots,\alpha_r,\,
 \beta_1,\ldots,\beta_r,\,
 \alpha_1,\ldots,\alpha_r,\,
 \beta_1,\ldots,\beta_r,                            \tag{0.1}
\]

where \(\alpha_i,\beta_i\) are the two alternating directions in local
block \(B_i\).  Every resulting component is an isometric \(C_{4r}\).
Assume throughout that

\[
                         1\le q\le H=o(r).             \tag{0.2}
\]

At these depths, a window meets \(q\) distinct macroblocks.  If the source
macroprofile is \(k\), every round-robin cycle has exactly the projected
column

\[
 \boxed{
 \gamma_{q,k}
 =4\sum_{t\in\mathbb Z_r}
   e_{\left(q,k,k-\mathbf1_{[t,t+q)}\right)}.}          \tag{0.3}
\]

Here \([t,t+q)\) is a cyclic interval in the ordered selected block set.
The factor \(4\) comes from the four copies of the macroblock word
\(1,2,\ldots,r\) in (0.1).  Formula (0.3) is independent of

* the local owner phase;
* the local associator corner
  \(\varepsilon\in\{0,1\}^r\);
* the particular cycle in the round-robin factor.

Consequently the projected semigroup of individual round-robin cycle
columns is the one-ray semigroup

\[
                         \mathbb N\gamma_k,\qquad
 \gamma_k=(\gamma_{q,k})_{q\le H}.                    \tag{0.4}
\]

It is normal in its group lattice:

\[
 \boxed{
 \operatorname{cone}(\gamma_k)\cap
 \operatorname{gp}_{\mathbb Z}(\gamma_k)
 =\mathbb N\gamma_k.}                                 \tag{0.5}
\]

For canonical disjoint packets, retain one packet tag in every column.
If \(g_P\) is the whole-factor census of packet \(P\), all \(2^r\)
corners have the same tagged column

\[
                         c_{P,\varepsilon}=(e_P,g_P).  \tag{0.6}
\]

The complete tagged projected semigroup is

\[
 \boxed{
 \mathsf S_{\rm rr}
 =\left\{
 \left((n_P)_P,\sum_Pn_Pg_P\right):
 n_P\in\mathbb Z_{\ge0}
 \right\},}                                           \tag{0.7}
\]

which is isomorphic to the free semigroup
\(\mathbb N^{\mathfrak P}\), hence normal.  Its Graver basis before
duplicate columns are identified is exactly

\[
 \boxed{
 \mathcal G
 =\{\pm(e_{P,\varepsilon}-e_{P,\varepsilon'}):
       P\in\mathfrak P,\ \varepsilon\ne\varepsilon'\}.}             \tag{0.8}
\]

Every Graver move has \(\ell_1\)-norm two and zero macroprofile action.

Thus the structured projected semigroup has **no asymptotic holes at all**.
Deleting the exponentially small canonical leave outside the full packets,
or deleting any union of whole packets, preserves (0.7).  For simultaneous
unweighted census error through \(H\) depths, a deleted owner costs \(H\)
profile occurrences, so a general packet deletion must have size
\(o(W/H)\), not merely \(o(W)\); the canonical exponential leave satisfies
this automatically.

This positive normality result does not round the desired cross-sector
flow.  It shows instead that, on the exact-owner slice \(n_P=1\), the
projected census is the single fixed vector

\[
                         \sum_Pg_P.                   \tag{0.9}
\]

There is no projected choice to round.  The \(\varepsilon\)-cube acts only
inside the fibres forgotten by macroprofile projection.  Therefore the
remaining alternative is a cone-membership statement:

\[
 \boxed{\text{Does the fixed census (0.9) already have balanced target
 columns, up to }o(W)\text{?}}                         \tag{0.10}
\]

If not, semigroup normality cannot help, because the desired flow lies
outside the round-robin projected cone on the exact-owner slice.

For one balanced tensor sector, (0.10) fails maximally under sectorwise
quotas: (0.3) reaches only \(r\) of the \(\binom rq\) symmetric deletion
profiles.  This is the previously proved conditional deficit

\[
                         1-{r\over\binom rq}.           \tag{0.11}
\]

It remains explicitly conditional.  A target may be supplied from a
different source macroprofile, and the global cross-sector occupancy flow
uses precisely that freedom.  The present theorem proves neither a global
deficit nor global balance.  It proves that integer decomposition and
Graver complexity are not the live issue for the structured projected
columns: **global cone membership and fine labelled-target collisions are.**

The Hamming phase columns with one fixed direction order obey the same
theorem.  Allowing many genuinely different direction orders creates a
nontrivial cyclic-interval design semigroup; no normality assertion for
that enlarged semigroup is made here.

There is, moreover, an asymptotic obstruction below macroprofile
projection.  In the canonical first-\(r\)-eligible packet atlas, a
round-robin \(q\)-window touches one cyclic run of \(q\) selected blocks.
The touched blocks are no longer locally eligible in the target, while
every untouched selected block remains eligible.  Therefore any target hit
at depth \(q<r\) must contain a physical run of at least \(q/2\)
consecutive non-eligible eight-blocks.  A uniform rank-\((m-q)\) target has
independent pre-conditioning eligible-block density
\[
                         {3\over32}+o(1).              \tag{0.12}
\]
Consequently, whenever \(q/\log m\to\infty\),
\[
 \boxed{
 {\,\#\{\text{targets hit by the canonical round-robin atlas at depth }q\}
  \over \binom{2m+1}{m-q}}
 \le O(m^{3/2})\left(1-{3\over32}+o(1)\right)^{q/2}
 =o(1).}                                               \tag{0.13}
\]
At \(q=x\sqrt m\), the atlas therefore misses
\((1-o(1))N_q=\Theta_x(W)\) targets.  Thus projected normality is not only
vacuous: the fixed physical round-robin order is globally false for the
Gaussian band.  The recursive nonlinear packet factor or a catalogue of
owner-dependent direction orders is essential.

## 1. Round-robin cycles and their macroblock word

In each selected local block \(B_i\), either associator shore partitions
the same 24 middle owners into oriented \(Q_2\)'s.  Choose an oriented
local square

\[
                         z_i(0),z_i(1),z_i(2),z_i(3),   \tag{1.1}
\]

whose directions alternate

\[
                         \alpha_i,\beta_i,\alpha_i,\beta_i.          \tag{1.2}
\]

On the Cartesian product of \(r\) such squares, a round-robin component
increments local coordinates in the order

\[
 1,2,\ldots,r,\ 1,2,\ldots,r,\ 1,2,\ldots,r,\ 1,2,\ldots,r,          \tag{1.3}
\]

where the first and third passes use the current \(\alpha/\beta\)
direction and the second and fourth use the other.  In physical cube
directions this is (0.1).  Every one of the \(2r\) physical directions
occurs once in the first \(2r\) positions and the word then repeats.
Hence every component is an isometric \(C_{4r}=C_{2(2r)}\).

The macroblock label word is simply

\[
                         (1,2,\ldots,r)^4.             \tag{1.4}
\]

For \(q<r\), every length-\(q\) interval in (1.4) consists of \(q\)
distinct block labels.  Its label set is a cyclic interval
\([t,t+q)\subseteq\mathbb Z_r\).  Every such interval occurs at four
starts of a component.

All middle owners in one packet have the same macroblock occupancy on the
selected blocks—four points in every \(B_i\)—and the exterior is frozen.
Let \(k\) be this complete macroprofile.  A lower \(q\)-window removes one
selected point in each touched block, so its profile is

\[
                         k-\mathbf1_{[t,t+q)}.          \tag{1.5}
\]

Equations (1.4)--(1.5) prove (0.3).  The argument uses only local
cardinalities, which are identical on the two associator shores, so the
column is independent of \(\varepsilon\).

The upper profile is the complementary translate

\[
                         k+\mathbf1_{[t,t+q)},          \tag{1.6}
\]

and has the identical rigidity.  Including both signs merely appends a
second fixed copy to \(\gamma_k\).

## 2. Normality of the individual-cycle projection

Let \(L_k=\mathbb Z\gamma_k\) be the group generated by the one projected
cycle column.  Every point of
\(\mathbb R_{\ge0}\gamma_k\cap L_k\) has the form

\[
                         a\gamma_k,\qquad
 a\in\mathbb Z_{\ge0}.                                \tag{2.1}
\]

This is exactly \(\mathbb N\gamma_k\), proving (0.5).  Notice that
normality is relative to the physical group lattice \(L_k\).  In the
ambient coordinate lattice, the factor four in (0.3) is a visible
congruence; it is not a semigroup hole.

This proves more than eventual or approximate normality: the projected
semigroup is normal for every \(r\) and every \(H<r\).

The determinant-\(2\) triangle from the unrestricted cycle catalogue
disappears under this projection.  Its three translated cycles have the
same \(\gamma_k\), so the three offending columns become identical.  The
projection removes the owner-incidence information which carried the
triangle.

## 3. Tagged packet factors and the Graver basis

Let \(\mathfrak P\) be the canonical family of pairwise disjoint tensor
packets covering all but \(o(W)\) middle owners.  In packet \(P\), every
\(\varepsilon\) gives a whole \(C_{4r}\)-factor on the same support.
Let \(g_{P,\varepsilon}\) be its simultaneous lower/upper macroprofile
census through depth \(H\).

### Lemma 3.1

\[
                         g_{P,\varepsilon}=g_P          \tag{3.1}
\]

for every \(\varepsilon\).

#### Proof

Every cycle in every corner has macroblock word (1.4), and all cycles
partition the same owner support.  Formula (0.3), summed over the
\(24^r/(4r)\) cycles, is therefore independent of the local resolution.
\(\square\)

Introduce the tagged column

\[
                         c_{P,\varepsilon}=(e_P,g_P).   \tag{3.2}
\]

If \(z=(z_{P,\varepsilon})\) is an integer relation among these columns,
the packet-tag rows give

\[
                         \sum_\varepsilon z_{P,\varepsilon}=0
                         \qquad(P\in\mathfrak P).       \tag{3.3}
\]

Conversely, (3.3) annihilates the macroprofile rows because those rows are
constant within each packet.  Hence the integer kernel is the direct sum

\[
 \ker_{\mathbb Z}C
 =\bigoplus_{P\in\mathfrak P}
   \left\{z\in\mathbb Z^{2^r}:\sum_\varepsilon z_\varepsilon=0\right\}.
                                                                    \tag{3.4}
\]

The conformally primitive elements of one zero-sum lattice are exactly
\(e_\varepsilon-e_{\varepsilon'}\).  This proves the Graver formula
(0.8).

Quotienting duplicate columns leaves one column \(c_P=(e_P,g_P)\) per
packet.  They are linearly independent because of the tag rows.  Their
nonnegative integer semigroup is free and is exactly (0.7), proving
normality.

On the exact-owner slice, the tag equations impose

\[
                         \sum_\varepsilon x_{P,\varepsilon}=1.       \tag{3.5}
\]

Every integral corner and every fractional convex combination then has
the same macro census \(g_P\).  Thus even fractional rounding has no
macroprofile effect.

## 4. Boundary deletion

The canonical first-\(r\)-eligible packet construction leaves
\(e^{-\Omega(m)}W=o(W)\) middle owners outside all full packets.  Remove
that family.  The remaining supports are disjoint full packets, so the
tagged normality theorem applies literally.

More generally, remove any family of complete packets.  This deletes the
corresponding free generators from (0.7); a face of a free semigroup is
again free and normal.  If simultaneous profile error is measured by the
unweighted sum over \(q\le H\), its error contribution is exactly \(H\)
times the deleted owner mass (twice that when lower and upper signs are
both counted).  Hence \(o(W)\) aggregate error requires an
\(o(W/H)\) deletion.  This distinction does not affect normality.

The theorem does not cover arbitrary deletion of isolated owners inside a
packet.  Such a deletion breaks its \(C_{4r}\)-factor and creates a
separate path-completion/absorber problem.  Therefore “delete \(o(W)\)
boundary owners” must mean the canonical outside leave or a union of whole
packet boundaries for this exact statement.

## 5. Cone membership versus semigroup saturation

Let

\[
 G^{\rm rr}=\sum_{P\in\mathfrak P}g_P                              \tag{5.1}
\]

be the unique projected census on the exact-owner slice.  Let
\(G^{\rm bal}\) be any desired balanced integral rounding of the
cross-sector flow.

### Theorem 5.1 (exact criterion)

There is a structured round-robin packet selection with projected census
\(G^{\rm bal}\) if and only if

\[
                         G^{\rm bal}=G^{\rm rr}.        \tag{5.2}
\]

With packet-boundary deletion whose full simultaneous census has
\(o(W)\) mass—equivalently an \(o(W/H)\) owner deletion in the unweighted
\(H\)-depth ledger—and \(o(W)\) allowed profile error, the corresponding
criterion is

\[
                         \|G^{\rm bal}-G^{\rm rr}\|_1=o(W),          \tag{5.3}
\]

after charging every removed packet's full census to the error ledger.

#### Proof

Necessity follows from (3.5) and Lemma 3.1.  Sufficiency is immediate:
choose any corner in every retained packet. \(\square\)

Thus normality cannot convert the abstract flow (0.1) into round-robin
cycles.  The abstract flow must first be shown to agree with the unique
native census, or the cycle catalogue must be enlarged by genuinely
different macroblock orders.

## 6. The conditional sectorwise comparison

Fix one packet and one depth \(2\le q<r\).  If its \(24^r\) starts are
required to be spread uniformly over all symmetric profiles

\[
                         k-\mathbf1_J,\qquad J\in\binom{[r]}q,       \tag{6.1}
\]

then every cell has ideal mass \(24^r/\binom rq\).  The round-robin
factor is supported only on the \(r\) cyclic intervals and therefore has
missing ideal mass

\[
                         24^r\left(1-{r\over\binom rq}\right).       \tag{6.2}
\]

This reproduces the sectorwise obstruction.  It does **not** prove that
\(G^{\rm rr}\) is globally unbalanced, because the global target census
may feed (6.1) from packets having other source profiles.  Equations
(5.2)--(5.3), rather than (6.2), are the unconditional criterion.

## 7. Hamming phases and enlarged order catalogues

For a fixed Hamming kernel and a fixed cyclic direction order, changing
the affine phase class translates cube vertices but does not change the
direction word.  Hence its projected aggregate macroprofile column is
again fixed, and the duplicate-column normality proof applies.

If one admits genuinely different direction orders \(\sigma\), the
columns become

\[
 4\sum_{t\in\mathbb Z_r}
 e_{\left(q,k,k-\mathbf1_{J_t(\sigma)}\right)},                     \tag{7.1}
\]

where \(J_t(\sigma)\) is the macroblock set in the corresponding
length-\(q\) interval.  Their semigroup is a simultaneous cyclic-interval
design semigroup.  It is no longer one-ray, and the proof above gives no
normality or bounded Graver basis for it.

The recursive nonlinear \(Q_s\) factor proves literal injectivity inside
each packet through \(q\le s/2\), but its outer packet census can still
collide at physical targets.  Thus enlarging the internal factor solves
the one-packet consecutive-window problem; it does not settle the global
criterion (5.3).

## 8. Final verdict

After shallow macroprofile projection, the structured
\(\mathbb Z_4^r\) round-robin semigroup is exactly normal, with Graver
complexity two.  This is not a route to constant one because the
projection also kills every local associator degree of freedom.

There is therefore no projected asymptotic semigroup hole to exhibit.
There is, however, the fine asymptotic hole (0.13), which closes the fixed
round-robin atlas.  The exact remaining alternatives are:

1. enlarge the catalogue by many macroblock direction orders and prove a
   new interval-design decomposition theorem; or
2. use an owner-dependent direction order, such as the recursive nonlinear
   packet factor, so touched blocks do not form one run in the canonical
   first-\(r\) list; or
3. abandon the fixed first-\(r\) packet order through cross-packet trades
   or a context-dependent packet atlas.

Merely changing the local \(\varepsilon\)-corner preserves the macroblock
word (1.4) and therefore cannot evade Lemma 9.1.

## 9. Fine eligibility-run obstruction for the canonical round-robin atlas

We prove (0.13).  Use the canonical partition into labelled eight-blocks
\[
                         B_1,\ldots,B_B,\qquad
                         B=\lfloor m/4\rfloor.          \tag{9.1}
\]
Call a block eligible for a set \(T\) when
\[
                         T\cap B_i\in\mathcal V_i,      \tag{9.2}
\]
where every member of \(\mathcal V_i\) has cardinality four.

Suppose \(T\) is the lower depth-\(q\) target of a round-robin cycle start
\(X\).  Let
\[
                         I(X)=(i_1<\cdots<i_r)          \tag{9.3}
\]
be the first \(r\) eligible blocks of \(X\).  Because \(q<r\), the
round-robin macroblock word (1.4) touches a cyclic interval
\[
                         J=\{t,t+1,\ldots,t+q-1\}
                         \pmod r                       \tag{9.4}
\]
of \(q\) distinct selected positions.

For \(j\notin J\), no local coordinate in \(B_{i_j}\) changes, so
\[
                         T\cap B_{i_j}
                         =X\cap B_{i_j}\in\mathcal V_{i_j}.          \tag{9.5}
\]
For \(j\in J\), exactly one selected coordinate is deleted, and hence
\[
                         |T\cap B_{i_j}|=3;             \tag{9.6}
\]
such a block is not eligible for \(T\).  Thus the eligibility word of
\(T\), restricted to the cyclic selected list, has one run of \(q\)
zeros and \(r-q\) ones.

Every unselected physical block before \(i_r\) is ineligible for \(X\),
by the first-\(r\) rule.  It is frozen between \(X\) and \(T\), and is
therefore also ineligible for \(T\).  If the cyclic run (9.4) does not
cross the cut between \(i_r\) and \(i_1\), all its \(q\) selected blocks
lie in one physical interval containing no target-eligible block.  If it
crosses the cut, its two linear pieces have total size \(q\), so one piece
has size at least \(q/2\); that piece again lies in a physical interval
with no eligible block.  We have proved:

### Lemma 9.1 (necessary empty run)

Every target hit by the canonical round-robin atlas at depth \(q<r\)
has a linear run of at least \(\lceil q/2\rceil\) consecutive
eight-blocks, none eligible for the target.

Now generate a random set \(\mathbf T\) by choosing every coordinate
independently with probability
\[
                         p={m-q\over2m+1},              \tag{9.7}
\]
and then condition on \(|\mathbf T|=m-q\).  Before conditioning, the block
eligibility indicators are independent, with common probability
\[
\begin{aligned}
 \pi_q
 &=24p^4(1-p)^4\\
 &={3\over32}+o(1)                                    \tag{9.8}
\end{aligned}
\]
uniformly for \(q=o(m)\).

Let \(L=\lceil q/2\rceil\).  A union bound over at most \(B\) possible
linear runs gives
\[
 \Pr(\text{an eligible-free run of length }L)
 \le B(1-\pi_q)^L.                                    \tag{9.9}
\]
The conditioning event has probability \(\Theta(m^{-1/2})\), uniformly
for \(q=O(\sqrt m\,\omega(m))=o(m^{2/3})\) by the local central limit
estimate.  Hence conditioning multiplies (9.9) by at most \(O(\sqrt m)\):
\[
 \Pr(\text{such a run}\mid|\mathbf T|=m-q)
 \le O(m^{3/2})(1-\pi_q)^{q/2}.                       \tag{9.10}
\]

If \(q/\log m\to\infty\), the right side tends to zero.  Lemma 9.1 then
proves (0.13).  At \(q=x\sqrt m\), the target layer has
\(N_q=\Theta_x(W)\), proving a macroscopic missing-target obstruction.

The theorem is specific to the fixed round-robin order aligned with the
ordered first-\(r\) eligible list.  An owner-dependent recursive direction
order need not make its touched blocks one physical/eligibility run and is
not covered by this no-go.
