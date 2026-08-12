# Logarithmic Kneser augmenters: the terminal-star Hall cut and a critical-scale poisoned state

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let

\[
 \Omega=[2m],\qquad
 \mathcal L=\binom{\Omega}{m-1},\qquad
 \mathcal P=\binom{\Omega}{m}/(X\sim X^c),
\]

\[
 W=\binom{2m}{m},\qquad
 N=\binom{2m}{m-1},\qquad
 D=W-N={W\over m+1}.                                         \tag{0.1}
\]

The proposed correlation-robust statement

\[
 \text{“every uncovered \(R\) has an eligible augmenter at
 \(t\sim\log_2m\)”}                                           \tag{0.2}
\]

is false for arbitrary critical-density states.  The obstruction is
already present in the two terminal owner resources and is independent
of the \(t\) old-edge correlations.

For \(R\in\mathcal L\), define its terminal owner star

\[
 \Sigma(R)=\{[R+h]:h\in\Omega\setminus R\}.                   \tag{0.3}
\]

It has only \(m+1\) owner-pairs.  Every all-intersection augmenter from
Theorem 2.3 of
MATH_THEOREM_KNESER_ZERO_SIGNATURE_HEXAGON_AND_CRITICAL_AUGMENTER_20260726.md
which starts at \(R\) consumes a free clone at one member of
\(\Sigma(R)\).  Consequently

\[
 \boxed{\Sigma(R)\text{ saturated }\Longrightarrow
        \text{no eligible augmenter from \(R\), at any depth.}}       \tag{0.4}
\]

The raw census does not disperse this bottleneck.  For every
\(0\le t\le m-2\) and every fixed \(h\notin R\), the number of depth-\(t\)
templates whose \(R\)-terminal is \([R+h]\) is exactly

\[
 \mathsf A_{t,h}(R)=(m-1)_t(m)_{t+1}
                  ={1\over m+1}\mathsf A_t(R).                \tag{0.5}
\]

Thus the \(m+1\) terminal resources form a hitting set for all
\(\mathsf A_t(R)\) templates, uniformly in \(t\).  The exponential factor
\(2^t\) in the normalized census does not overcome a terminal star with
zero slack.

This is not merely a formal degree vector.  For every \(m\ge4\) and every
\(R\), Section 3 constructs a literal auxiliary matching of
\(2(m+1)\) Kneser edges which

* leaves \(R\) uncovered;
* saturates every member of \(\Sigma(R)\);
* has folded owner degree at most two everywhere.

Moreover, this gadget can be implanted into **any** feasible common
matching after changing only \(O(m)\) edges.  Therefore:

> If a critical-size feasible common matching exists, then another
> feasible common matching at the same \(u=\Theta(D)\) scale exists with
> an uncovered \(R\) having no eligible all-intersection augmenter of any
> length.

Equivalently, either the critical common-factor theorem itself is false,
or the universal per-owner logarithmic supersaturation theorem (0.2) is
false.  In neither case can (0.2) be the proof of CR.

The exact simultaneous obstruction is a bipartite Hall cut.  Join an
uncovered lower vertex \(R\) to every currently free clone in
\(\Sigma(R)\).  Any family of disjoint all-intersection augmenters
absorbing a set \(\mathcal A\) of uncovered vertices requires

\[
                         |\Gamma(\mathcal A)|\ge|\mathcal A|. \tag{0.6}
\]

The constructed state violates the singleton cut
\(\Gamma(\{R\})=\varnothing\).  At critical density the total terminal
incidence is only constant on average:

\[
 {1\over N}\sum_{R\in\mathcal L}\deg_{\widetilde B_F}(R)
 ={2m(D+u)\over N}=\Theta(1) \qquad(u=\Theta(D)).              \tag{0.7}
\]

Thus global lower/clone densities \(\Theta(1/m)\) cannot force (0.6).
A positive CR proof must either maintain terminal Hall expansion as an
invariant, or first route owner slack into deficient terminal stars using
nonzero-signature switches.  Zero-signature hexagons preserve the
obstruction exactly.

## 1. Exact terminal-link census

Fix \(R\in\mathcal L\), \(0\le t\le m-2\), and
\(h\in\Omega\setminus R\).  Let \(\mathcal A_{t,h}(R)\) be the family of
ordered depth-\(t\) augmenters of Theorem 2.3 whose other endpoint is
\(S\) and whose distinguished omitted coordinate is \(h\).  Necessarily

\[
                         |R\cap S|=t,\qquad h\notin S.         \tag{1.1}
\]

### Proposition 1.1 (exact link of one terminal owner)

For every such \(R,t,h\),

\[
 |\mathcal A_{t,h}(R)|
  =\binom{m-1}{t}\binom m{t+1}t!(t+1)!
  =(m-1)_t(m)_{t+1}.                                         \tag{1.2}
\]

Consequently

\[
                         |\mathcal A_{t,h}(R)|
                         ={\,\mathsf A_t(R)\over m+1}.         \tag{1.3}
\]

#### Proof

Choose the intersection \(R\cap S\) in
\(\binom{m-1}{t}\) ways.  Outside \(R\), the set \(S\) must use
\(m-1-t\) points from the \(m\)-set
\(\Omega\setminus(R\cup\{h\})\), giving

\[
 \binom m{m-1-t}=\binom m{t+1}                               \tag{1.4}
\]

choices.  Once \(R,S,h\) are fixed, Theorem 2.3 has
\(t!(t+1)!\) oriented identifications.  This proves (1.2).
Finally,

\[
 (m+1)(m)_{t+1}=(m+1)_{t+2},                                \tag{1.5}
\]

and the asserted total census is
\(\mathsf A_t(R)=(m-1)_t(m+1)_{t+2}\).  This gives (1.3).
\(\square\)

### Corollary 1.2 (terminal-star hitting)

Let \(F\) be any auxiliary matching and let \(R\) be uncovered.  If every
owner-pair in \(\Sigma(R)\) has load two in \(F\), then no augmenter of
Theorem 2.3 starting at \(R\) is eligible, for any
\(0\le t\le m-2\).

#### Proof

The exact signature of every such augmenter contains
\(\mathbf e_{[R+h]}\) for its distinguished
\(h\in\Omega\setminus(R\cup S)\).  This is a member of \(\Sigma(R)\).
Eligibility requires a free clone there, contrary to saturation.
\(\square\)

The obstruction is therefore insensitive to the old-edge supply.  Even
if all \(t\) prescribed old edges occur for an enormous number of
templates, the terminal link can delete every one of them.

## 2. The terminal Hall graph

Let \(F\) be a common matching: a Kneser matching whose folded Johnson
degree is at most two.  Let

\[
 \mathcal U=\{R\in\mathcal L:d_K^F(R)=0\}                     \tag{2.1}
\]

be its uncovered lower set.  Give every unused owner clone its own token,
and let \(\mathcal C_{\rm free}\) be the token set.  Define a bipartite
graph

\[
                         B_F=(\mathcal U,\mathcal C_{\rm free}) \tag{2.2}
\]

by joining \(R\) to a free clone of \(P\) exactly when

\[
                         P=[R+h]\quad\text{for some }h\notin R. \tag{2.3}
\]

Also let \(\widetilde B_F\) denote the same incidence graph with the full
left shore \(\mathcal L\), rather than only \(\mathcal U\).

### Theorem 2.1 (necessary Hall condition for simultaneous augmentation)

Suppose a collection of capacity-compatible all-intersection augmenters
absorbs every endpoint in \(\mathcal A\subseteq\mathcal U\).  Then

\[
                         |\Gamma_F(\mathcal A)|\ge|\mathcal A|. \tag{2.4}
\]

In particular, every individually augmentable \(R\) must have
\(\deg_{B_F}(R)\ge1\).

#### Proof

For each absorbed endpoint \(R\), the signature identity (2.15) in the
augmenter theorem consumes one previously free clone at
\([R+h]\in\Sigma(R)\).  Cancelled internal resources retain their old
clones and no terminal clone is released.  Capacity compatibility makes
the consumed clone tokens distinct for distinct endpoint occurrences.
Assigning each \(R\in\mathcal A\) its consumed token is therefore a
matching from \(\mathcal A\) into \(\Gamma_F(\mathcal A)\), which proves
(2.4). \(\square\)

### Proposition 2.2 (exact total terminal incidence)

If \(F\) leaves \(u\) lower vertices uncovered, then it has exactly
\(D+u\) free owner clones and

\[
             \sum_{R\in\mathcal L}
                 \deg_{\widetilde B_F}(R)
                    =2m(D+u).                                \tag{2.5}
\]

#### Proof

The clone shore has \(W\) vertices.  Since \(F\) has
\((N-u)/2\) edges and every auxiliary edge uses two clones, its unused
clone count is

\[
                         W-(N-u)=D+u.                         \tag{2.6}
\]

A clone of \(P=[X]\) is adjacent in \(\widetilde B_F\) to the \(m\) lower facets of
\(X\) and the \(m\) lower facets of \(X^c\).  These \(2m\) lower sets are
distinct.  Summing over free clone tokens proves (2.5). \(\square\)

Equation (2.5) is over the whole lower layer, not just over the uncovered
set.  Slack may place all of its terminal incidence on already covered
lower vertices.  Even its global average is only

\[
 {2m(D+u)\over N}=2\left(1+{u\over D}\right)                 \tag{2.7}
\]

when \(u=O(D)\).  Hence neither the singleton Hall inequalities nor their
family versions follow from total slack.

## 3. A literal saturated-terminal gadget

Assume \(m\ge4\), fix \(R\in\mathcal L\), and put

\[
                         C=\Omega\setminus R,\qquad |C|=m+1.  \tag{3.1}
\]

Choose a cyclic ordering

\[
                         C=\{c_i:i\in\mathbb Z_{m+1}\}        \tag{3.2}
\]

and two distinct points \(r_0,r_1\in R\).  For every
\(i\in\mathbb Z_{m+1}\), define four lower vertices

\[
\begin{aligned}
 A_{i,0}&=R-r_0+c_i,&
 B_{i,0}&=C\setminus\{c_i,c_{i+1}\},\\
 A_{i,1}&=R-r_1+c_i,&
 B_{i,1}&=C\setminus\{c_i,c_{i+2}\},
\end{aligned}                                                \tag{3.3}
\]

and the two Kneser edges

\[
                         e_{i,j}=\{A_{i,j},B_{i,j}\},
                         \qquad j\in\{0,1\}.                  \tag{3.4}
\]

### Theorem 3.1 (saturated-terminal poison)

The \(2(m+1)\) edges in (3.4) form a Kneser matching.  Their folded owner
resources are

\[
 P_i=[R+c_i],\qquad
 Q_{i,0}=[R-r_0+c_i+c_{i+1}],\qquad
 Q_{i,1}=[R-r_1+c_i+c_{i+2}],                                \tag{3.5}
\]

with resource multiset

\[
                         \biguplus_i\{P_i,Q_{i,0}\}
                         \uplus
                         \biguplus_i\{P_i,Q_{i,1}\}.          \tag{3.6}
\]

All \(3(m+1)\) owner-pairs in (3.5) are distinct.  Consequently the
folded loads are

\[
                         d(P_i)=2,\qquad d(Q_{i,j})=1,        \tag{3.7}
\]

and zero elsewhere.  The lower vertex \(R\) is uncovered, while

\[
                         \Sigma(R)=\{P_i:i\in\mathbb Z_{m+1}\} \tag{3.8}
\]

is saturated.  Hence \(R\) has no eligible all-intersection augmenter of
any length.

#### Proof

Each \(A_{i,j}\) has size \(m-1\), contains \(c_i\), and otherwise lies
in \(R\).  The corresponding \(B_{i,j}\) lies in \(C\) and omits \(c_i\),
so the two endpoints of every \(e_{i,j}\) are disjoint.

The \(A_{i,j}\)'s are pairwise distinct: their added point recovers \(i\),
and their missing point then recovers \(j\).  The sets
\(\{c_i,c_{i+1}\}\) and \(\{c_i,c_{i+2}\}\), as \(i\) varies, are
\(2(m+1)\) distinct unordered pairs for \(m+1\ge5\).  Thus all
\(B_{i,j}\)'s are distinct.  No \(A_{i,j}\) equals a \(B_{k,\ell}\),
because the former contains \(m-2\ge2\) points of \(R\) and the latter
contains none.  Therefore (3.4) is a Kneser matching.

Relative to the middle set \(X_i=R+c_i\), the edge \(e_{i,0}\) is the
cell \((r_0,c_{i+1})\) and \(e_{i,1}\) is the cell
\((r_1,c_{i+2})\).  Their resource pairs are exactly those in (3.5).

The \(P_i\)'s are distinct.  No \(P_i\) equals a \(Q_{k,j}\), because
their displayed representatives contain respectively \(m-1\) and
\(m-2\) points of \(R\); equality with a complement is also impossible.
Within one \(j\)-class, the omitted cyclic pairs are distinct.  Between
the two classes, the representatives omit different points \(r_0,r_1\)
of \(R\).  Finally, a displayed \(Q\)-representative contains \(m-2\)
points of \(R\), whereas the complement of another contains exactly one
point of \(R\); these cannot agree for \(m\ge4\).  Hence all owner-pairs
in (3.5) are distinct, proving (3.6)--(3.7).

None of the lower vertices in (3.3) is \(R\), and (3.8) follows directly
from the definition of \(P_i\).  Corollary 1.2 finishes the proof.
\(\square\)

## 4. Implanting the obstruction at critical density

The preceding gadget is local.  It can be imposed on an arbitrary common
matching at only polynomial cost.

### Theorem 4.1 (critical-scale poisoning)

Let \(F\) be any common matching satisfying

\[
                         d_K^F\le1,\qquad d_{J^\pm}^F\le2.     \tag{4.1}
\]

For every prescribed \(R\in\mathcal L\), there is another common matching
\(F_R\) such that

\[
                         |F_R|\ge |F|-8(m+1)-1,               \tag{4.2}
\]

and also

\[
                         |F_R|\le |F|+2(m+1).                 \tag{4.2a}
\]

It also satisfies

\[
                         d_K^{F_R}(R)=0,\qquad
                         d_{J^\pm}^{F_R}(P)=2
                         \quad(P\in\Sigma(R)).                \tag{4.3}
\]

Thus \(R\) is uncovered and has no eligible all-intersection augmenter.

#### Proof

Let \(G_R\) be the matching from Theorem 3.1.  Its lower support has
\(4(m+1)\) vertices and its folded owner support has \(3(m+1)\) vertices.

Starting from \(F\), delete every selected edge which

1. is incident in \(K\) with a lower vertex of \(G_R\) or with \(R\); or
2. is incident in \(J^\pm\) with an owner-pair used by \(G_R\).

Because \(F\) is a Kneser matching, the first rule deletes at most
\(4(m+1)+1\) edges.  Because its folded degrees are at most two, the
second rule deletes at most \(6(m+1)\) further edges.  At most
\(10(m+1)+1\) edges are therefore deleted in total.

Now insert all \(2(m+1)\) edges of \(G_R\).  The deletion rules remove
every lower or folded-owner conflict with the gadget, so the result is a
common matching.  It satisfies (4.3) by Theorem 3.1, and

\[
 |F_R|\ge |F|-\bigl(10(m+1)+1\bigr)+2(m+1)
          =|F|-8(m+1)-1,                                    \tag{4.4}
\]

which proves (4.2).  If this insertion happens to increase cardinality,
it increases it by at most the \(2(m+1)\) inserted edges, proving
(4.2a). \(\square\)

### Corollary 4.2 (failure of universal critical supersaturation)

Assume there is a sequence of feasible common matchings \(F_m\) with

\[
                         u(F_m)=O(D).                         \tag{4.5}
\]

Then there is another sequence \(F'_m\) with

\[
                         u(F'_m)=\Theta(D)                    \tag{4.6}
\]

and prescribed uncovered vertices \(R_m\) such that no \(R_m\) starts an
eligible augmenter of Theorem 2.3 at any depth.

#### Proof

Apply Theorem 4.1 and use the matching exactly as constructed.
Equations (4.2) and (4.2a) show that its uncovered count differs from
\(u(F_m)\) by only \(O(m)\), and hence remains \(O(D)\).
If it is smaller than \(D\), delete non-gadget edges until the uncovered
count lies in \([D,D+2]\).  There are enough such edges because the
matching has \(\Theta(W)\) edges whereas \(D=o(W)\).  These deletions do
not alter the saturated gadget pairs.  The resulting uncovered count is
\(\Theta(D)\), proving (4.6).  Equation (4.3) and Corollary 1.2 give the
final assertion. \(\square\)

This proves the announced dichotomy.  If no sequence in (4.5) exists,
then the owner part of CR already fails.  If one exists, universal
per-owner augmenter supersaturation fails by Corollary 4.2.

## 5. Consequences for the exact CR gate

The logarithmic census remains useful, but only after a new terminal-Hall
invariant is supplied.  A valid positive statement must include at least

\[
                         |\Gamma_F(\mathcal A)|\ge|\mathcal A|-O(D)
                         \qquad(\mathcal A\subseteq\mathcal U), \tag{5.1}
\]

and a second condition pairing endpoints that can use a common omitted
coordinate \(h\).  Neither follows from

\[
                         |\mathcal U|=\Theta(W/m),\qquad
                         |\mathcal C_{\rm free}|=\Theta(W/m). \tag{5.2}
\]

The old-edge condition along the \(t\)-step alternating path is an
additional gate after (5.1); the present obstruction occurs before it.

Zero-signature hexagons do not help with (0.4), because they preserve
every folded owner degree and hence preserve the terminal Hall graph.
Elementary rectangles or longer nonzero-signature switches can move
clone slack between owner-pairs, but then CR needs a joint
slack-routing/augmentation theorem rather than an augmenter
supersaturation theorem alone.

Accordingly the exact successor is:

> Construct a near-perfect common matching while maintaining terminal
> Hall expansion, or prove that any terminal Hall violation admits a
> capacity-legal nonzero-signature switch which decreases a Hall-defect
> potential.

Without one of these two statements, the factor
\(2^t\) at \(t\sim\log_2m\) is neutralized by the \(m+1\)-point terminal
hitting set \(\Sigma(R)\), and the exact all-intersection augmenter
hierarchy cannot by itself prove CR.

The poisoned construction concerns a prescribed endpoint and therefore
does not rule out a weaker theorem asserting eligibility for all but
\(O(D)\) uncovered vertices.  Such a quarantine is sufficient for CR.
What has been ruled out is the requested every-owner supersaturation and
any proof that derives it from the two global residual densities alone.
