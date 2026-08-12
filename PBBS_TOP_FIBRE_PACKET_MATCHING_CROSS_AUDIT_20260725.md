# PBBS versus the critical growing top-fibre packet matching

Date: 2026-07-25

Pure mathematics only. No computation, search, solver, or probabilistic
rounding theorem is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad N_h=\binom{2m}{m-h},\qquad
 \lambda_h=\frac{W}{N_h}.
\]

Choose the first depth (H) for which

\[
 \lambda_H\ge m+H,
 \qquad M:=m+H.
 \tag{0.1}
\]

Then

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 MN_H=W-O(WH/m)=W-o(W),\qquad HN_H=o(W).
 \tag{0.2}
\]

Thus one full length-(M) common-top promotion packet for every
rank-((m+H)) top has exactly the right total size, from below, and one
reset per top is negligible.

This note proves four further facts.

1. The packet-selection hypergraph has an exact symmetric fractional
   matching saturating every top and using every middle owner to load at
   most one.
2. Its exact largest owner--owner relative codegree is
   (2/m^2). Thus the crude maximum-codegree growing-uniformity parameter
   is critical:
   \[
      (M+1)^2\frac{\Delta_2}{D}=2+o(1),
   \]
   not (o(1)). However this maximum is attained only by the (M)
   adjacent owner pairs in one packet. Summed over the exact distance
   spectrum of one packet, the normalized double-overlap mass is only
   \((2+o(1))/m\). Hence the owner-only near-matching problem is more
   favorable than the maximum-codegree audit suggests.
3. For any integral one-packet-per-top selection there is an exact
   balanced-collision identity for every lower and upper interval shadow.
   The sum of all unavoidable capacity holes is already (o(W)). Hence
   the sole missing assertion is an (o(W)) bound on the excess collision
   mass above that arithmetic floor, simultaneously through depth (H).
4. A height-((H-1)) simple PBBS return does canonically give an
   (H)-state segment of one of these top packets. It gives only an
   (H/M=o(1)) fraction of a packet. Producing all packets this way would
   require order (W/H) compatible sectors and, crucially, fusion of
   (M/H) sectors per common top. Existing PBBS quotient packing theorems
   control edge-disjoint returns inside one canonical trajectory; they do
   not supply this cross-top fusion or the cross-packet shadow discrepancy.

The surviving theorem is therefore a critical top-indexed cyclic-packet
matching/discrepancy theorem. PBBS gives an exact local subpacket model,
but its present quotient and corner bounds do not prove the required
near-perfect global selection.

## 1. Exact threshold arithmetic

The consecutive ratio is

\[
 \frac{\lambda_h}{\lambda_{h-1}}
 =\frac{m+h}{m-h+1}.
 \tag{1.1}
\]

Minimality in (0.1) gives

\[
 \lambda_{H-1}<m+H-1=M-1.
\]

Consequently

\[
 1\le \frac{\lambda_H}{M}
 <\frac{M-1}{m-H+1}
 =1+\frac{2H-2}{m-H+1}.
 \tag{1.2}
\]

The standard central expansion

\[
 \log\lambda_h
 =\frac{h^2}{m}
 +O\!\left(\frac hm+\frac{h^3}{m^2}\right)
 \tag{1.3}
\]

then gives (H=(1+o(1))\sqrt{m\log m}). Write

\[
 \frac{\lambda_H}{M}=1+\eta,
 \qquad 0\le\eta=O(H/m).
 \tag{1.4}
\]

The total number of owner positions in one full packet per top is

\[
 T:=MN_H=W\frac{M}{\lambda_H}=\frac{W}{1+\eta}.
 \tag{1.5}
\]

Thus

\[
 0\le W-T=O(WH/m)=o(W),
 \tag{1.6}
\]

and

\[
 HN_H=\frac{HW}{\lambda_H}\le\frac{HW}{M}=o(W).
 \tag{1.7}
\]

This first-crossing convention has one convenience over the last depth
with (lambda_h\le m+h): all full packets fit under the middle-owner
capacity, so no slot deletion is required.

## 2. The top-packet hypergraph

Let

\[
 \mathcal U=\binom{[2m]}{M},\qquad
 \mathcal X=\binom{[2m]}m.
\]

For (U\in\mathcal U) and a directed cyclic order (pi) of (U),
modulo rotation, let

\[
 \mathcal P(U,\pi)
 =\{U\setminus I_\pi(t,H):t\in\mathbb Z_M\}.
 \tag{2.1}
\]

This is exactly the set of (M) middle owners on the common-top
promotion cycle. Define a multihypergraph (mathscr K_H) on

\[
 \mathcal U\mathbin{\dot\cup}\mathcal X
\]

with edge

\[
 e(U,\pi)=\{U\}\cup\mathcal P(U,\pi).
 \tag{2.2}
\]

Every edge has size (M+1) and contains exactly one top vertex.

### Theorem 2.1 (degree census and exact fractional matching)

Every top has degree

\[
 D_U=(M-1)!,
 \tag{2.3}
\]

and every middle owner has degree

\[
 D_X=\binom mH H!m!=\frac{m!^2}{(m-H)!}.
 \tag{2.4}
\]

Moreover

\[
 \frac{D_X}{D_U}=\frac{M}{\lambda_H}le1
 \tag{2.5}
\]

and the ratio is (1-O(H/m)). Assigning weight (1/D_U) to every
packet edge is therefore a fractional matching which gives every top load
exactly one and every owner load exactly (M/\lambda_H\le1).

#### Proof

There are ((M-1)!) directed cyclic orders modulo rotation. For a fixed
owner (X), first choose its containing top by choosing

\[
 Q=U\setminus X\in\binom{[2m]\setminus X}{H},
\]

which gives (inom mH) choices. In a fixed top, the number of cyclic
orders in which this prescribed (H)-set is an interval is (H!m!):
collapse it to one cyclic block, order its (H) internal labels, and
cyclically order the block with the (m) remaining labels. This proves
(2.3)--(2.4).

Finally, with

\[
 a=\binom mH,\qquad b=\binom MH,
\]

one has (lambda_H=b/a), while

\[
 \frac{H!m!}{(M-1)!}=\frac Mb.
\]

Thus (D_X/D_U=aM/b=M/\lambda_H), proving (2.5) and the fractional
claim. \(square\)

So there is no capacity or fractional obstruction to selecting one packet
per top with disjoint owners. The missing issue is integral rounding at
growing edge size.

## 3. Exact pair codegrees and criticality

Let (X,Y\in\mathcal X) be distinct and put

\[
 d=|X\setminus Y|=|Y\setminus X|.
\]

### Theorem 3.1 (owner-pair codegree)

If (1\le d<H), then

\[
 \boxed{
 \frac{\deg(X,Y)}{D_X}=\frac{2}{\binom md^2}.}
 \tag{3.1}
\]

If (d>H), the codegree is zero. At (d=H),

\[
 \boxed{
 \frac{\deg(X,Y)}{D_X}
 =\frac{m-H+1}{\binom mH^2}.}
 \tag{3.2}
\]

In particular, at the growing depth (H),

\[
 \max_{X\ne Y}\deg(X,Y)
 =\frac{2+o(1)}{m^2}D_X,
 \tag{3.3}
\]

attained at Johnson distance one.

#### Proof

A common top exists only when (d\le H). For (d\le H), the number of
common tops is

\[
 \binom{m-d}{H-d}.
 \tag{3.4}
\]

Fix one such top and put

\[
 Q=U\setminus X,\qquad R=U\setminus Y.
\]

When (d<H), the two (H)-sets have intersection of size (H-d).
For both to be cyclic intervals, their three successive pieces

\[
 Q\setminus R,\quad Q\cap R,\quad R\setminus Q
\]

must occur in this order or the reverse order, and their complementary
((m-d))-set is the remaining cyclic block. Hence the number of orders is

\[
 2(d!)^2(H-d)!(m-d)!.
 \tag{3.5}
\]

Multiplying (3.4) and (3.5), and dividing by

\[
 D_X=\frac{m!^2}{(m-H)!},
\]

gives (3.1).

When (d=H), the two prescribed intervals are disjoint. Collapsing each
to a block gives

\[
 H!^2(m-H+1)!
\]

orders, which yields (3.2). For (H\to\infty), (3.2), all values
(d\ge2), and the top--owner codegrees are smaller than the value at
(d=1). This proves (3.3). \(square\)

The packet size is (M+1=(1+o(1))m). Therefore

\[
 \boxed{
 (M+1)^2\frac{\Delta_2}{D_X}=2+o(1).}
 \tag{3.6}
\]

This is the same critical phenomenon seen in the PBBS residence packing:
the maximum pair codegree vanishes exactly at the inverse-square scale of
the atom size. The following exact packet-specific calculation shows that
this crude maximum is not the full story.

### Theorem 3.2 (the realized pair spectrum is subcritical)

For one packet (P=\mathcal P(U,\pi)),

\[
 \boxed{
 \frac1{D_X}
 \sum_{\{X,Y\}\subseteq P}\deg(X,Y)
 =\frac{2+o(1)}m.}
 \tag{3.7}
\]

The same conclusion holds after adding all top--owner pairs from the
hyperedge (e(U,\pi)).

#### Proof

Write the packet owners as complements of the (M) cyclic (H)-windows.
Two windows at shorter cyclic separation (d<H) have Johnson distance
(d), and there are exactly (M) unordered pairs at every such distance.
All remaining owner pairs have Johnson distance (H). Therefore Theorem
3.1 gives

\[
 \begin{aligned}
 \frac1{D_X}\sum_{\{X,Y\}\subseteq P}\deg(X,Y)
 ={}&2M\sum_{d=1}^{H-1}\binom md^{-2}\\
 &+\left[\binom M2-M(H-1)\right]
   \frac{m-H+1}{\binom mH^2}.
 \end{aligned}
 \tag{3.8}
\]

The (d=1) term is

\[
 \frac{2M}{m^2}=\frac{2+o(1)}m.
\]

The sum over (d\ge2) is (O(M/m^4)=o(1/m)), and the final term is
superpolynomially smaller at
(H\sim\sqrt{m\log m}). This proves (3.7).

For a fixed top and owner lying in it, the codegree is (H!m!), whose
ratio to (D_X) is (1/\binom mH). Summing this over the (M) owners of
the packet is still (o(1/m)). \(\square\)

Thus an edge's multiple-intersection correction is (o(D_X)), even
though the worst-pair bound multiplied by (M^2) is constant. This is
genuine evidence that a bespoke semi-random argument might solve the
owner-only near-matching. It is not yet such an argument, and it says
nothing by itself about the (2H) simultaneous interval-shadow rows.

### Theorem 3.3 (same-row interval spectrum)

Fix one lower or upper row of rank (r), and put

\[
 h=M-r.
\]

Thus (r=m-q,h=H+q) on the lower side and
(r=m+q,h=H-q) on the upper side. Assume (0<h<M/2). A fixed rank-(r)
target has packet degree

\[
 \boxed{
 D_r=\frac{(2m-r)!r!}{(m-H)!}=\lambda_qD_X.}
 \tag{3.9}
\]

For two rank-(r) targets at Johnson distance (d<h),

\[
 \boxed{
 \frac{\deg(S,T)}{D_r}
 =\frac{2}{\binom rd\binom{2m-r}d}.}
 \tag{3.10}
\]

At (d=h), the ratio is

\[
 \boxed{
 \frac{r-h+1}{\binom rh\binom{2m-r}h}.}
 \tag{3.11}
\]

Consequently, uniformly on every shallow range (q=o(H)), the sum of
same-row pair codegrees realized inside one packet is

\[
 \boxed{
 \frac1{D_r}
 \sum_{\{S,T\}\text{ in one packet row}}\deg(S,T)
 =\frac{2+o(1)}m.}
 \tag{3.12}
\]

#### Proof

A top containing a fixed target (S) is obtained by adjoining (h)
coordinates from its complement. Once the top is fixed, (S) is an
interval exactly when its complementary (h)-set is an interval. Hence

\[
 \deg(S)=\binom{2m-r}{h}h!r!
 =\frac{(2m-r)!r!}{(m-H)!},
\]

which is (3.9).

For a pair at distance (d<h), choose the (h-d) additional top
coordinates outside (S\cup T), and apply the same four-block cyclic
count as in Theorem 3.1 to the two complementary (h)-intervals. The
result is

\[
 2(d!)^2(2m-r-d)!(r-d)!/(m-H)!,
\]

and division by (D_r) gives (3.10). When (d=h), the two complementary
(h)-intervals are disjoint blocks, giving (3.11).

Inside one packet row, there are (M) pairs at every distance
(1\le d<h), while all remaining pairs have distance (h). On
(q=o(H)), both (r) and (2m-r) are (m+o(m)), and
(h=(1+o(1))H\to\infty). Thus the (d=1) term is

\[
 \frac{2M}{r(2m-r)}=\frac{2+o(1)}m,
\]

the terms (d\ge2) are (o(1/m)), and (3.11) contributes
superpolynomially less. This proves (3.12). \(\square\)

In particular, throughout the genuinely difficult inner window
(q=O(\sqrt{m\log\log m})=o(H)), the sum of (3.12) over all lower and
upper rows is (o(1)). This removes another crude maximum-codegree
objection. It still does not prove the needed integral selection: nested
cross-row incidences and preservation of the collision floors (4.2) have
not been controlled.

The next calculation shows that the word ``nested'' is essential rather
than cosmetic.

### Theorem 3.4 (exact vertical nested-pair codegree)

Let (A\subset B\subseteq[2m]), with

\[
 |A|=a,\qquad |B|=b=a+d\le M.
\]

Among all top packets, their degrees satisfy

\[
 \boxed{
 \frac{\deg(A,B)}{\deg(B)}
 =\frac{d+1}{\binom bd}.}
 \tag{3.13}
\]

In particular, for adjacent ranks (d=1), the conditional ratio is

\[
 \frac2b=(2+o(1))/m.
 \tag{3.14}
\]

One packet realizes exactly (M(d+1)) nested pairs between its interval
rows of lengths (b) and (b-d). Hence their normalized total pair mass
is

\[
 \boxed{
 \frac{M(d+1)^2}{\binom bd}.}
 \tag{3.15}
\]

For adjacent rows this is (4+o(1)), whereas for every fixed (d\ge2)
it is (O(m^{1-d})).

#### Proof

First choose a top (U\supset B), then require both (A) and (B) to be
cyclic intervals. Once (B) is collapsed to one cyclic block, the order
inside (B) must have (A) as one consecutive linear block. The number
of internal orders is

\[
 (d+1)!a!.
\]

The complementary (M-b) labels and the (B)-block have
((M-b)!) cyclic orders. Therefore

\[
 \deg(A,B)
 =\binom{2m-b}{M-b}(M-b)!(d+1)!a!.
\]

The corresponding degree of (B) is

\[
 \deg(B)=\binom{2m-b}{M-b}(M-b)!b!.
\]

Their ratio is
((d+1)!a!/b!=(d+1)/\binom bd), proving (3.13).

Every cyclic (b)-interval contains exactly (d+1) cyclic
((b-d))-intervals, and there are (M) choices of the larger interval in
one packet. This proves (3.15). \(\square\)

Thus a maximum-codegree analysis of all decorated shadow rows has a real
nonvanishing contribution: every adjacent pair of depths carries a
deterministic nested-column mass (4+o(1)). It is not a same-rank
collision and should not be discarded as one. A successful rounding must
preserve and exploit these whole nested interval columns. Treating the
(M(2Q+1)) shadow entries of a packet as unrelated hypergraph vertices
recreates exactly the growing-atom clustering obstruction.

## 4. Exact all-depth hole ledger

Choose one packet (P_U) for every (U\in\mathcal U), without assuming
disjointness. Every packet has (M) state positions, so the total number
of state occurrences is (T=MN_H).

For (0\le q\le H), let

\[
 \mu_q^-(S),\qquad |S|=m-q,
\]

and

\[
 \mu_q^+(S),\qquad |S|=m+q,
\]

be the multiplicities of the lower and upper interval flags among all
selected packet positions. Put

\[
 C_q^\pm=\sum_S(\mu_q^\pm(S)-1)_+,
 \tag{4.1}
\]

and subtract the forced collision floor

\[
 E_q^\pm=C_q^\pm-(T-N_q)_+.
 \tag{4.2}
\]

### Theorem 4.1 (holes equal forced deficit plus collision excess)

If (M_q^\pm) is the number of missing rank-((m\pm q)) flags, then

\[
 \boxed{
 M_q^\pm=(N_q-T)_++E_q^\pm.}
 \tag{4.3}
\]

Moreover

\[
 \boxed{
 \sum_{q=0}^H(N_q-T)_+
 =O\!\left(W\frac{H^{3/2}}m\right)=o(W).}
 \tag{4.4}
\]

#### Proof

For any integer load vector of total mass (T), its support size is

\[
 T-\sum_S(\mu(S)-1)_+.
\]

Thus

\[
 M_q^\pm=N_q-T+C_q^\pm,
\]

which is exactly (4.3).

For (4.4), use (1.4). If (N_q>T), then

\[
 \lambda_q<1+\eta.
 \tag{4.5}
\]

But directly from the product for (lambda_q),

\[
 \lambda_q
 =\prod_{i=0}^{q-1}
 \left(1+\frac{2i+1}{m-i}\right)
 \ge1+\frac{q^2}{m}.
 \tag{4.6}
\]

Hence (4.5) is possible only for

\[
 q^2<m\eta=O(H).
\]

There are only (O(\sqrt H)) such depths, and at each of them

\[
 0<N_q-T\le W-T=O(WH/m).
\]

This proves (4.4). Since
(H=(1+o(1))\sqrt{m\log m}), one has
(H^{3/2}/m=o(1)). \(square\)

At depth (H), every upper flag in the packet over (U) is (U) itself,
with multiplicity (M). Therefore

\[
 C_H^+=N_H(M-1)=T-N_H,
 \qquad E_H^+=0.
 \tag{4.7}
\]

So even the apparently extreme top multiplicity is exactly the forced
balanced floor, not an error.

Combining (4.3)--(4.4), the exact residual is

\[
 \boxed{
 \sum_{q=0}^H(E_q^-+E_q^+)=o(W).}
 \tag{4.8}
\]

If the packet owner supports are pairwise disjoint, then (E_0^\pm=0)
and only (W-T=o(W)) middle owners are absent. More generally,
(E_0=o(W)) is enough; literal repair of the missing middle owners still
costs only (o(W)).

Thus exact packet disjointness is a clean sufficient strengthening, but
the OR compiler only needs small collision excess.

### Proposition 4.2 (an (o(W))-cost outer packet reservoir)

Let (gamma(m)\to\infty) with
(gamma(m)=o(\log\log m)), and put

\[
 Q=\left\lceil
 \sqrt{m(\log\log m+\gamma(m))}
 \right\rceil,
 \qquad
 \varepsilon=e^{-\gamma(m)/2}.
 \tag{4.9}
\]

After an arbitrary core selection of one packet per top, one may append

\[
 R=\left\lceil\varepsilon\frac WM\right\rceil
 \tag{4.10}
\]

additional full packets so that the total number of lower and upper holes
at all depths (Q<q\le H) is (o(W)). Their total word cost, including
initializations, is (o(W)).

#### Proof

Choose the (R) additional packets independently and uniformly from all
top/order pairs. For (q<H), one packet contains (M) distinct lower
rank-((m-q)) flags and (M) distinct upper rank-((m+q)) flags.
Coordinate transitivity therefore gives, for every fixed target,

\[
 \Pr(\text{one packet hits the target})=\frac{M}{N_q}.
 \tag{4.11}
\]

Hence, regardless of the holes left by the core selection, the expected
number remaining at depth (q) on either side is at most

\[
 N_q\exp(-RM/N_q).
 \tag{4.12}
\]

The central expansion gives

\[
 \frac{W}{N_Q}
 =\exp(Q^2/m+o(1))
 \ge (\log m)e^{\gamma(m)-o(1)}.
 \tag{4.13}
\]

Since (N_q) decreases with (q), (4.10)--(4.13) imply

\[
 \frac{RM}{N_q}
 \ge(\log m)e^{\gamma(m)/2-o(1)}
 \qquad(q>Q).
\]

Summing (4.12) over the (2H) rows gives (o(W)). At upper depth (H),
the core already hits every top once, so no reservoir estimate is needed.
Some deterministic reservoir realization is no worse than its
expectation.

Finally, its literal cost is

\[
 R(M+O(H))
 =\varepsilon W(1+o(1))+O(M)=o(W).
\]

This proves the proposition. \(\square\)

Therefore the hard integral packet discrepancy is confined to

\[
 q\le Q=(1+o(1))\sqrt{m\log\log m},
 \tag{4.14}
\]

even though the larger depth (H\sim\sqrt{m\log m}) is what makes one
reset per top affordable. On this inner window, Theorem 3.3 has total
same-row realized double-overlap mass (O(Q/m)=o(1)).

## 5. Exact PBBS subpacket bridge

There is a genuine local intersection with the PBBS zero-winding
structure. Work in the canonical PBBS factor on (2m+1) coordinates and
distinguish one coordinate (infty). Let a simple zero-winding return
have height

\[
 s=H-1.
\]

Its exact normal form has an active cyclic set (Gamma) of size

\[
 2s+1=2H-1
\]

and two inactive cores (K,K'), each of size

\[
 m-s=m-H+1.
\]

Suppose (infty\in K'). Then

\[
 U=K\cup\Gamma\subseteq[2m]
\]

has size (m+H=M). The even projected owners are

\[
 A_{2j}=K\cup V_j,
 \qquad 0\le j\le s,
 \tag{5.1}
\]

where (V_j) are (s)-windows of (Gamma). Their complements in (U)
are (H)-windows. After cutting the cyclic order of (Gamma) at the
unique boundary which linearizes these (H) consecutive windows and
then appending an arbitrary order of (K), the owners in (5.1) are
exactly (H) consecutive states of one common-top promotion packet over
(U).

Thus a PBBS simple return is a valid top-packet **subsegment**, with no
local factorability gap.

It is not a full packet. Its fraction of the (M) states is

\[
 \frac HM=o(1).
 \tag{5.2}
\]

To cover (T=(1-o(1))W) owner positions by such subsegments would require

\[
 \Theta(W/H)
 \tag{5.3}
\]

owner-disjoint sectors and, for each top, fusion of order

\[
 \frac MH=\Theta\!\left(\sqrt{m/\log m}\right)
 \tag{5.4}
\]

compatible sectors into one cyclic packet. Resetting between these
subsegments would cost order (W), so the fusion cannot be omitted.

The present PBBS quotient/packing machinery does not provide (5.3)--(5.4):

* its interval packing theorems concern return supports inside one fixed
  canonical PBBS trajectory;
* its corner and exit charges control overlaps of phases of one return;
* equal shadows in two different selected top packets are cross-fibre
  collisions and have no common PBBS chronological support to which those
  charges apply; and
* the intended PBBS Catalan packing bound would itself bound edge-disjoint
  Gaussian-window returns by (O(W/m)), whose (H)-state subsegments
  contain only (O(WH/m)=o(W)) owners.

Therefore PBBS supplies a correct local atom but, in its current form, not
the near-perfect top-indexed selection theorem.

## 6. Exact legal vertical-ladder switches

The packet space nevertheless has a useful small-support integral move.
Fix a top (U), and suppose two adjacent entries of its selected cyclic
order are

\[
 \ldots,x_{-1},a,b,x_2,\ldots .
\]

Let (pi') be obtained by swapping (a,b).

### Theorem 6.1 (adjacent swap changes two interval boundaries per row)

For every proper interval length (2\le\ell\le M-2), the interval
families of (pi) and (pi') differ only by

\[
 L_{\ell-1}\cup\{a\}
 \longleftrightarrow
 L_{\ell-1}\cup\{b\},
 \tag{6.1}
\]

and

\[
 \{b\}\cup R_{\ell-1}
 \longleftrightarrow
 \{a\}\cup R_{\ell-1},
 \tag{6.2}
\]

where

\[
 L_{\ell-1}=\{x_{1-\ell},\ldots,x_{-1}\},
 \qquad
 R_{\ell-1}=\{x_2,\ldots,x_\ell\}.
\]

At lengths (1,M-1), the interval family is unchanged as an unordered
set, and at length (M) it is the single top (U).

Consequently one adjacent swap changes exactly two middle owners, at most
two lower targets in every row, and at most two upper targets in every
proper row. Across the depths, its complete support is the union of two
nested boundary ladders.

#### Proof

An interval whose membership changes must contain exactly one of the two
adjacent coordinates (a,b). There is a unique length-(ell) interval
which contains (a) but not (b): the interval ending at (a). There is
likewise a unique interval containing (b) but not (a): the interval
starting at (b). These are exactly (6.1)--(6.2). All other intervals
contain both coordinates or neither, so their underlying sets do not
change. The endpoint cases are immediate. As (ell) varies, the left
blocks and right blocks are nested, proving the ladder assertion.
\(\square\)

Adjacent swaps generate every cyclic order of a fixed top. Hence the
space of one-packet-per-top selections is a connected product of legal
switch graphs, and every switch has only (O(Q)) support on the hard rows
from Proposition 4.2. This gives a sharper possible route than a generic
growing-uniformity matching theorem:

> prove that every selection whose balanced shadow excess is not (o(W))
> admits either one improving vertical-ladder swap, or a bounded collection
> of such swaps with negative total excess drift.

No such descent inequality is proved here. Theorem 3.4 explains why it
must treat each ladder as one correlated object: its adjacent-depth
incidences carry constant normalized mass.

There is also an exact warning against a two-top correction.

### Proposition 6.2 (no nontrivial two-top cancellation)

The four middle owners changed by one adjacent swap have union exactly the
top (U). Consequently, if two adjacent-swap owner-change vectors sum to
zero, then their tops are equal. A two-top switch cannot preserve the
middle-owner load vector while changing any shadow row.

#### Proof

At owner length (m), the two old changed intervals are the length-(m)
interval ending at (a) and the length-(m) interval starting at (b).
Together they occupy (2m) consecutive positions of the cyclic order.
Since

\[
 |U|=M=m+H\le2m,
\]

their union is all of (U). Thus the support of the swap's owner-change
vector determines (U).

If two ({-1,0,1})-valued four-support change vectors are negatives of
one another, their supports agree. Their support unions, and hence their
tops, agree. \(\square\)

Therefore exact owner-preserving shadow descent needs a genuinely
multi-top circuit, not a paired local exchange. This is the precise point
at which the known finite nonlocal factor-fibre circuits are relevant; an
all-dimensional suspension or abundance theorem for such circuits remains
missing.

## 7. The exact surviving packet theorem

The following statement is sufficient for coefficient one.

> **Critical shallow top-packet matching/discrepancy theorem.** At the
> first depth (H) satisfying (lambda_H\ge m+H), choose one directed
> cyclic order (pi_U) for every
> (U\in\binom{[2m]}{m+H}) so that, for (Q) in (4.9),
> \[
>   \sum_{q=0}^Q(E_q^-+E_q^+)=o(W),
> \]
> with (E_q^\pm) defined by (4.1)--(4.2).

A stronger, cleaner owner clause is that the packet supports
(mathcal P(U,pi_U)) are pairwise disjoint; because their total size is
(T=W-o(W)), this is a near-perfect matching of the middle owners.

Indeed, cut every selected cycle once and initialize it independently.
The word length is

\[
 T+O(HN_H)=W+o(W).
\]

Equations (4.3)--(4.4) repair the inner holes, Proposition 4.2 supplies
the remaining controlled rows at (o(W)) cost, and the two outer Boolean
tails also cost (o(W)) at depth (H). Hence the theorem gives a literal
contiguous-OR word of length (W+o(W)).

The packet hypergraph has all of the favorable scalar properties:

* exact fractional matching;
* owner slack only (O(H/m));
* maximum relative pair codegree (2/m^2+o(m^{-2}));
* total reset cost (o(W)); and
* total forced shadow-hole floor (o(W)).

What remains is precisely the critical integral cancellation represented
by (3.6) and the simultaneous shadow discrepancy (4.8). Neither is a
divisibility, tail, reset, or local PBBS-factorability problem.
