# Coordinate-overlapping chain compression of the arbitrary-\(k\) \(Q_2\) carrier

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

The arbitrary-\(k\) common-owner carrier can be compressed from
\(6k+10\) coordinates to

\[
                         n_k=2k+2t+8,
 \qquad                   t=\lceil\log_2(k+1)\rceil,
\tag{0.1}
\]

without changing its owner count, factor cube, signed ledgers, death
density, common phase, or suspension.

The compressed construction uses a chain of coordinate pairs
\(P_0,\ldots,P_k\).  Seed \(i\) acts on the adjacent pair triple
\(P_{i-1},P_i,S\), where the splitter pair \(S\) is common to all seeds.
The \(k+1\) carrier sectors are separated by \(t\) binary tag pairs.

For every \(k\ge1\), it gives:

\[
 |\mathcal U_k^{\rm ch}|=16(2k+1),
 \qquad
 4(2k+1)\text{ physical }Q_2\text{'s per factor},
\tag{0.2}
\]

\[
 L^-_\epsilon
 =16(k+|\epsilon|)f_0+16(k+1-|\epsilon|)f_1,
\tag{0.3}
\]

\[
 L^+_\epsilon
 =16(k+|\epsilon|)f_1+16(k+1-|\epsilon|)f_2,
\tag{0.4}
\]

and an all-new pointwise death density

\[
                         {k\over2k+1}.
\tag{0.5}
\]

All \(2^k\) factors share one \(\mathbb Z_4\) owner phase and suspend on
identical support at every length.

The exact unbiased-block eligibility is

\[
 \boxed{
 p_k^{\rm ch}
 ={16(2k+1)\over2^{2k+2t+8}}
 ={2k+1\over2^{2k+2t+4}}.}
\tag{0.6}
\]

Consequently a near-spanning tensor with
\(r=m^{2/3+o(1)}\) carrier blocks exists whenever

\[
                         \boxed{k^2 4^k=o(m^{1/3}).}
\tag{0.7}
\]

This is genuine coordinate overlap but not repeated owner overlap.
Adjacent seed gadgets share \(P_i\) and all seeds share \(S\), yet their
owner supports are tag-disjoint.  Every owner belongs to exactly one seed
sector or to the survivor sector, so no owner is simultaneously recoupled
by several chain seeds in one static corner.  Section 8 gives a separate
adaptive rank-rotation of the exact corner menu under which the same
tagged owner sector is recoupled on, off, and on again along a sequence.
That repeated action remains context-dependent and tag-sectorwise; it is
not simultaneous multihit ownership.

## 1. Coordinates and tags

For \(j=0,1,\ldots,k\), let

\[
                         P_j=\{a_j,b_j\}
\tag{1.1}
\]

be pairwise disjoint coordinate pairs.  Let

\[
                         S=\{s_0,s_1\}
\tag{1.2}
\]

be a further splitter pair.

Take \(t=\lceil\log_2(k+1)\rceil\) tag pairs

\[
                         T_\ell=\{z_\ell^0,z_\ell^1\},
 \qquad 1\le\ell\le t.
\tag{1.3}
\]

Choose distinct binary words

\[
                         \gamma(0),\gamma(1),\ldots,\gamma(k)
                         \in\{0,1\}^t
\tag{1.4}
\]

and put

\[
                         G_i=
 \{z_\ell^{\gamma_\ell(i)}:1\le\ell\le t\}.
\tag{1.5}
\]

Thus every tag state selects one endpoint of every tag pair, and distinct
sectors have distinct tag restrictions.

Finally take two reservoir pairs

\[
                         R_1=\{u,v\},
 \qquad                   R_2=\{w,x\},
\tag{1.6}
\]

with split orientations

\[
 \mathcal Y=\{uw,vw,vx,ux\},
 \qquad Q_R=(uw,vw,vx,ux).
\tag{1.7}
\]

The total number of pairs is

\[
 (k+1)+1+t+2=k+t+4,
\tag{1.8}
\]

which proves the ambient coordinate count in (0.1).

## 2. Adjacent local seeds

For \(1\le i\le k\), define

\[
\begin{aligned}
 D_i=\{&a_{i-1}b_{i-1}s_0,
        a_{i-1}b_{i-1}s_1,\\
       &a_i b_i s_0,
        a_i b_i s_1\},
\end{aligned}
\tag{2.1}
\]

and

\[
\begin{aligned}
 Z_i=\{&b_{i-1}a_i s_0,
        a_{i-1}b_i s_0,\\
       &b_{i-1}a_i s_1,
        a_{i-1}b_i s_1\}.
\end{aligned}
\tag{2.2}
\]

Every \(D_i\)-state contains exactly one full chain pair.  Every
\(Z_i\)-state splits \(P_{i-1},P_i,S\).

For \(\eta\in\{0,1\}\), the four states with splitter endpoint
\(s_\eta\) form the physical square

\[
 Q_{i,\eta}=
 (a_{i-1}b_{i-1}s_\eta,
  b_{i-1}a_i s_\eta,
  a_i b_i s_\eta,
  a_{i-1}b_i s_\eta).
\tag{2.3}
\]

Its two axes are the disjoint coordinate swaps

\[
 a_{i-1}\leftrightarrow a_i,
 \qquad
 b_{i-1}\leftrightarrow b_i.
\tag{2.4}
\]

The two squares \(Q_{i,0},Q_{i,1}\) are disjoint and partition
\(D_i\dot\cup Z_i\).

Freeze every chain pair outside the active adjacent pair at its first
endpoint.  Thus put

\[
 A_i=\{a_j:0\le j\le k,\ j\notin\{i-1,i\}\}
\tag{2.5}
\]

and embed an active local state by

\[
                         E_i(X)=G_i\cup A_i\cup X,
 \qquad 1\le i\le k.
\tag{2.6}
\]

The seed sectors are

\[
                         \mathcal S_i^{\rm ch}
 =\{E_i(X):X\in D_i\cup Z_i\}.
\tag{2.7}
\]

Use tag word \(\gamma(0)\) for the survivor.  Its raw local states are a
second tagged copy of \(D_1\):

\[
                         \mathcal S_0^{\rm ch}
 =\{G_0\cup A_1\cup X:X\in D_1\}.
\tag{2.8}
\]

The survivor and seed 1 may therefore have identical untagged chain
restrictions, but never identical full states.

### Lemma 2.1 (tag-disjoint sectors)

The \(k+1\) families

\[
 \mathcal S_0^{\rm ch},\mathcal S_1^{\rm ch},\ldots,
 \mathcal S_k^{\rm ch}
\tag{2.9}
\]

are pairwise disjoint.

#### Proof

Every state in sector \(i\) restricts to \(G_i\) on the tag coordinates.
The words \(\gamma(i)\) are distinct, so two different sectors disagree
on at least one tag pair. \(\square\)

Every special state has rank

\[
 3+(k-1)+t=k+t+2
\tag{2.10}
\]

on the \(k+t+2\) nonreservoir pairs.  Thus it selects exactly one
coordinate per pair on average, even though a \(D_i\)-state fills one
chain pair and empties its adjacent chain pair.

## 3. Common carrier and exact factor cube

Define

\[
 \boxed{
 \mathcal U_k^{\rm ch}
 =\{X\cup Y:
 X\in\mathcal S_0^{\rm ch}\dot\cup\cdots\dot\cup
       \mathcal S_k^{\rm ch},\ Y\in\mathcal Y\}.}
\tag{3.1}
\]

After adjoining a reservoir orientation, every owner has rank

\[
                         k+t+2+2=k+t+4
\tag{3.2}
\]

on \(2(k+t+4)\) coordinates.  Hence the carrier is literally middle
layer.

There are four survivor special states, eight in every seed sector, and
four reservoir orientations.  Lemma 2.1 gives

\[
                         |\mathcal U_k^{\rm ch}|
 =4(4+8k)=16(2k+1).
\tag{3.3}
\]

For seed \(i\), define its old shore by the eight vertical cells

\[
 \mathscr A_i^0
 =\{E_i(X)\cup Q_R:X\in D_i\cup Z_i\},
\tag{3.4}
\]

and its new shore by the eight special cells

\[
 \mathscr A_i^1
 =\{(G_i\cup A_i\cup Q_{i,\eta})\cup Y:
       \eta\in\{0,1\},\ Y\in\mathcal Y\}.
\tag{3.5}
\]

Both shores partition the same 32-owner seed sector by (2.3).

The fixed survivor shore is

\[
 \mathscr A_0
 =\{(G_0\cup A_1\cup X)\cup Q_R:X\in D_1\}.
\tag{3.6}
\]

For \(\epsilon\in\{0,1\}^k\), put

\[
 \boxed{
 \mathscr F_\epsilon^{\rm ch}
 =\mathscr A_0\mathbin{\dot\cup}
  \mathop{\dot\bigcup}_{i=1}^k\mathscr A_i^{\epsilon_i}.}
\tag{3.7}
\]

### Theorem 3.1 (exact chain factor cube)

Every \(\mathscr F_\epsilon^{\rm ch}\) partitions
\(\mathcal U_k^{\rm ch}\) exactly once into

\[
                         4+8k=4(2k+1)
\tag{3.8}
\]

physical \(Q_2\)'s.

#### Proof

Equations (3.4) and (3.5) are exact alternative partitions within one
seed sector.  Equation (3.6) partitions the survivor sector.  Lemma 2.1
makes all sectors disjoint, so their union has neither collision nor
leave. \(\square\)

## 4. Exact lower and upper ledgers

Use the fixed matching whose pairs are all \(P_j\), the splitter \(S\),
all tag pairs, and the two reservoir pairs.  Every inactive chain state,
tag state, and reservoir orientation is split.

On an old seed shore, the four \(D_i\)-cells contribute \(16f_1\) below,
while the four \(Z_i\)-cells contribute \(16f_0\).  Every lower edge of a
new special square has local intersection one of

\[
 b_{i-1}s_\eta,\quad a_i s_\eta,\quad
 b_i s_\eta,\quad a_{i-1}s_\eta,
\tag{4.1}
\]

so the new shore contributes \(32f_0\).  The survivor contributes
\(16f_1\).  This proves (0.3).

Every old vertical upper edge fills one reservoir pair, and therefore has
type one above \(Z_i\) and type two above \(D_i\).  Every new special
upper union contains exactly one of \(P_{i-1},P_i\), while the splitter
endpoint and reservoir orientation remain split.  Thus old and new seed
upper ledgers are

\[
                         16f_1+16f_2,
 \qquad                   32f_1,
\tag{4.2}
\]

and the survivor contributes \(16f_2\).  This proves (0.4).

Every bit consequently has the exact background-independent drifts

\[
                         16(e_0-e_1)
 \quad\hbox{and}\quad     16(e_1-e_2).
\tag{4.3}
\]

The \(k\) death classes are the sixteen owners over the tagged
\(D_i\)-states.  They are disjoint by Lemma 2.1.  The survivor-high class
has sixteen owners and the buffer-zero classes have total size \(16k\),
which proves (0.5) pointwise.

## 5. Common phase, suspension, and phasewise operator

Assign \(g=0,1,2,3\) cyclically on each embedded square
\(G_i\cup A_i\cup Q_{i,\eta}\).  This is consistent because the two
splitter squares in one sector are disjoint and different sectors are
tag-disjoint.  Assign arbitrary \(g\)-values on the survivor states.

Order \(\mathcal Y\) as \(y_0=uw,y_1=vw,y_2=vx,y_3=ux\), and colour

\[
                         c(X\cup y_j)=g(X)+j\pmod4.
\tag{5.1}
\]

This is cyclic on every vertical cell and every special cell.  Therefore
one owner colouring is compatible with all cells of all \(2^k\) factors.
The standard coloured-square suspension produces
\(4(2k+1)\) physical \(C_{2h}\)'s on one identical support for every
\(h\ge2\).

The phase-balanced cube charts also carry over verbatim.  Chart the
\(s_0\)-square in its displayed order and the \(s_1\)-square after one
cyclic rotation.  At every fixed abstract \(Q_2\)-vertex, exactly four of
the eight cells in each new seed sector expose a death vertex.  Old
vertical cells use the reservoir chart.

Hence a corner of weight \(s\) has, conditional on every Hamming phase,
the exact lower death and upper birth rates

\[
                         p_s^-={s\over2k+1},
 \qquad                   p_s^+=1-p_s^-.
\tag{5.2}
\]

In particular the all-new product-transversal \(q\)-window has

\[
 D_q\sim\operatorname{Bin}\left(q,{k\over2k+1}\right),
 \qquad
 B_q=q-D_q
 \sim\operatorname{Bin}\left(q,{k+1\over2k+1}\right).
\tag{5.3}
\]

The phasewise buffer/death/survivor multiplicities remain \(4k,4k,4\),
so the exact joint source/lower/upper polynomial remains

\[
                         \Xi_k(x,y,z)
 ={kz+kxz+xyz^2\over2k+1}.
\tag{5.4}
\]

Thus chain compression changes inventory, not the signed type operator.

## 6. Exact eligibility and growing packing

The ambient block has \(n_k=2k+2t+8\) coordinates and the carrier has
\(16(2k+1)\) owners.  Therefore

\[
 p_k^{\rm ch}
 ={16(2k+1)\over2^{n_k}}
 ={2k+1\over2^{2k+2t+4}},
\tag{6.1}
\]

which is (0.6).

Since \(t=\lceil\log_2(k+1)\rceil\),

\[
                         (k+1)^2\le2^{2t}<4(k+1)^2.
\tag{6.2}
\]

Writing \(4^k=2^{2k}\), (6.1) and (6.2) give the explicit bounds

\[
 {2k+1\over64\,4^k(k+1)^2}
 <p_k^{\rm ch}
 \le
 {2k+1\over16\,4^k(k+1)^2}.
\tag{6.3}
\]

Partition the \(2m\) ordinary coordinates into

\[
                         B=\left\lfloor{2m\over n_k}\right\rfloor
                          =\left\lfloor{m\over k+t+4}\right\rfloor
\tag{6.4}
\]

labelled chain blocks.  If \(m\ge2(k+t+4)\), then

\[
 {m\over2(k+t+4)}\le B\le {m\over k+t+4}.
\tag{6.5}
\]

Combining (6.3)--(6.5),

\[
 {m(2k+1)\over
  128(k+t+4)4^k(k+1)^2}
 <Bp_k^{\rm ch}
 \le
 {m(2k+1)\over
  16(k+t+4)4^k(k+1)^2}.
\tag{6.6}
\]

In particular, \(1\le t\le k\) because \(2^k\ge k+1\) for \(k\ge1\).
Using also \(k+t+4\le6k\), \((k+1)^2\le4k^2\), and
\(2k+1\le3k\), one obtains the coarser uniform
bounds

\[
 {m\over1536\,k^2 4^k}
 <Bp_k^{\rm ch}
 \le {3m\over16\,k^2 4^k}.
\tag{6.7}
\]

Thus

\[
                         Bp_k^{\rm ch}
 =\Theta\left({m\over k^2 4^k}\right).
\tag{6.8}
\]

For every integer \(r\le Bp_k^{\rm ch}/2\), the first-\(r\)-eligible
selector gives disjoint canonical packets
\((\mathcal U_k^{\rm ch})^r\), and the half-mean Chernoff estimate gives

\[
 {W-G\over W}
 \le2(m+1)\exp\left(-{Bp_k^{\rm ch}\over8}\right).
\tag{6.9}
\]

If \(k^2 4^k=o(m^{1/3})\), then (6.7) gives

\[
                         Bp_k^{\rm ch}=\omega(m^{2/3}).
\tag{6.10}
\]

Choose a power-of-two \(2r\) with

\[
                         {1\over2}m^{2/3}\le r\le m^{2/3}.
\tag{6.11}
\]

For all sufficiently large \(m\), (6.10) implies
\(r\le Bp_k^{\rm ch}/2\).  Tensoring the local factors and applying the
standard Hamming factor gives a literal \(C_{4r}\)-factor on the retained
owners with exactly

\[
                         {G\over4r}
\tag{6.12}
\]

components.  Through \(H=O_A(\sqrt m)\), its certified collar is

\[
                         O\left({HW\over r}\right)=o(W).
\tag{6.13}
\]

When \(k\to\infty\) under (0.7), (5.3) has lower and upper centre errors
\(O_A(\sqrt m/k+1)=o(\sqrt m)\) and fluctuations
\(O_p(m^{1/4})\).  Hence the leading Gaussian pair-type conclusion of the
uncompressed carrier remains valid with the improved inventory.

## 7. Exact boundary

Proved:

1. a coordinate-overlapping adjacent-chain realization for arbitrary
   \(k\);
2. tag-disjoint exact one-copy ownership for all \(2^k\) factor corners;
3. unchanged pointwise lower and upper ledgers and death density;
4. one common \(\mathbb Z_4\) phase and all-length suspension;
5. the unchanged phasewise birth--death operator;
6. exact eligibility
   \((2k+1)/2^{2k+2t+4}\); and
7. near-spanning long-cycle packing under
   \(k^2 4^k=o(m^{1/3})\), with \(o(W)\) certified collar.

Not proved:

* a context-independent fixed-generator cube in which one owner belongs
  simultaneously to several adjacent physical seed sectors (Section 8
  gives a weaker but literal adaptive repeated-owner realization);
* dependent multihit action beyond the tag-disjoint Poisson-binomial law;
* exact finite orbit or labelled target balance;
* occurrence-resolved all-depth collision control; or
* coefficient one.

The chain theorem is therefore a strict carrier-density improvement and
an exact sequential-coordinate-overlap realization.  Section 8 adds
adaptive repeated-owner transport; fixed-generator multihit transport
remains open.

## 8. Adaptive rank-rotated cube and repeated owner recoupling

There is a second, genuinely adaptive use of the same exact factor menu.
Let

\[
                         \rho=(1\ 2\ \cdots\ k)
\tag{8.1}
\]

act on seed labels, and for every logical subset \(S\subseteq[k]\) put

\[
                         \Psi(S)=\rho^{|S|}(S).
\tag{8.2}
\]

Define the rank-rotated factor cube by

\[
                         \widetilde{\mathscr F}_S
 =\mathscr F^{\rm ch}_{\Psi(S)}.
\tag{8.3}
\]

### Theorem 8.1 (exact adaptive cube)

The family \(\{\widetilde{\mathscr F}_S:S\subseteq[k]\}\) consists of
\(2^k\) distinct literal exact factors on the same carrier and with the
same common \(\mathbb Z_4\) phase.  Every logical Boolean edge
\(S\to S\cup\{j\}\) has the aggregate signed drift

\[
                         16(e_0-e_1)
 \quad\hbox{below},\qquad
                         16(e_1-e_2)
 \quad\hbox{above}.
\tag{8.4}
\]

Nevertheless, for \(k\ge3\), one and the same tagged owner sector is
recoupled on, then off, and later on again along a nested logical path.

#### Proof

On the rank-\(r\) Boolean layer, \(S\mapsto\rho^rS\) is a bijection of
the \(r\)-subsets.  Hence \(\Psi\) is a bijection of the whole Boolean
lattice and preserves cardinality.  The original physical factor cube
has distinct corners, so (8.3) also has \(2^k\) distinct exact corners.
Common support and common phase are inherited cornerwise.

The ledger of \(\mathscr F_T^{\rm ch}\) depends only on \(|T|\).  If
\(j\notin S\), then

\[
 |\Psi(S\cup\{j\})|-|\Psi(S)|
 =|S|+1-|S|=1,
\tag{8.5}
\]

so (0.3)--(0.4) give (8.4), regardless of how many physical seed shores
change.

For repeated recoupling, take the nested path

\[
 S_0=\varnothing,\qquad
 S_r=\{k,1,2,\ldots,r-1\}\quad(1\le r\le k).
\tag{8.6}
\]

Then

\[
 \Psi(S_1)=\{1\},
 \qquad
 \Psi(S_2)=\{2,3\},
 \qquad
 \Psi(S_k)=[k].
\tag{8.7}
\]

For \(k\ge3\), physical seed sector 1 is therefore old at \(S_0\), new
at \(S_1\), old at \(S_2\), and new again at \(S_k\).  The carrier owners
in tagged sector 1 are identical at all four corners.  Thus the repeated
recoupling is literal, not an aggregate relabelling of owner mass.
\(\square\)

### Proposition 8.2 (exact edge cost)

Let \(|S|=r\) and \(j\notin S\).  The number of physical seed sectors
whose shores change on the logical edge \(S\to S\cup\{j\}\) is

\[
\boxed{
 d_j(S)
 =|\Psi(S)\mathbin\triangle\Psi(S\cup\{j\})|
 =2r+1-2|S\cap\rho S|-2\mathbf1_{\{\rho j\in S\}}.}
\tag{8.8}
\]

In particular

\[
 1\le d_j(S)\le
 \min\{2r+1,\,2k-2r-1\},
\tag{8.9}
\]

and \(d_j(S)\) is odd.  The edge turns on exactly

\[
                         {d_j(S)+1\over2}
\tag{8.10}
\]

physical sectors and turns off exactly

\[
                         {d_j(S)-1\over2}.
\tag{8.11}
\]

It recouples \(32d_j(S)\) carrier owners.  Equivalently it replaces
\(8d_j(S)\) old shore cells by \(8d_j(S)\) new shore cells, with
\(16d_j(S)\) cell records in the symmetric difference of the two factor
cell sets.

#### Proof

Put \(A=\Psi(S)=\rho^rS\) and
\(B=\Psi(S\cup\{j\})=\rho^{r+1}(S\cup\{j\})\).  Applying \(\rho^{-r}\)
to the intersection gives

\[
 |A\cap B|
 =|S\cap(\rho S\cup\{\rho j\})|
 =|S\cap\rho S|+\mathbf1_{\{\rho j\in S\}}.
\tag{8.12}
\]

The last equality uses \(j\notin S\), which implies
\(\rho j\notin\rho S\).  Since \(|A|=r\) and \(|B|=r+1\), equation
(8.8) follows.  The general intersection bound

\[
                         |A\cap B|\ge\max\{0,2r+1-k\}
\tag{8.13}
\]

gives (8.9).  The size difference \(|B|-|A|=1\) then gives
(8.10)--(8.11).  Thus the \((d+1)/2\) forward shore drifts and
\((d-1)/2\) reverse shore drifts cancel to exactly one copy of (8.4).
Each changed tagged seed sector has 32 owners and its two shores contain
eight cells apiece, proving the physical counts.
\(\square\)

The repeated-owner path (8.6) is especially cheap.  Its first and last
logical edges have \(d=1\), while every intervening edge has

\[
                         d=3.
\tag{8.14}
\]

Indeed, for \(1\le r\le k-2\),
\(|S_r\cap\rho S_r|=r-1\) and the newly added \(j=r\) satisfies
\(\rho j\notin S_r\).  On the last edge the indicator term in (8.8) is
one.  Thus the same owners can be recoupled repeatedly while every step
replaces at most three physical seed shores and still has net unit signed
drift.

### Exact scope of adaptivity

The map \(\Psi\) is context-dependent.  The physical toggle set for
logical direction \(j\) is

\[
 \Delta_j(S)=
 \Psi(S)\mathbin\triangle\Psi(S\cup\{j\}),
\tag{8.15}
\]

and depends on \(S\).  For example, with \(j=k\),

\[
                         \Delta_k(\varnothing)=\{1\},
 \qquad                   \Delta_k(\{1\})=\{3\}
\tag{8.16}
\]

for every \(k\ge3\).  Hence these logical directions are not fixed
commuting products of the original sectorwise shore involutions.  A fixed
sectorwise-XOR model would have \(\Delta_j(S)\) independent of the context
\(S\).

Tautologically, the maps \(S\mapsto S\triangle\{j\}\) still define
commuting involutions of the *abstractly relabelled corner set*.  The
claim is not that the logical Boolean cube has lost commutativity.  The
claim is that those logical involutions have no context-independent
realization by fixed local physical shore toggles; their physical action
is adaptive through (8.15).

Every individual corner remains one of the already certified exact
factors, and every adaptive edge is a simultaneous replacement of whole
tag-disjoint shores.  Thus integrality, literal ownership and common phase
are preserved.  What is new is repeated context-dependent recoupling of
the same owner sector along a sequence.  What is still not supplied is a
single factor in which one owner simultaneously belongs to several seed
sectors, or a proof that the adaptive labelled all-depth deltas balance
all target fibres.
