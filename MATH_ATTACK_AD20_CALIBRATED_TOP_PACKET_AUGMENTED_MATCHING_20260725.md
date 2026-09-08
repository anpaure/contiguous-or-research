# AD20: calibrated full-top packets and the augmented matching gate

Date: 2026-07-25

Pure mathematics only.  No computation, solver, or web search is used.

## 0. Verdict

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q}.
\tag{0.1}
\]

The useful calibration for **full** common-top promotion packets is the
first crossing

\[
 H=\min\{h\ge1:\lambda_h\ge m+h\},\qquad M=m+H.
\tag{0.2}
\]

This is the one-step dual of the previously studied last value satisfying
\(\lambda_h\le m+h\).  It changes the slot discrepancy in the useful
direction.  If

\[
 c={\lambda_H\over M},\qquad S=MN_H,
\tag{0.3}
\]

then

\[
 1\le c<1+{2H-2\over m-H+1},\qquad
 S={W\over c}\le W,
\tag{0.4}
\]

and the exact middle-slot deficit satisfies

\[
 \boxed{D:=W-S< {2H-2\over M-1}W=o(W).}
\tag{0.5}
\]

Moreover

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 N_H=(1+o(1)){W\over m},
\tag{0.6}
\]

so one cut full promotion cycle at each of the \(N_H\) tops has total
reset toll \(2HN_H=o(W)\), and the two Boolean tails beyond the band have
size \(O(W/H)=o(W)\).

The main new result of this note is an exact augmented-hypergraph
formulation in which all scalar and fractional constraints are solved.
For ranks at which the packet density is at most one, physical masks are
capacity-one vertices.  For ranks at which the density exceeds one, every
target is replaced by a number of mandatory clones, and the exact excess
is represented by a common overflow pool.  Every decorated packet has
exactly \(M\) vertices in every controlled rank class.  The resulting
hypergraph has an explicit fractional matching of total mass \(N_H\),
saturating every top, every mandatory clone, and every overflow vertex.

A perfect integral matching in this augmented hypergraph would select one
full cyclic-order packet at every top, with pairwise disjoint middle owners,
and would leave only

\[
 O\!\left({WH^{3/2}\over m}\right)=o(W)
\tag{0.7}
\]

aggregate holes in the entire growing band.  It would therefore give a
literal word of length \(W+o(W)\).

That perfect matching is not proved here.  The exact codegree audit shows
why the standard bounded-uniformity nibble cannot simply be quoted.  Same-
rank middle-owner codegrees are of order \(m^{-2}\), but nested targets in
adjacent ranks have exact conditional codegree \(2/m\) at the centre.
After augmentation, the maximum fractional pair mass is still
\((2+o(1))/m\), while an edge has

\[
 R=1+2HM
\tag{0.8}
\]

vertices.  Thus \(R\) grows and \(R/m\asymp H\to\infty\).  The Boolean-
cover slot graph inside one packet is connected; contracting every
first-order pair contracts the whole packet, whereas a one-successor chain
flow leaves half of each central cover cycle uncontracted.  This is a sharp
obstruction to the proposed sequential ``chain flow, then an
\(m^{-2}\)-codegree nibble'' proof, not an obstruction to the augmented
perfect matching itself.

All asymptotics and incidence identities below are integral and exact
before limits are taken.

## 1. The first-crossing scale

The exact consecutive ratio is

\[
 {\lambda_{h+1}\over\lambda_h}
 ={m+h+1\over m-h}.
\tag{1.1}
\]

### Theorem 1.1 (exact first-crossing window)

For all sufficiently large \(m\), the integer \(H\) in (0.2) satisfies
\(1<H<m\), and, with \(M,c,S,D\) as in (0.3)--(0.5),

\[
 \boxed{
 1\le c<{M-1\over m-H+1}
       =1+{2H-2\over m-H+1}.}
\tag{1.2}
\]

Consequently

\[
 \boxed{
 0\le {D\over W}=1-{1\over c}
 <{2H-2\over M-1}.}
\tag{1.3}
\]

#### Proof

Minimality gives

\[
 \lambda_{H-1}<m+H-1=M-1.
\]

By (1.1),

\[
 \lambda_H
 =\lambda_{H-1}{m+H\over m-H+1}
 <(M-1){M\over m-H+1}.
\]

The defining inequality \(\lambda_H\ge M\) and division by \(M\)
prove (1.2).  Since \(S=MN_H=MW/\lambda_H=W/c\),

\[
 {D\over W}=1-{1\over c}
 <1-{m-H+1\over M-1}
 ={2H-2\over M-1},
\]

which is (1.3).  The endpoint assertions follow from Theorem 1.2 below.
\(\square\)

### Theorem 1.2 (asymptotic location)

The first crossing obeys

\[
 \boxed{H=(1+o(1))\sqrt{m\log m}.}
\tag{1.4}
\]

In particular,

\[
 c=1+O(H/m)=1+o(1),\qquad
 N_H=(1+o(1)){W\over m},
\tag{1.5}
\]

and

\[
 HN_H=o(W).
\tag{1.6}
\]

#### Proof

Uniformly for \(h=o(m^{2/3})\), Taylor expansion of the exact product

\[
 \lambda_h=\prod_{i=0}^{h-1}{m+i+1\over m-i}
\]

gives

\[
 \log\lambda_h={h^2\over m}
 +O\!\left({h\over m}+{h^3\over m^2}\right).
\tag{1.7}
\]

Indeed the linear terms sum to
\(\sum_{i<h}(2i+1)/m=h^2/m\), and the sum of the uniform quadratic
remainders is \(O(h^3/m^2)\).

Fix \(\varepsilon>0\), and take the nearest integers to

\[
 h_-=(1-\varepsilon)\sqrt{m\log m},\qquad
 h_+=(1+\varepsilon)\sqrt{m\log m}.
\]

Equation (1.7) yields

\[
 \lambda_{h_-}=m^{(1-\varepsilon)^2+o(1)}<m+h_-,
\]

and

\[
 \lambda_{h_+}=m^{(1+\varepsilon)^2+o(1)}>m+h_+.
\]

Thus \(h_-<H\le h_+\) eventually.  This proves (1.4).  Equations
(1.2), (0.3), and \(M\sim m\) then give (1.5)--(1.6).
\(\square\)

### Proposition 1.3 (outer-tail ledger)

At the first-crossing depth,

\[
 \boxed{2\sum_{q=H+1}^{m}N_q=O(W/H)=o(W).}
\tag{1.8}
\]

More precisely,

\[
 2\sum_{q=H+1}^{m}N_q
 \le 2N_H{m-H\over2H+1}
 \le {2W\over2H+1}.
\tag{1.9}
\]

#### Proof

For \(q\ge H\),

\[
 {N_{q+1}\over N_q}={m-q\over m+q+1}
 \le {m-H\over M+1}=:\rho<1.
\]

Geometric summation gives the first inequality in (1.9).  Since
\(\lambda_H\ge M>m-H\), one has
\(N_H=W/\lambda_H<W/(m-H)\), proving the second inequality.
\(\square\)

## 2. Full cyclic packets and exact degrees

Let \(V=[2m]\).  For a top

\[
 U\in\binom VM,\qquad M=m+H,
\]

and a directed cyclic order

\[
 \pi=(u_0,u_1,\ldots,u_{M-1})
\]

modulo cyclic rotation, write

\[
 I_\pi(t,r)=\{u_t,u_{t+1},\ldots,u_{t+r-1}\}.
\tag{2.1}
\]

The full common-top promotion cycle has middle owners
\(I_\pi(t,m)\), \(t\in\mathbb Z_M\).  At every controlled rank

\[
 m-H\le r<M,
\tag{2.2}
\]

its flags are exactly the \(M\) cyclic intervals

\[
 \mathcal I_r(U,\pi)=
 \{I_\pi(t,r):t\in\mathbb Z_M\}.
\tag{2.3}
\]

At rank \(M\), its common upper flag is \(U\).  Cutting one arc produces
one literal useful-prefix path with \(M\) owner letters and exact reset
toll \(2H\).

Let \(\mathscr P\) be the indexed family of all pairs \((U,\pi)\).
There are

\[
 L=(M-1)!
\tag{2.4}
\]

directed cyclic orders at each top.

### Theorem 2.1 (exact point degrees)

Every top has packet degree

\[
 d_{\rm top}=L.
\tag{2.5}
\]

For \(0<r<M\), every fixed target
\(T\in\binom Vr\) has packet degree

\[
 \boxed{
 d_r=\binom{2m-r}{M-r}r!(M-r)!.}
\tag{2.6}
\]

In particular a middle owner has degree

\[
 d_m=\binom mH m!H!.
\tag{2.7}
\]

If every packet receives weight \(1/L\), then every top has load one and
every rank-\(r\) target has load

\[
 \boxed{
 \mu_r={S\over\binom{2m}{r}}.}
\tag{2.8}
\]

For \(r=m\pm q\), this is

\[
 \mu_r={\lambda_q\over c}.
\tag{2.9}
\]

#### Proof

For (2.6), first choose a top containing \(T\), in
\(\binom{2m-r}{M-r}\) ways.  In a cyclic order of that top, contract
the prescribed interval \(T\) to one block.  There are \((M-r)!\)
cyclic orders of that block and the remaining \(M-r\) points, and \(r!\)
internal orders of the block.  This proves (2.6).  Equation (2.7) is its
middle specialization.

The total packet weight is \(N_H\), and every packet supplies \(M\)
distinct targets in every rank (2.2).  Transitivity on that rank gives
load \(MN_H/\binom{2m}{r}=\mu_r\), proving (2.8)--(2.9).
\(\square\)

## 3. Exact pair incidences

The following formulas audit every factor of two needed later.  Put

\[
 A=2m-r,\qquad s=M-r.
\tag{3.1}
\]

For the ranks in (2.2), \(s\le2H\), so eventually \(2s<M\).

### Theorem 3.1 (same-rank interval codegree)

Let \(T,T'\in\binom Vr\) be distinct and put

\[
 d=|T\setminus T'|=|T'\setminus T|.
\]

They occur together in a packet only if \(d\le s\).  Conditional on a
uniform indexed packet containing \(T\), the exact probability of also
containing \(T'\) is

\[
 \boxed{
 p_r(d)=
 \begin{cases}
 \displaystyle {2\over\binom rd\binom Ad},&1\le d<s,\\[3mm]
 \displaystyle {r-s+1\over\binom rs\binom As},&d=s,\\[3mm]
 0,&d>s.
 \end{cases}}
\tag{3.2}
\]

For middle owners this becomes

\[
 p_m(d)={2\over\binom md^2}\quad(1\le d<H),
\tag{3.3}
\]

and

\[
 p_m(H)={m-H+1\over\binom mH^2}.
\tag{3.4}
\]

In particular, the largest non-boundary middle-owner value is exactly
\(2/m^2\).

#### Proof

A common top must contain \(T\cup T'\), so there are

\[
 \binom{A-d}{s-d}
\tag{3.5}
\]

choices when \(d\le s\).  Inside such a top, take complements.  The two
complements are prescribed cyclic \(s\)-intervals at distance \(d\).

If \(d<s\), their left arm, overlap, and right arm have sizes
\(d,s-d,d\).  There are two orientations.  Treating their union as one
block gives exactly

\[
 2(r-d)!(d!)^2(s-d)!
\tag{3.6}
\]

cyclic orders.  Multiplying (3.5) and (3.6), and dividing by the point
degree

\[
 \binom As r!s!,
\]

gives

\[
 {2(A-d)!(r-d)!(d!)^2\over A!r!}
 ={2\over\binom rd\binom Ad}.
\]

If \(d=s\), the two complementary \(s\)-blocks are disjoint.  Treating
them as two blocks gives

\[
 (r-s+1)!(s!)^2
\]

cyclic orders and a unique top, which yields the boundary line of (3.2).
Equations (3.3)--(3.4) follow by putting \(r=A=m,s=H\).
\(\square\)

The boundary term matters near the top.  For \(r=M-1\), one has \(s=1\)
and \(p_r(1)=1/(m-H+1)\), not \(O(m^{-2})\).  The clone augmentation in
Section 4 divides this high-load correlation among \(m-H+1\) mandatory
copies.

### Theorem 3.2 (nested cross-rank codegree)

Let \(T\in\binom Vr\), let \(B\supset T\) have size \(r+d<M\), and
put \(1\le d<s=M-r\).  Conditional on a uniform indexed packet
containing \(T\),

\[
 \boxed{
 \Pr(B\hbox{ also occurs})
 ={d+1\over\binom{2m-r}{d}}.}
\tag{3.7}
\]

In particular every prescribed Boolean cover \(T\subset B\),
\(|B|=|T|+1\), has conditional probability

\[
 \boxed{{2\over2m-r}.}
\tag{3.8}
\]

At the central cover \(r=m\), this is exactly \(2/m\).

#### Proof

There are

\[
 \binom{2m-r-d}{s-d}
\]

common tops.  In a cyclic order, the interval \(B\) contains the interval
\(T\).  The \(d\) points of \(B\setminus T\) can be split between the
two ends of \(T\) in \(d+1\) ways.  After choosing the split, all internal
orders together contribute \(d!r!\), and the \(s-d\) points outside
\(B\) contribute \((s-d)!\).  Thus the number of cyclic orders at one
common top is

\[
 (d+1)!r!(s-d)!.
\]

Division by \(\binom{2m-r}{s}r!s!\) simplifies to (3.7).
\(\square\)

Theorems 3.1 and 3.2 separate the two scales exactly: same-rank central
motion is second order, but an adjacent-rank cover is first order.

## 4. The augmented packet hypergraph

Let

\[
 \mathcal J=\{m-H,m-H+1,\ldots,M-1\}.
\tag{4.1}
\]

This set has \(2H\) ranks.  For \(r\in\mathcal J\), put

\[
 N(r)=\binom{2m}{r},\qquad \mu_r={S\over N(r)}.
\tag{4.2}
\]

Split

\[
 \mathcal J_0=\{r:\mu_r\le1\},\qquad
 \mathcal J_+=\{r:\mu_r>1\}.
\tag{4.3}
\]

For \(r\in\mathcal J_0\), take the physical rank-\(r\) masks themselves
as capacity-one resource vertices.

For \(r\in\mathcal J_+\), define

\[
 k_r=\lfloor\mu_r\rfloor\ge1,
 \qquad e_r=S-k_rN(r),
 \qquad 0\le e_r<N(r).
\tag{4.4}
\]

Create

\[
 \mathcal C_r=\{(T,j):T\in\binom Vr,\ 1\le j\le k_r\}
\tag{4.5}
\]

of **mandatory clones**, and a disjoint overflow set \(\mathcal D_r\) of
size \(e_r\).  The total size of this resource class is exactly

\[
 |\mathcal C_r|+|\mathcal D_r|
 =k_rN(r)+e_r=S.
\tag{4.6}
\]

For a base packet \(P=(U,\pi)\), a rank-\(r\) decoration, for
\(r\in\mathcal J_+\), does the following.  It chooses an integer

\[
 d_r\in
 \left\{\left\lfloor{e_r\over N_H}\right\rfloor,
       \left\lceil{e_r\over N_H}\right\rceil\right\},
\tag{4.7}
\]

chooses \(d_r\) of the \(M\) physical intervals in
\(\mathcal I_r(P)\) as overflow occurrences, assigns them to
\(d_r\) distinct vertices of \(\mathcal D_r\), and assigns every
remaining interval \(T\) one clone \((T,j)\).  The family contains all
such choices.  When \(e_r=0\), only \(d_r=0\) is used.

For all sufficiently large \(m\), the values in (4.7) lie between zero
and \(M\), and whenever positive do not exceed \(e_r\); hence the
decoration family is nonempty.  Indeed

\[
 {e_r\over N_H}
 =M\left(1-{k_r\over\mu_r}\right)\in[0,M),
\tag{4.8}
\]

and \(N_H\ge2\) eventually.

### Definition 4.1 (calibrated augmented packet hypergraph)

The vertex classes are:

1. the \(N_H\) top vertices \(U\in\binom VM\);
2. the physical rank-\(r\) masks for every \(r\in\mathcal J_0\);
3. \(\mathcal C_r\sqcup\mathcal D_r\) for every
   \(r\in\mathcal J_+\).

An edge is one base packet together with one decoration at every high-load
rank.  It contains its top, exactly \(M\) resource vertices at every one
of the \(2H\) ranks, and hence has exact size

\[
 \boxed{R=1+2HM.}
\tag{4.9}
\]

Denote this finite integral hypergraph by \(\mathcal A_{m,H}\).

The decoration records no fractional physical packet.  Every edge is one
literal full promotion cycle.  Clone and overflow labels are bookkeeping
resources used only to enforce balanced integral incidence.

## 5. Exact fractional matching of the augmentation

### Theorem 5.1 (symmetric fractional saturation)

The hypergraph \(\mathcal A_{m,H}\) has a fractional matching
\(z\) of total mass exactly \(N_H\) such that

1. every top vertex has load exactly one;
2. every physical vertex in a low-load rank has load \(\mu_r\le1\);
3. every mandatory clone has load exactly one; and
4. every overflow vertex has load exactly one.

#### Proof

Give every base packet weight \(1/L\).  This gives the loads in
Theorem 2.1.  It remains to distribute each base weight over decorations.

Fix \(r\in\mathcal J_+\).  Randomize \(d_r\) between the two integers in
(4.7) so that

\[
 \mathbb E d_r={e_r\over N_H}.
\tag{5.1}
\]

Conditional on \(d_r\), choose the overflow occurrences uniformly among
the \(M\) interval occurrences, choose a uniform \(d_r\)-subset of
\(\mathcal D_r\), and choose independently and uniformly one of the
\(k_r\) clone labels for every nonoverflow occurrence.  Perform these
decorations independently at the different ranks and split the base
weight according to the resulting finite distribution.

A fixed physical target \(T\) has base occurrence load \(\mu_r\).  The
probability that its occurrence is not sent to overflow is

\[
 1-{\mathbb E d_r\over M}
 =1-{e_r\over MN_H}
 =1-{e_r\over S}
 ={k_r\over\mu_r}.
\tag{5.2}
\]

It is then assigned any prescribed clone label with probability
\(1/k_r\).  Hence a fixed clone \((T,j)\) has load

\[
 \mu_r{k_r\over\mu_r}{1\over k_r}=1.
\]

The total base packet mass is \(N_H\).  A fixed overflow vertex is chosen
inside a random decorated packet with mean probability

\[
 {\mathbb E d_r\over e_r}={1\over N_H}
\]

when \(e_r>0\), and therefore also has load one.  Tops and low-load
vertices have the asserted loads directly from Theorem 2.1.  Since every
top has load one, the total fractional edge mass is \(N_H\).
\(\square\)

Thus there is no divisibility, top-capacity, owner-capacity, rank-capacity,
or fractional Hall obstruction in the calibrated augmentation.

## 6. What an integral matching gives

### Theorem 6.1 (perfect augmented matching implies coefficient one)

Assume that \(\mathcal A_{m,H}\) has a matching of size \(N_H\).  Then
there is a literal nonzero contiguous-OR word on \([2m]\) of length

\[
 W+o(W)
\tag{6.1}
\]

covering every nonempty mask.

#### Proof

Every augmented edge contains one top, and there are exactly \(N_H\)
tops.  A matching of size \(N_H\) therefore uses one packet at every top.
At every high-load rank, its selected edges use

\[
 MN_H=S
\]

pairwise distinct resource vertices.  By (4.6), this is the entire clone-
plus-overflow class.  In particular, every mandatory clone is covered.
Consequently every physical target at that rank occurs in at least
\(k_r\ge1\) selected packets.

At a low-load rank, the packet intervals themselves are capacity-one
vertices.  Hence the selected packets hit exactly \(S\) distinct masks and
leave exactly

\[
 N(r)-S
\tag{6.2}
\]

holes.  This includes the middle rank: since \(\mu_m=1/c\le1\), the
packets have \(S\) pairwise distinct middle owners and leave exactly
\(D=W-S\) owners.

It remains to sum (6.2).  Let

\[
 Q=\max\{q\le H:\lambda_q\le c\}.
\tag{6.3}
\]

Every low-load rank has distance at most \(Q\) from the middle.  The exact
lower bound

\[
 \log\lambda_q
 =\sum_{i<q}\log\left(1+{2i+1\over m-i}\right)
 \ge\sum_{i<q}{2i+1\over m+i+1}
 \ge {q^2\over m+q}
\tag{6.4}
\]

and (1.2) give, eventually,

\[
 {q^2\over m+q}\le\log c\le {3H\over m}.
\]

Since \(q\le H=o(m)\), this implies

\[
 Q\le\sqrt{6H}.
\tag{6.5}
\]

For every low-load rank,

\[
 0\le N(r)-S\le W-S=D.
\]

There are at most \(2Q+1\) such ranks.  The aggregate controlled-band
hole count is therefore at most

\[
 \boxed{
 B_{\rm thin}:=(2Q+1)D
 <(2\sqrt{6H}+1){2H-2\over M-1}W
 =O\!\left({WH^{3/2}\over m}\right)=o(W).}
\tag{6.6}
\]

Cut every selected promotion cycle once and concatenate the resulting
useful-prefix paths.  Their exact principal length plus resets is

\[
 S+2HN_H\le W+o(W)
\tag{6.7}
\]

by Theorem 1.2.  Append each of the at most \(B_{\rm thin}\) controlled-
band holes as one literal letter, and append the two outer tails.  Equations
(6.6) and (1.8) add only \(o(W)\) letters.  Every appended mask is nonzero;
the empty mask is not required.  This proves (6.1).
\(\square\)

This theorem is an exact coefficient-one reduction.  It requires no SCD,
no wreath synchronization, and no fractional object inside the final
word.

### Proposition 6.2 (quantitative near-matching boundary)

Let \(\mathcal M\) be any matching in \(\mathcal A_{m,H}\) with
\(t\) edges, and let \(E_+\) be the total number of uncovered mandatory
clone vertices over all high-load ranks.  The corresponding physical
packets have aggregate controlled-band holes at most

\[
 \boxed{
 B_{\rm thin}+(2Q+1)M(N_H-t)+E_+ +(N_H-t).}
\tag{6.8}
\]

The final term records missing top masks and may be omitted if tops are
completed separately.

#### Proof

At a low-load rank, matching disjointness gives exactly \(tM\) distinct
hits, so

\[
 N(r)-tM=(N(r)-S)+M(N_H-t).
\]

Summing over at most \(2Q+1\) low ranks gives the first two terms of
(6.8).  A high-load target which is physically absent has all its
mandatory clones uncovered, so the number of high-load holes is at most
\(E_+\).  Finally, each omitted top is a missing depth-\(H\) upper target.
\(\square\)

Thus a generic matching covering merely \((1-o(1))N_H\) tops is not, by
itself, enough.  One needs at least

\[
 M Q(N_H-t)=o(W),\qquad E_+=o(W),
\tag{6.9}
\]

or a separate completion proving the same aggregate ledger.

## 7. Decisive codegree and contraction audit

For the fractional matching in Theorem 5.1, write

\[
 \Omega(v,w)=\sum_{E\ni v,w}z_E.
\tag{7.1}
\]

This is the fractional pair mass, not an unnormalized count of indexed
copies.

### Proposition 7.1 (an unavoidable first-order pair)

Fix a middle owner \(X\) and a prescribed one-element extension
\(Y=X\cup\{y\}\).  If rank \(m+1\) is low-load, then

\[
 \boxed{\Omega(X,Y)={2\over cm}.}
\tag{7.2}
\]

If rank \(m+1\) is high-load, then for every mandatory clone \((Y,j)\),

\[
 \boxed{\Omega(X,(Y,j))={2\over m+1}.}
\tag{7.3}
\]

Consequently

\[
 \max_{v\ne w}\Omega(v,w)\ge {2+o(1)\over m}.
\tag{7.4}
\]

#### Proof

The physical middle-owner load is \(\mu_m=1/c\).  By (3.8), conditional
on its occurrence the prescribed extension occurs with probability
\(2/m\).  This proves (7.2).

At a high-load rank, the proof of Theorem 5.1 shows that a fixed physical
occurrence is assigned to a prescribed mandatory clone with probability
\(1/\mu_{m+1}\).  Since

\[
 \mu_{m+1}={\lambda_1\over c}={m+1\over cm},
\]

division of (7.2) by \(\mu_{m+1}\) gives (7.3).
\(\square\)

By contrast, for two middle owners at Johnson distance one, (3.3) gives

\[
 \Omega(X,X')={2\over cm^2}.
\tag{7.5}
\]

Thus the first-order obstruction is exactly cross-rank Boolean-cover
incidence, not same-rank packet overlap.

### Proposition 7.2 (the cover-slot graph is connected)

Fix one base packet.  Between any two consecutive proper ranks \(r,r+1\)
in its interval band, put

\[
 P_t=I_\pi(t,r),\qquad Q_t=I_\pi(t,r+1).
\]

The Boolean-cover incidences are exactly

\[
 P_t\subset Q_t,qquad P_t\subset Q_{t-1}
 \quad(t\in\mathbb Z_M).
\tag{7.6}
\]

They form one alternating cycle of length \(2M\).  Consequently:

1. a one-successor chain matching internalizes at most \(M\) of its
   \(2M\) cover incidences;
2. contracting every cover incidence between these two ranks identifies
   all \(2M\) slots; and
3. the cover-slot graph on every rank and start of the complete packet is
   connected.

#### Proof

An \(r\)-interval has exactly its left and right one-point cyclic
extensions among the \((r+1)\)-intervals, giving (7.6).  Alternating the
two types walks through all starts modulo \(M\), so the graph is a
\(2M\)-cycle.  Its matching number is \(M\), and its edge contraction is
connected.  Consecutive rank pairs share their rank-slot vertices, so the
union over the whole band remains connected.
\(\square\)

### Consequence for generic nibble arguments

The augmented edge rank is \(R=1+2HM\), while Proposition 7.1 gives

\[
 R\max_{v\ne w}\Omega(v,w)\ge(4+o(1))H\longrightarrow\infty.
\tag{7.7}
\]

Classical almost-perfect-matching statements whose quantifiers fix the
uniformity before sending the normalized codegree to zero do not apply to
this growing-rank sequence.  Nor can one first contract a single
successor at every target and then invoke only the \(m^{-2}\) same-rank
estimate: Proposition 7.2 leaves half of every cover cycle, while
contracting all cover edges contracts the entire physical packet.

This is a rigorous obstruction to those two proof templates.  It is not a
counterexample to a row-aware matching theorem exploiting the interval
geometry, and it is not a counterexample to the existence of the perfect
matching in Theorem 6.1.

## 8. Exact remaining theorem

The remaining statement in this lane is now the following finite integral
problem.

> **Calibrated augmented packet matching \((\mathrm{CAPM})\).**  For the
> first-crossing depth (0.2), the augmented hypergraph
> \(\mathcal A_{m,H}\) has a matching of size \(N_H\).

By Theorem 6.1, \((\mathrm{CAPM})\) implies

\[
 \nu(2m)\le(1+o(1))\binom{2m}{m}.
\]

A quantitatively weaker sufficient form is a matching satisfying (6.9).
This weaker statement must control total uncovered mandatory-clone mass,
not merely the fraction of uncovered tops.

### Proved in this note

1. The exact first-crossing window (1.2) and deficit (1.3).
2. \(H\sim\sqrt{m\log m}\), \(N_H\sim W/m\), reset toll \(o(W)\), and
   outer tails \(o(W)\).
3. The exact full-packet point degrees (2.5)--(2.7).
4. The exact same-rank and nested cross-rank codegrees (3.2) and (3.7),
   including every factor of two.
5. The integral augmented hypergraph with exactly matched scalar class
   sizes.
6. Its exact symmetric fractional matching.
7. A perfect augmented matching implies a literal \(W+o(W)\) word.
8. The exact near-matching leave ledger (6.8).
9. The first-order adjacent-rank pair mass and connected cover-slot
   obstruction.

### Not proved

1. \((\mathrm{CAPM})\), or the weaker quantitative matching condition
   (6.9).
2. Any unbounded-uniformity nibble theorem strong enough to infer it from
   the displayed degrees and codegrees.
3. An absorption construction preserving all clone classes and the cyclic
   chronology simultaneously.

The calibrated route therefore survives every scalar, literal, and
fractional audit.  Its precise boundary is no longer an informal
``round one order per top'' request: it is the explicit perfect-matching
problem \((\mathrm{CAPM})\), with a proved \(o(W)\) hole ledger and a
proved first-order cover-correlation barrier to generic sequential
rounding.
