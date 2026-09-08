# Distance-one near-C bridges give a genuine positive one-owner common reserve at q=2

**Date:** 2026-08-13
**Status:** unconditional exact positive theorem for $q=d+1=2$, all
$c>q$, and the explicit ambient range below. The reserve consists of
actual legal closed rails, every coefficient is one, and every named-owner
collision is audited. This is not a signed-lattice argument. No claim is
made here for $q\ge3$.

## 1. Setup and the reduced bridge notation

Put

\[
 q=2,\qquad R=c+2,\qquad M=k-c,
 \qquad c\ge3,\qquad M\ge\max\{8,c+2\}.
\tag{1.1}
\]

Write

\[
 C=C_0\mathbin{\dot\cup}\{0\},\qquad |C_0|=c-1,
\tag{1.2}
\]

and choose distinct labels $1,\ldots,8$ outside $C$. Designate

\[
 P=\{1,2\},\qquad H=C\cup P.
\tag{1.3}
\]

For $i\in\{0,\ldots,8\}$, let

\[
 K_i=C_0\cup\{i\}.
\tag{1.4}
\]

Thus $K_0=C$, while for every $i\ne0$,

\[
 K_i=C-\{0\}+\{i\}
\tag{1.5}
\]

is a distance-one near-$C$ bridge core.

Suppress the common set $C_0$, and write

\[
 [ijk]=C_0\cup\{i,j,k\}.
\tag{1.6}
\]

For a word $\sigma=(v_0,\ldots,v_{N-1})$ of distinct labels avoiding
$i$, let $Q(i;\sigma)$ be the period-$N$ rail with core $K_i$ and
that cyclic toggle order. Since $q=2$, its complete named-owner deck is

\[
 \mathcal D Q(i;\sigma)
 =\{[i v_j v_{j+1}]:j\in\mathbb Z_N\}.
\tag{1.7}
\]

All periods in the certificate are $6$ or $7$. They are legal because
$2(q+1)=6$ and $M\ge8$.

## 2. The explicit positive bridge certificate

Consider the following two collections of eight closed rails. The last
column lists the complete owner deck of each rail, not merely its point
signature.

### The positive collection

| core | cyclic toggle word | complete reduced owner deck |
|---|---|---|
| $K_0$ | $124685$ | $012,024,046,068,058,015$ |
| $K_0$ | $263748$ | $026,036,037,047,048,028$ |
| $K_1$ | $2486375$ | $124,148,168,136,137,157,125$ |
| $K_2$ | $1356487$ | $123,235,256,246,248,278,127$ |
| $K_3$ | $142678$ | $134,234,236,367,378,138$ |
| $K_5$ | $038247$ | $035,358,258,245,457,057$ |
| $K_6$ | $143827$ | $146,346,368,268,267,167$ |
| $K_8$ | $015647$ | $018,158,568,468,478,078$ |

Call this component collection $\mathcal A^+$. Its period multiset is

\[
 (6,6,7,7,6,6,6,6)
\tag{2.1}
\]

and it has $50$ owner occurrences.

### The negative collection

| core | cyclic toggle word | complete reduced owner deck |
|---|---|---|
| $K_0$ | $1537468$ | $015,035,037,047,046,068,018$ |
| $K_1$ | $258437$ | $125,158,148,134,137,127$ |
| $K_2$ | $046358$ | $024,246,236,235,258,028$ |
| $K_3$ | $124678$ | $123,234,346,367,378,138$ |
| $K_4$ | $125786$ | $124,245,457,478,468,146$ |
| $K_6$ | $025813$ | $026,256,568,168,136,036$ |
| $K_7$ | $051628$ | $057,157,167,267,278,078$ |
| $K_8$ | $042635$ | $048,248,268,368,358,058$ |

Call this component collection $\mathcal A^-$. Its period multiset is

\[
 (7,6,6,6,6,6,6,6)
\tag{2.2}
\]

and it has $49$ owner occurrences.

Define the following explicit $49$-owner set:

\[
\begin{aligned}
 \mathcal R_0=\{&015,018,024,026,028,035,036,037,046,047,048,057,058,
 068,078,\\
 &123,124,125,127,134,136,137,138,146,148,157,158,167,168,\\
 &234,235,236,245,246,248,256,258,267,268,278,346,358,367,
 368,378,457,468,478,568\},
\end{aligned}
\tag{2.3}
\]

where every word $ijk$ means the named owner $[ijk]$.

### Theorem 2.1 (positive distance-one one-owner absorber)

Both component collections are owner matchings, and their complete owner
vectors satisfy

\[
 \boxed{
 \sum_{Q\in\mathcal A^+}f(Q)=e_H+\mathbf1_{\mathcal R_0},
 \qquad
 \sum_{Q\in\mathcal A^-}f(Q)=\mathbf1_{\mathcal R_0}.}
\tag{2.4}
\]

In particular,

\[
 \sum_{Q\in\mathcal A^+}f(Q)
 -\sum_{Q\in\mathcal A^-}f(Q)=e_H
\tag{2.5}
\]

is a genuine positive one-owner trade between two simple closed-rail
collections. Every non-$C$ core used in it is exactly of the form
$C-0+i$.

#### Proof

Reading cyclic consecutive pairs in the two tables gives the displayed
decks by (1.7). No owner is repeated within either table. The sorted
owner list of the second table is exactly (2.3); the sorted owner list of
the first is exactly (2.3) together with $012$, which is $H$. This
proves simplicity and (2.4) directly over the named-owner basis. The
period sums are $50$ and $49$, as required. No cancellation inside a
component and no negative coefficient occurs. $\square$

The certificate therefore goes strictly beyond the scalar residue in the
distance-one character calculation: it resolves all $49$ collateral
named owners, their core assignments, their periods, and all same-state
collisions.

## 3. Why a compound bridge certificate is necessary

The following exact observation rules out the most economical-looking
one-rail attempt for every $q>1$.

### Proposition 3.1 (one rail on each side cannot absorb one owner)

Let $C_0$ be fixed and let every allowed core be $C_0+r$. Suppose
two legal rails $Q^+,Q^-$, with the same $q\ge2$, had simple decks
obeying

\[
 f(Q^+)=f(Q^-)+e_H.
\tag{3.1}
\]

Then no such pair exists.

#### Proof

If the smaller period is $N$, the larger is $N+1$, and all $N$
owners of the smaller deck must occur in the larger deck.

If the cores agree, every toggle label of the smaller rail occurs in
$q$ of its owners, so containment of decks forces containment of toggle
supports. The supports consequently differ by one label. Of the
$N+1$ cyclic $q$-windows of the larger support, exactly $q$ contain
the new label. Hence at most $N+1-q<N$ can belong to the smaller deck,
a contradiction.

If the cores are $C_0+r$ and $C_0+s$ with $r\ne s$, every common
owner contains both $r$ and $s$. In the rail centred at $r$, the
label $s$ is either unused or is a toggle and occurs in exactly $q$
owners. Thus the decks intersect in at most $q$ owners. But a legal
smaller period satisfies $N\ge2q+2>q$, again a contradiction.
$\square$

Thus the point-signature of one bridge rail cannot itself be promoted to
a one-owner reserve. The eight-by-eight compound trade in Theorem 2.1 is
not being used as shorthand for a signed one-column identity.

## 4. Compatibility with the insertion/star one-owner macro

We now exhibit a choice of the one-owner macro for which (2.4) is an
actual common reserve for its compulsory shores.

At $q=2$ there is only one correction leaf. Consequently the repeated-
centre packing inequality used for the general star construction is not
needed: one centre potential and one leaf potential are automatically
simple on each signature-separated shore. All required disjointness is
checked directly below.

Use the insertion pair with core $C=K_0$

\[
 Q_\Delta^- =Q(0;234567),
 \qquad
 Q_\Delta^+=Q(0;2134567).
\tag{4.1}
\]

Thus the label $1$ is inserted between $2$ and $3$. Its reduced
decks are

\[
\begin{aligned}
 \mathcal DQ_\Delta^-&=\{023,034,045,056,067,027\},\\
 \mathcal DQ_\Delta^+&=\{012,013,034,045,056,067,027\}.
\end{aligned}
\tag{4.2}
\]

In particular $H=012$ is a new positive owner. Directly from (2.3),

\[
 \mathcal R_0\cap
 (\mathcal DQ_\Delta^-\cup\mathcal DQ_\Delta^+)=\varnothing.
\tag{4.3}
\]

Choose a $(c+1)$-set $S\subseteq[k]\setminus C$ containing
$\{1,2\}$, choose $z\notin C\cup S$, and put

\[
 E=[k]\setminus(S\cup\{z\}),\qquad |E|=M-2\ge6.
\tag{4.4}
\]

For $u=1,2$, choose a cyclic order $\tau_u$ on $E$, choose an
insertion gap for $z$, and write $\tau_u^+$ for the resulting order
on $E+z$. When $c=3$, additionally choose $\tau_u$ so that the two
labels of $C_0$ are nonadjacent. Such an order exists because
$|E|\ge6$; insertion preserves their nonadjacency. Put

\[
 \Phi_u=
 f(S-u,E+z,\tau_u^+)-f(S-u,E,\tau_u),
\tag{4.5}
\]

and

\[
 Y_H=(f(Q_\Delta^+)-f(Q_\Delta^-))+\Phi_1-\Phi_2.
\tag{4.6}
\]

Its two raw component shores are therefore

\[
\begin{aligned}
 \mathcal Y^+
 &=\{Q_\Delta^+,\ (S-1,E+z,\tau_1^+),
                  \ (S-2,E,\tau_2)\},\\
 \mathcal Y^-
 &=\{Q_\Delta^-,\ (S-1,E,\tau_1),
                  \ (S-2,E+z,\tau_2^+)\}.
\end{aligned}
\tag{4.7}
\]

The usual insertion calculation gives

\[
 P_RY_H=
 (\mathbf1_C+2e_1)+(e_2-e_1)=\mathbf1_H.
\tag{4.8}
\]

More importantly here, both raw shores in (4.7) are owner matchings.
The two star cores are signature-separated by labels $1,2$, and a star
owner cannot collide with an insertion owner because it would have to
contain the two disjoint $c$-cores $C$ and $S-u$, while
$2c>c+2=R$. The owner $H$ occurs in $\mathcal Y^+$ and nowhere
else.

Define, exactly as in the star-core obstruction note,

\[
 \mathcal B^+=\sum_{Q\in\mathcal Y^-}f(Q),
 \qquad
 \mathcal B^-=\sum_{Q\in\mathcal Y^+}f(Q)-e_H.
\tag{4.9}
\]

Both are simple $2M+3$-owner matchings with equal point degrees.

### Lemma 4.1 (complete bridge/star collision audit)

Every owner of either $\mathcal A^\pm$ contains $C_0$. No owner of
either star potential in (4.7) collides with an owner of
$\mathcal A^\pm$.

#### Proof

A star owner contains one of the cores $S-u$, which is disjoint from
$C_0$. If $c\ge4$, a collision would force a rank-$(c+2)$ owner to
contain their union of size

\[
 |C_0|+|S-u|=2c-1>c+2,
\]

which is impossible.

If $c=3$, equality of a bridge owner and a star owner would force the
star core $S-u$ to be the reduced triple in that bridge owner and would
force the star toggle $2$-window to be exactly $C_0$. The
nonadjacency condition imposed after (4.4) excludes precisely this last
possibility, in both the small and enlarged star cycles. $\square$

### Theorem 4.2 (genuine closed-rail common reserve)

Let

\[
 \boxed{R_H=e_H+\mathbf1_{\mathcal R_0}
       =\sum_{Q\in\mathcal A^+}f(Q).}
\tag{4.10}
\]

Then $R_H$ is a nonnegative simple $50$-owner vector, itself a union
of eight legal closed rails, and both

\[
 \boxed{\mathcal B^++R_H,\qquad \mathcal B^-+R_H}
\tag{4.11}
\]

are nonnegative sums of eleven pairwise owner-disjoint legal closed rails.
Explicitly,

\[
\begin{aligned}
 \mathcal B^++R_H
 &=\sum_{Q\in\mathcal Y^-}f(Q)
   +\sum_{Q\in\mathcal A^+}f(Q),\\
 \mathcal B^-+R_H
 &=\sum_{Q\in\mathcal Y^+}f(Q)
   +\sum_{Q\in\mathcal A^-}f(Q).
\end{aligned}
\tag{4.12}
\]

Both states contain exactly $2M+53$ owners. Their complete period
ledgers are

\[
\begin{array}{c|c|c}
\text{state}&\text{macro periods}&\text{bridge-reserve periods}\\ \hline
\mathcal B^++R_H&(6,M-2,M-1)&(6,6,7,7,6,6,6,6)\\
\mathcal B^-+R_H&(7,M-1,M-2)&(7,6,6,6,6,6,6,6).
\end{array}
\tag{4.13}
\]

#### Proof

The vector equalities in (4.12) follow from (2.4) and (4.9). Each
collection $\mathcal Y^\pm$ is simple by the signature/core argument
above, and each $\mathcal A^\pm$ is simple by Theorem 2.1. Equation
(4.3) handles every bridge/insertion collision in the corresponding
state: $\mathcal A^+$ meets the small insertion deck, whereas
$\mathcal A^-$ meets the large insertion deck. Lemma 4.1 handles every
bridge/star collision. Thus each right side of (4.12) is owner-disjoint.
All coefficients are one and all displayed periods are legal. Summing
the periods on either row of (4.13) gives $2M+53$. $\square$

This explicitly breaks the compulsory-owner character: the bridge rails
do not merely supply its missing residue; their $49$ collateral owners
are recoupled into the second positive rail decomposition (2.4).

## 5. Verification and exact scope

The dependency-free verifier

scratch/verify_near_c_bridge_q2_common_reserve_20260813.py

checks:

1. every cycle word, period, and full named-owner deck in both tables;
2. simplicity of both bridge collections;
3. the exact multiset identity (2.4), including all $49$ reserve owners;
4. disjointness from both insertion decks in (4.2); and
5. a full ground-set instance at the boundary $c=3,M=8$, including the
   star potentials and both $69$-owner common-reserve states.

The SHA-256 digest of the sorted reduced list (2.3), joined by single
spaces, is

\[
 \texttt{84698875b1b37bad70766904af764e31ebf00e8a3fa633b18152b46b04718d06}.
\tag{5.1}
\]

The theorem proves a true nonnegative common reserve in the first
nontrivial toggle width $q=2$. It does **not** prove a corresponding
certificate for $q\ge3$, compatibility with an arbitrary preselected
choice of the star macro, a global owner factor, upper-ticket preservation,
socket/common-cap preservation, or affine-semigroup normality. In
particular, no signed owner-lattice identity has been reinterpreted as a
positive decomposition.
