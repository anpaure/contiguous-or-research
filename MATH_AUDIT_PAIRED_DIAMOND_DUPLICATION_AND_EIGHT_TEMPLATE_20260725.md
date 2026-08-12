# Owner-duplication audit and an eight-template separated coboundary

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Verdict

The paired-swap conveyor in
MATH_ATTACK_FOUR_TEMPLATE_ROTOR_COBBOUNDARY_20260725.md is locally exact
but globally unusable as a middle near-factor.

In every useful two-step block, the two carrier alternatives have a common
source and a common endpoint.  Across the paired carriers, the source
collars differ by one adjacent swap in positions \(p,p+1\).  Their source
middle owners coincide unless \(p=Q\).  A conveyor sweep has \(Q\) useful
blocks and only one possible \(p=Q\) exception.  Consequently every carrier
pair has at least

\[
 \frac M2-O\!\left(\frac M Q+Q\right)
 =\frac M2-o(M)
 \tag{0.1}
\]

forced equal-owner occurrence pairs.  Pairing all but \(o(N_H)\) carriers
therefore gives middle collision excess at least

\[
 \boxed{\frac14MN_H-o(W)=\frac14W-o(W).}
 \tag{0.2}
\]

Since the primary construction has only \(S=MN_H=W-o(W)\) middle
occurrences for \(W\) targets, (0.2) leaves at least
\(W/4-o(W)\) middle holes.  The conveyor cannot satisfy the owner
near-transversal gate.

A single four-template chain-swap gadget has the same structural defect:
one adjacent collar swap can separate the two source owners only at
\(p=Q\), and can separate the two two-step endpoint owners only at
\(p=Q-2\).  It cannot do both.

There is a local eight-template repair.  Arrange four arrival diamonds
around a Johnson 4-cycle.  Their four source owners, four intermediate
owners on either side of the switch, and four endpoints are all distinct.
The unperturbed four vertical strings cancel at every rank.  Perturb one
edge chain by one adjacent increment at a prescribed rank.  The resulting
eight-path switch is zero at every other rank and leaves one elementary
rectangle of squared norm four at the prescribed rank.

Thus owner separation requires a cycle of diamond edges, not a second
difference of two parallel edges.  The new open gate is packing these
four-carrier, eight-path separated cycles at coefficient scale while
keeping the full owner support near-rainbow.

## 1. Exact owner chronology of a paired diamond block

Consider two quotient states

\[
\begin{aligned}
 \omega_0&=(L;z_1,\ldots,z_{p-1},a,b,z_{p+2},\ldots,z_n;R_0),\\
 \omega_1&=(L;z_1,\ldots,z_{p-1},b,a,z_{p+2},\ldots,z_n;R_1),
\end{aligned}
 \qquad n=2Q.
 \tag{1.1}
\]

Their source middle owners are

\[
 X_i=L+\{\hbox{first \(Q\) collar labels of }\omega_i\}.
 \tag{1.2}
\]

Hence

\[
 \boxed{X_0=X_1\quad\Longleftrightarrow\quad p\ne Q.}
 \tag{1.3}
\]

Indeed, for \(p<Q\) both \(a,b\) lie in the first \(Q\) slots; for \(p>Q\)
both lie outside; and for \(p=Q\) exactly one lies inside.

Choose common departures \(x,x'\in L\), common arrivals \(y,y'\), and tie
the arrival-order bits oppositely.  The two intermediate owners have the
form

\[
 L+y+\{z_1,\ldots,z_{Q-1}\},
 \qquad
 L+y'+\{z'_1,\ldots,z'_{Q-1}\},
 \tag{1.4}
\]

where \(z'\) is the swapped collar.  They are distinct because \(y\ne y'\)
and neither arrival belongs to either displayed base.

After the two updates, the collar swap has moved to positions
\(p+2,p+3\), provided both remain in the collar.  Thus the two endpoint
owners coincide unless

\[
 p+2=Q.
 \tag{1.5}
\]

Equations (1.3) and (1.5) are incompatible: one adjacent swap cannot make
both source and endpoint owner pairs distinct.

During a front-swap injection block the two states start coalesced.  The
first intermediate owner is independent of which common lower label was
chosen as the first departure, because that departure is immediately
restored in the first collar slot.  The endpoint swap lies in positions
\(1,2\), both inside the middle prefix.  Hence every state of an injection
block also has equal paired owners.

## 2. Linear duplicate lower bound

Let one odd-position conveyor cycle consist of one injection block and the
\(Q\) useful blocks with

\[
 p=1,3,\ldots,2Q-1.
 \tag{2.1}
\]

Every useful block has a distinct source occurrence.  By (1.3), at most one
of these \(Q\) source pairs can have different owners.  Thus a length-\(M\)
paired conveyor has at least

\[
 E_{\mathrm{pair}}
 \ge
 \frac M2-O\!\left(\frac M Q+Q\right)
 \tag{2.2}
\]

pairwise disjoint equal-owner occurrence pairs.  The same estimate holds
for the even-position conveyor.  Injection states only increase the number
of equal-owner pairs and are not needed in (2.2).

Let \(S=MN_H\) be the total number of primary middle-owner occurrences and
let \(D_m\) be their number of distinct supports.  If occurrences are
partitioned into owner classes of sizes \(d_X\), then

\[
 S-D_m=\sum_X(d_X-1).
 \tag{2.3}
\]

Any family of disjoint equal-owner occurrence pairs has size at most the
right side of (2.3): a class of size \(d_X\) contains at most
\(\lfloor d_X/2\rfloor\le d_X-1\) disjoint pairs.

Pair all but \(o(N_H)\) carrier tags.  Summing (2.2) over
\(N_H/2-o(N_H)\) pairs gives

\[
 S-D_m
 \ge
 \left(\frac{N_H}{2}-o(N_H)\right)
 \left(\frac M2-o(M)\right)
 =\frac14MN_H-o(W).
 \tag{2.4}
\]

Since \(MN_H=W-o(W)\),

\[
 D_m\le \frac34W+o(W).
 \tag{2.5}
\]

The exact middle-hole identity is

\[
 h_m=W-D_m=W-S+(S-D_m),
\]

so (2.4) yields

\[
 \boxed{h_m\ge\frac14W-o(W).}
 \tag{2.6}
\]

This is a support obstruction, not a variance estimate.  No choice of the
arrival-order bits can alter it because every counted source is a
block-boundary state common to both alternatives.

## 3. Why the four-template gadget cannot be owner-separated

A four-template rank-isolated gadget uses two carrier source chains
\(\mathcal C,\mathcal C'\) that differ by one adjacent collar swap in
positions \(p,p+1\).

Both positive configurations contain the same two source occurrences and
the same two two-step endpoint occurrences; the switch changes only the
intermediate states.  By (1.3), the source owners differ only for \(p=Q\).
By (1.5), the endpoint owners differ only for \(p=Q-2\).  Therefore

\[
 \boxed{
 \text{every four-template adjacent-chain gadget forces an equal owner
 either at its sources or at its endpoints}.}
 \tag{3.1}
\]

Adding a spectator swap can separate one boundary, but its vertical string
creates an additional surviving rank.  A second pair is required to close
that extra string.  The economical way to do this while separating all
owners is the four-edge cycle below.

### 3.1 Why a three-edge cycle still duplicates an owner

A three-edge cochain cycle would use six path templates.  The triangles of
a Johnson graph have two forms.

1. Three vertices share a common codimension-one base:
   \(K+a,K+b,K+c\).  All three edge intersections are \(K\), so the three
   diamond source owners coincide.
2. The vertices are
   \(K+a+b,K+a+c,K+b+c\).  Their edge intersections
   \(K+a,K+c,K+b\) are distinct, but every two-step diamond endpoint
   contains the same three labels \(a,b,c\).  Hence all three endpoint
   owners coincide.

Thus a coherent saturated-chain triangle can separate sources or endpoints,
but not both.  A four-edge Johnson square is the first cycle whose edge
intersections and edge unions can both be distinct.  This explains the
eight-path size of the successor below.

## 4. A Johnson four-cycle of vertical strings

Let

\[
 \mathcal B=(B_k)
\]

be a saturated base chain, and choose four fixed labels

\[
 a,b,c,d
\]

outside every \(B_k\).  Define four saturated diamond-base chains by

\[
 C^a_k=B_{k-1}+a,\qquad
 C^c_k=B_{k-1}+c,\qquad
 C^d_k=B_{k-1}+d,\qquad
 C^b_k=B_{k-1}+b.
 \tag{4.1}
\]

For a base chain \(\mathcal C\) and two arrivals \(u,v\), write

\[
 V(\mathcal C;u,v)_\ell
 =e_{C_{\ell-1}+u}-e_{C_{\ell-1}+v}.
 \tag{4.2}
\]

Consider the four oriented strings

\[
\begin{aligned}
 V_1&=V(\mathcal C^a;b,c),\\
 V_2&=V(\mathcal C^c;a,d),\\
 V_3&=V(\mathcal C^d;c,b),\\
 V_4&=V(\mathcal C^b;d,a).
\end{aligned}
 \tag{4.3}
\]

### Lemma 4.1 (exact cycle cancellation)

\[
 \boxed{V_1+V_2+V_3+V_4=0}
 \tag{4.4}
\]

at every rank.

#### Proof

At target rank \(\ell\), abbreviate \(B=B_{\ell-2}\).  The four strings
are

\[
\begin{aligned}
 &e_{B+a+b}-e_{B+a+c},\\
 &e_{B+a+c}-e_{B+c+d},\\
 &e_{B+c+d}-e_{B+b+d},\\
 &e_{B+b+d}-e_{B+a+b}.
\end{aligned}
\]

They are the four oriented edges of a Johnson 4-cycle and telescope.
\(\square\)

Unlike the parallel-edge four-template construction, the four source
owners of this cycle are

\[
 B_{m-1}+a,\quad B_{m-1}+c,\quad
 B_{m-1}+d,\quad B_{m-1}+b,
 \tag{4.5}
\]

and are pairwise distinct.

## 5. Perturbing one edge leaves one rank

Fix a desired target rank \(r\).  Change \(\mathcal B\) to a saturated
chain \(\widetilde{\mathcal B}\) which differs from \(\mathcal B\) only at
base rank \(r-2\), by interchanging two adjacent increments \(u,v\).
Thus for a common \((r-3)\)-set \(K\),

\[
 B_{r-2}=K+u,\qquad
 \widetilde B_{r-2}=K+v.
 \tag{5.1}
\]

Replace only the first chain \(\mathcal C^a\) by

\[
 \widetilde C^a_k=\widetilde B_{k-1}+a.
\]

Define

\[
 \Xi_8=
 V(\widetilde{\mathcal C}^a;b,c)
 +V(\mathcal C^c;a,d)
 +V(\mathcal C^d;c,b)
 +V(\mathcal C^b;d,a).
 \tag{5.2}
\]

### Theorem 5.1 (eight-template separated coboundary)

The vector \(\Xi_8\) vanishes at every rank except \(r\).  At rank \(r\),

\[
\boxed{
\begin{aligned}
(\Xi_8)_r={}&
 e_{K+v+a+b}+e_{K+u+a+c}\\
 &-e_{K+v+a+c}-e_{K+u+a+b}.
\end{aligned}}
 \tag{5.3}
\]

Consequently

\[
 \|\Xi_8\|_1=4,\qquad
 \|\Xi_8\|_2^2=4.
 \tag{5.4}
\]

#### Proof

At every rank other than \(r\), the perturbed first string equals \(V_1\),
so Lemma 4.1 gives zero.  At rank \(r\), subtract the old first edge from
the new one and use (5.1):

\[
\begin{aligned}
(\Xi_8)_r
={}&(e_{K+v+a+b}-e_{K+v+a+c})\\
 &-(e_{K+u+a+b}-e_{K+u+a+c}),
\end{aligned}
\]

which is (5.3).  The four masks are distinct. \(\square\)

Each vertical string in (5.2) is the difference of two positive two-step
rotor paths.  Thus \(\Xi_8\) uses eight path templates in four carriers.
Both sides of the switch select one path in every carrier and have the same
word length.

## 6. Complete middle-owner separation

Specialize Theorem 5.1 to

\[
 r=m.
\]

The perturbation is at \(B_{m-2}\).  Since adjacent-swap chains coalesce one
rank later,

\[
 \widetilde B_{m-1}=B_{m-1}.
 \tag{6.1}
\]

Therefore the four source owners remain exactly the four distinct sets in
(4.5).

The two-step endpoint owner of a diamond with base chain
\(\mathcal C\) and arrivals \(s,t\) is

\[
 C_{m-2}+s+t.
 \tag{6.2}
\]

The perturbation in (5.1) occurs one rank above the \(B_{m-3}\) used in
(6.2), so it does not change an endpoint owner.  The four endpoint owners
are

\[
\begin{aligned}
 &B_{m-3}+a+b+c,\\
 &B_{m-3}+a+c+d,\\
 &B_{m-3}+b+c+d,\\
 &B_{m-3}+a+b+d,
\end{aligned}
 \tag{6.3}
\]

which are pairwise distinct.

At the intermediate time, the positive configuration has owners

\[
 \widetilde B_{m-2}+a+b,\quad
 B_{m-2}+a+c,\quad
 B_{m-2}+c+d,\quad
 B_{m-2}+b+d,
 \tag{6.4}
\]

and the negative configuration has owners

\[
 \widetilde B_{m-2}+a+c,\quad
 B_{m-2}+c+d,\quad
 B_{m-2}+b+d,\quad
 B_{m-2}+a+b.
 \tag{6.5}
\]

All four owners in (6.4) are distinct, and all four in (6.5) are distinct.
The fixed labels \(a,b,c,d\) lie outside both base sets, while
\(\widetilde B_{m-2}\ne B_{m-2}\), so no perturbed vertex can equal an
unperturbed vertex with a different displayed pair.

There are no cross-time collisions inside the gadget either.  Put

\[
 K=B_{m-3},\qquad
 B_{m-2}=K+u,\qquad
 \widetilde B_{m-2}=K+v,\qquad
 B_{m-1}=K+u+v.
 \tag{6.6}
\]

Relative to the six distinguished labels
\(\{u,v,a,b,c,d\}\), every source owner contains both \(u,v\) and one of
\(a,b,c,d\); every intermediate owner contains exactly one of \(u,v\) and
two of \(a,b,c,d\); and every endpoint owner contains neither \(u,v\) and
three of \(a,b,c,d\).  These three signatures are disjoint.

Hence:

\[
 \boxed{
 \text{all twelve local owner occurrences in either positive configuration
 are pairwise distinct}.}
 \tag{6.7}
\]

There is no forced local middle duplication analogous to (2.2).

## 7. Legal carrier tags and exact scope

Choose four distinct carriers containing the common visible labels used by
\(\mathcal B\), \(a,b,c,d,u,v\), and the required diamond departures.
Their remaining \(H-Q-O(1)\) labels may be different fillers.  Since
\(Q=o(H)=o(m)\), four such carrier tags exist for all sufficiently large
parameters.

In each carrier, initialize the appropriate source state, choose the two
arrival orders defining its edge in (5.2), and continue both alternatives
identically after their common two-step endpoint.  The positive and
negative configurations each contain one path with every carrier tag.
Initializations and continuations cancel pairwise, so their complete
incidence difference is exactly \(\Xi_8\).

If each physical tail is initially one unresolved block, the all-rank
ordered-partition audit from the four-template note applies to every edge,
and Theorem 5.1 cancels every Boolean rank other than \(r\).  In a long
packed construction the tails refine, so only the truncated hard-band
claim survives automatically.

The eight-template gadget removes the **forced** owner collision of the
paired conveyor.  It does not by itself prove a global near-transversal:
continuations belonging to different four-carrier gadgets must still be
chosen with \(o(W)\) aggregate owner collisions.

The exact new constant-one gate is therefore:

> **Separated eight-template packing \((\mathrm{SEP}_8)\).**  
> Partition all but \(o(N_H)\) carriers into four-tuples.  Pack
> \(\Theta(M)\) Johnson-cycle diamond blocks in every four-tuple, with the
> four source, intermediate, and endpoint owners distinct at every block.
> Choose their continuations and mixed frames so the global complete-braid
> excess collision is \(o(W)\).

Unlike the paired-swap conveyor, \((\mathrm{SEP}_8)\) is not refuted by a
linear forced-duplication ledger.  Its simultaneous chronological packing
remains open.

## 8. Global degree audit

The static global packing problem is resolved in
MATH_ATTACK_EIGHT_TEMPLATE_GLOBAL_PACKING_DEGREES_20260725.md.

For the ordered sign-robust fourteen-owner packet, the exact owner degree is
\(14(m)_3^2\) times a common chain/carrier factor.  A pair at Johnson
distance \(\delta\le3\) has normalized codegree \(O(m^{-2\delta})\), all
farther pairs have codegree zero, and every higher overlap loses the
corresponding power of \(m\).  Carrier and mixed overlaps are still
smaller because every fixed tag removes one large filler choice.

After cloning each carrier into \(\lfloor2M/7\rfloor\) formal block slots,
the owner and slot degrees balance.  An audited fixed-uniformity nibble
packs \((1/14-o(1))W\) robust-owner- and slot-disjoint packets.  Thus eight
templates have enough static capacity, with positive slack over the
\(W/16\) correction scale.

Each sign uses only twelve of the fourteen reserved owners.  At the
\(W/16\) correction scale, the remaining \(W/4+o(W)\) carrier states must
both connect the independently matched blocks and cover exactly the
complementary \(W/4+o(W)\) owners.  The exact open statement is the
productive square-tube completion lemma \((\mathrm{PSTUBE}_8)\).  Its
finite connector part is now proved by the two-update Latin transport in
`MATH_ATTACK_PSTUBE8_LATIN_TRANSPORT_AND_PROTECTED_STRIP_ABSORBER_20260725.md`;
the remaining statement is a committed whole-tube owner near-factor.  The global audit
also proves a sharp scale bound: a one-mark \(k\)-edge Johnson cycle has
\(3k\) actual and \(3k+2\) sign-robust owners per direction.  Hence the
eight-template square \((k=4)\) is the only sign-robust single-direction
cycle compatible with the \(W/16\) scale.  The minimal possible higher
escape is a ten-template five-cycle amortizing at least two marked
rectangles; its required positivity/target pairing is open.
