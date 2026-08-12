# MFUP by exact owner transversals and overlay-component descent

Date: 2026-07-25

Pure mathematics only. No generic probabilistic rounding theorem, finite
search, solver, or external input is used.

## 0. Outcome

Fix \(A>0\), put

\[
W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
H=\lceil A\sqrt m\rceil,
\]

and choose a power of two \(\ell\) with

\[
H=o(\ell),\qquad \ell=o(m),\qquad R=2\ell.
\tag{0.1}
\]

The mixed-frame useful-prefix theorem \(\mathrm{MFUP}_A\) is not proved in
this note. Two exact advances are proved.

First, there is no one-depth integral rounding obstruction. At any fixed
lower depth \(q\), the complete coordinate orbit of collared recursive
necklaces gives a biregular owner--target multigraph. Hall's theorem selects
exactly one occurrence for every middle owner while hitting **every**
rank-\((m-q)\) target. Thus fractional path-hitting at one depth rounds
integrally and exactly. What is missing is simultaneous use of the same
owner occurrences at all depths together with long packet runs.

Second, the complete simultaneous problem has an exact local reduction. A
necklace factor is an exact partition of the middle owners into long
recursive necklaces, apart from \(o(W/H)\) declared residual pieces. For
two such factors, every connected component of their block-overlay graph is
an exact owner-preserving trade. If one switches a component, the change in
the total path-hitting hole count is exactly

\[
\boxed{\Delta\operatorname{Hol}
=\operatorname{Loss}-\operatorname{Gain}.}
\tag{0.2}
\]

Here **Gain** counts previously missing signed targets hit by the incoming
side, and **Loss** counts targets whose only old hit lies in the outgoing
side and which the incoming side misses.

Consequently \(\mathrm{MFUP}_A\) follows from the following strictly local
combinatorial statement.

> **Overlay-component descent lemma \(\mathrm{OCD}_A\).** There is a
> sequence \(\varepsilon_m\downarrow0\) and an admissible finite class of
> long-necklace factors, closed under the permitted component switches, such
> that every factor \(F\) with
> \(\operatorname{Hol}(F)>\varepsilon_mW\) has a comparison factor \(G\)
> and one overlay component \(K\) satisfying
> \[
> \operatorname{Gain}_K(F,G)>\operatorname{Loss}_K(F,G).
> \]

This lemma mentions neither OR words, SCD colors, fractional vectors, nor a
global rounding algorithm. It is a one-component strict-improvement
inequality. A finite descent proof then constructs an exact mixed-frame
owner partition with \(o(W)\) aggregate holes. Since every intermediate
factor still consists of
\(O(W/R)+o(W/H)=o(W/H)\) long pieces, arbitrary hard useful-prefix
resets already have total excess \(o(W)\).

The note also audits why the usual shortcuts do not prove
\(\mathrm{OCD}_A\). Independent atom selection violates exact owner
partition; a one-depth Hall matching can fragment \(\Theta(W)\) packet
runs; and coordinate symmetry alone permits a whole fixed-frame factor with
the known positive Gaussian deficit. The remaining theorem is genuinely
the local gain--loss inequality above.

For odd \(n=2m+1\), use the exact wreath row

\[
X_j=I_\pi(j,m).
\]

A lower target \(T\) is hit at depth \(q\) exactly when one selected
consecutive \((q+1)\)-vertex Johnson path lies in its up-set

\[
\mathcal U_T=\{X:T\subseteq X,\ |X|=m\}.
\]

The intersection is then \(T\). Upper depth \(q\) is the complementary
lower depth \(q-1\), not lower depth \(q\). Nothing below assumes a converse
from arbitrary near-optimal OR words to singleton near-Ucycles.

## 1. Necklace occurrences and path-hit counts

Let \(\mathscr N\) be the finite multiset of all coordinate-labelled,
oriented, full-radius-\(H\) recursive necklaces under consideration. A
necklace \(B\in\mathscr N\) has a cyclic middle-owner set

\[
M(B)=\{X_0,\ldots,X_{R-1}\},
\qquad |M(B)|=R.
\tag{1.1}
\]

Every consecutive segment of at most \(H+1\) owners is geodesic. For a
lower target \(T\in\binom{[2m]}{m-q}\), define

\[
h^-_{T,B}
=\#\left\{i:
X_i,X_{i+1},\ldots,X_{i+q}\in\mathcal U_T
\right\}.
\tag{1.2}
\]

The recursive half-depth rainbow property gives

\[
h^-_{T,B}\in\{0,1\}
\tag{1.3}
\]

through \(q\le H\). Define \(h^+_{T,B}\) by reverse paths and
complementation. In the odd convention, its depth index is shifted as
described in Section 0.

A **collared owner factor** \(F\) is a collection of legal necklace pieces
whose middle-owner sets partition \(\binom{[2m]}m\). Main pieces are full
\(R\)-necklaces. A declared residual family is allowed provided its number
of pieces is \(o(W/H)\); every residual piece also carries one legal lower
and upper flag at every certified depth.

For a signed target \(S\), let

\[
c_S(F)=\sum_{B\in F}h_{S,B}
\tag{1.4}
\]

be its number of designated path hits. Put

\[
M_q^-(F)
=\#\left\{T\in\binom{[2m]}{m-q}:c_T^-(F)=0\right\},
\tag{1.5}
\]

and define \(M_q^+(F)\) similarly. The aggregate MFUP hole count is

\[
\operatorname{Hol}(F)
=\sum_{q=1}^H\bigl(M_q^-(F)+M_q^+(F)\bigr).
\tag{1.6}
\]

Every middle owner contributes exactly one designated lower and one
designated upper occurrence at each depth. Hence, for either sign,

\[
\sum_Tc_T(F)=W.
\tag{1.7}
\]

This gives an exact collision identity.

### Lemma 1.1 (holes are excess collisions above the forced floor)

For either sign and every \(q\le H\), define

\[
E_q^\pm(F)=\sum_T(c_T^\pm(F)-1)_+.
\tag{1.8}
\]

Then

\[
\boxed{
M_q^\pm(F)=E_q^\pm(F)-(W-N_q).}
\tag{1.9}
\]

Consequently

\[
\boxed{
\operatorname{Hol}(F)
=\sum_{q=1}^H(E_q^-(F)+E_q^+(F))
-2\sum_{q=1}^H(W-N_q).}
\tag{1.10}
\]

#### Proof

At one signed rank, let \(C\) be the set of targets with positive hit count.
Equation (1.7) gives

\[
E_q^\pm=\sum_{T\in C}(c_T^\pm-1)=W-|C|.
\]

Since \(M_q^\pm=N_q-|C|\), subtraction proves (1.9). Sum over signs and
depths to obtain (1.10). \(\square\)

Thus MFUP does not ask for collision-free shadows. The deterministic
baseline \(W-N_q\) repeats is unavoidable because there are \(W\) starts
and only \(N_q\) targets. It asks that the collision excess exceed this
floor by only \(o(W)\) after summing all depths.

## 2. One depth rounds exactly by Hall

Take the complete coordinate orbit of the collared recursive-necklace
multicover, with all labelled copies retained. Fix one lower depth \(q\).
Form a bipartite multigraph \(\Gamma_q\) as follows:

* the left vertices are middle owners \(X\in\binom{[2m]}m\);
* the right vertices are targets \(T\in\binom{[2m]}{m-q}\); and
* every labelled necklace occurrence at a center \(X\) contributes the edge
  \(XT\), where \(T\) is its depth-\(q\) forward path intersection.

Coordinate transitivity makes \(\Gamma_q\) biregular. Write its left and
right degrees as \(d_0\) and \(d_q\). Double counting gives

\[
Wd_0=N_qd_q,
\qquad d_q=\frac{W}{N_q}d_0\ge d_0.
\tag{2.1}
\]

### Theorem 2.1 (exact one-depth owner transversal)

There is a selection of exactly one labelled necklace occurrence at every
middle owner such that every rank-\((m-q)\) target is selected at least once.

#### Proof

Let \(\mathcal S\) be a set of right vertices and \(N(\mathcal S)\) its left
neighbourhood. Counting all edges incident with \(\mathcal S\) gives

\[
d_q|\mathcal S|
\le d_0|N(\mathcal S)|.
\]

By (2.1),

\[
|N(\mathcal S)|
\ge \frac{d_q}{d_0}|\mathcal S|
=\frac{W}{N_q}|\mathcal S|
\ge|\mathcal S|.
\]

Hall's theorem therefore gives a matching saturating every right vertex.
It uses \(N_q\) distinct middle owners. For every remaining middle owner,
choose an arbitrary incident edge. The resulting selection uses exactly
one occurrence per owner and retains the saturated matching edge at every
target. \(\square\)

The same theorem holds for one upper depth, with the odd shift when
appropriate.

### Exact scope

Theorem 2.1 is an integral statement, not an LP or expectation. It proves
that every individual path-hitting row has enough mixed-frame ownership
capacity. It does **not** prove MFUP for two reasons.

1. Applying Hall separately at different depths generally selects different
   occurrences of the same owner.
2. Even at one depth, the chosen owner occurrences may alternate at every
   position of every necklace, creating \(\Theta(W)\) runs and
   \(\Theta(HW)\) hard-prefix excess.

Thus the unresolved object is a simultaneous, run-coherent owner
transversal. There is no remaining one-depth Hall obstruction.

## 3. Long blocks make the bridge term automatic

Suppose every admissible owner factor \(F\) has at most

\[
C(F)\le \frac{W}{R}+r_m,
\qquad r_m=o(W/H),
\tag{3.1}
\]

pieces. Order them arbitrarily and independently initialize the useful
radius-\(H\) prefix at every piece. The exact hard-reset excess is at most

\[
\operatorname{Br}(F)\le2HC(F).
\tag{3.2}
\]

By (0.1) and (3.1),

\[
\boxed{
\operatorname{Br}(F)
\le \frac{2HW}{R}+o(W)
=\frac{HW}{\ell}+o(W)=o(W).}
\tag{3.3}
\]

Therefore, inside any class satisfying (3.1), MFUP reduces exactly to

\[
\operatorname{Hol}(F)=o(W).
\tag{3.4}
\]

No optimization of useful-prefix compatibility is needed. The only danger
is fragmentation into too many short pieces, which is why ownerwise Hall
selection in Theorem 2.1 cannot simply be compiled.

## 4. Exact owner-preserving overlay trades

Let \(F\) and \(G\) be two collared owner factors. Form their bipartite
block-overlay graph \(\mathcal O(F,G)\): its left vertices are the pieces of
\(F\), its right vertices are the pieces of \(G\), and a left and right piece
are adjacent when their middle-owner sets intersect.

For a connected component \(K\) of \(\mathcal O(F,G)\), write \(F_K\) and
\(G_K\) for its two block families.

### Lemma 4.1 (overlay components are exact trades)

For every component \(K\),

\[
\boxed{
\bigcup_{B\in F_K}M(B)=\bigcup_{B\in G_K}M(B).}
\tag{4.1}
\]

Consequently

\[
F\triangleleft_KG:=(F\setminus F_K)\cup G_K
\tag{4.2}
\]

is again an exact middle-owner partition.

#### Proof

Take an owner \(X\) in the left union. Its unique \(G\)-piece meets its
unique \(F\)-piece at \(X\), so both pieces lie in the same overlay component.
Thus \(X\) lies in the right union. The reverse inclusion is identical.
Replacing one partition of this common owner set by the other preserves
exact ownership there and changes nothing outside it. \(\square\)

This is the exact mechanism by which frames may become owner-dependent.
Switching a whole comparison factor is unnecessary; one may switch any
overlay component independently.

## 5. Exact gain--loss formula

Fix \(F,G\) and an overlay component \(K\). For every signed target \(S\),
write

\[
a_S=\sum_{B\in F\setminus F_K}h_{S,B},\qquad
u_S=\sum_{B\in F_K}h_{S,B},\qquad
v_S=\sum_{B\in G_K}h_{S,B}.
\tag{5.1}
\]

Define

\[
\operatorname{Gain}_K(F,G)
=\#\{S:a_S=0,\ u_S=0,\ v_S>0\},
\tag{5.2}
\]

\[
\operatorname{Loss}_K(F,G)
=\#\{S:a_S=0,\ u_S>0,\ v_S=0\},
\tag{5.3}
\]

where \(S\) ranges over all signed targets at depths \(1,\ldots,H\).

### Theorem 5.1 (exact component-switch derivative)

\[
\boxed{
\operatorname{Hol}(F\triangleleft_KG)-\operatorname{Hol}(F)
=\operatorname{Loss}_K(F,G)-\operatorname{Gain}_K(F,G).}
\tag{5.4}
\]

#### Proof

Before the switch, target \(S\) is a hole precisely when \(a_S+u_S=0\).
Afterward it is a hole precisely when \(a_S+v_S=0\).

If \(a_S>0\), it is covered both before and after. If \(a_S=0\), the
indicator increases exactly in the case \(u_S>0,v_S=0\), counted by
\(\operatorname{Loss}\), and decreases exactly in the case
\(u_S=0,v_S>0\), counted by \(\operatorname{Gain}\). All other cases have
zero change. Summing the indicator changes proves (5.4). \(\square\)

No independence, concentration, negative dependence, or approximation is
hidden in (5.4). It is an identity for one finite trade.

## 6. The localized successor lemma

Let \(\mathfrak F_m\) be a nonempty finite class of admissible collared owner
factors satisfying the long-piece bound (3.1). It may, for example, be the
closure of a collection of coordinate-conjugated fixed-frame recursive
factors under those overlay-component switches which preserve (3.1).

### Overlay-component descent lemma \(\mathrm{OCD}_A\)

There is a sequence \(\varepsilon_m\downarrow0\) such that, for every
\(F\in\mathfrak F_m\) with

\[
\operatorname{Hol}(F)>\varepsilon_mW,
\tag{6.1}
\]

there are \(G\in\mathfrak F_m\) and a component \(K\) of
\(\mathcal O(F,G)\) for which

\[
F\triangleleft_KG\in\mathfrak F_m,
\qquad
\boxed{\operatorname{Gain}_K(F,G)>\operatorname{Loss}_K(F,G).}
\tag{6.2}
\]

### Theorem 6.1 (\(\mathrm{OCD}_A\) implies \(\mathrm{MFUP}_A\))

If \(\mathrm{OCD}_A\) holds, then an admissible factor \(F_*\) satisfies

\[
\operatorname{Hol}(F_*)\le\varepsilon_mW=o(W),
\qquad
\operatorname{Br}(F_*)=o(W).
\tag{6.3}
\]

Hence the exact direct compiler gives a contiguous-OR word of length

\[
W+o(W)
\tag{6.4}
\]

covering the fixed central band.

#### Proof

Start from any \(F_0\in\mathfrak F_m\). If (6.1) holds, apply
\(\mathrm{OCD}_A\). Equations (5.4) and (6.2) decrease the nonnegative
integer \(\operatorname{Hol}\) by at least one. Every new factor remains in
the finite class \(\mathfrak F_m\). Therefore the descent terminates, and
it can terminate only at a factor \(F_*\) satisfying the first part of
(6.3).

The long-piece bound and (3.3) give the bridge estimate. Substitution in
the exact useful-prefix compiler proves (6.4). \(\square\)

This is a genuine globalization theorem: proving the one-component
inequality (6.2) automatically coordinates all depths and both signs by
finite descent. The lemma is sufficient, not claimed necessary; MFUP might
also hold in a factor class containing bad component-switch local minima.

## 7. What a proof of the descent lemma must use

The fractional orbit equations alone do not imply (6.2). Three tempting
arguments fail for exact reasons.

### 7.1 Independent necklace selection

Selecting orbit necklaces independently does not preserve the middle-owner
partition. Even before that defect is repaired, a target of fractional load
\(\mu_q=W/N_q=O_A(1)\) has Poisson-scale miss probability, so summing over
\(\Theta(W\sqrt m)\) signed target rows gives far more than \(o(W)\) holes.

### 7.2 Independent overlay-component choices

For fixed \(F,G\), choosing the \(F\)- or \(G\)-side independently in every
overlay component does preserve exact middle ownership by Lemma 4.1. This
does not by itself give a useful estimate. A target hit on only one side of
only one component is missed with probability \(1/2\); bounded fractional
load therefore again permits a constant miss probability. If the overlay
graph is connected, this experiment merely chooses all of \(F\) or all of
\(G\).

### 7.3 Coordinate symmetry and separate Hall choices

A uniformly relabelled fixed-frame factor is coordinate symmetric and is an
exact middle partition in every realization, yet every realization retains
the positive fixed-frame Gaussian deficit. Symmetry is therefore not a
substitute for (6.2).

Likewise, Theorem 2.1 solves each depth with a different owner transversal.
There is no audited exchange showing that those transversals can be made
common while retaining long runs. Invoking Hall separately and then
identifying the choices is invalid.

### 7.4 The exact local quantity

For an overlay component, the targets contributing to **Loss** are not all
targets hit by \(F_K\). They are only those with no hit outside \(K\) and no
incoming hit from \(G_K\). Thus a proof must exploit overlap of the old and
new path-hit families, not merely compare their equal total sizes. The
required inequality is the concrete expansion statement

\[
\#\{\text{newly filled global holes}\}
>
\#\{\text{globally unique hits destroyed}\}.
\tag{7.1}
\]

This is where the nested consecutive-path geometry and the local
coordinate-frame change must enter.

## 8. Exact theorem ledger

### Proved

1. At each fixed depth and sign, mixed-frame path-hitting has an exact
   integral owner transversal by a direct Hall argument.
2. Aggregate holes equal collision excess above the unavoidable rank floor,
   equation (1.10).
3. Long full-necklace factors automatically have \(o(W)\) bridge excess;
   no prefix scheduling theorem is needed for them.
4. Every overlay component of two exact owner factors is an exact
   owner-preserving frame trade.
5. The hole change under such a trade is exactly **Loss-Gain**.
6. The local descent lemma \(\mathrm{OCD}_A\) implies \(\mathrm{MFUP}_A\)
   by finite integer descent.

### Still open

1. The gain--loss inequality (6.2) for a concrete long-necklace factor
   class.
2. A construction of sufficiently rich small or mesoscopic overlay
   components under local coordinate-frame changes.
3. Simultaneous lower/upper and multidepth control inside the same component
   switches.
4. The coefficient-one theorem itself.

The live problem is therefore smaller than generic integral rounding:
construct one profitable owner-preserving overlay component whenever the
current aggregate hole potential is macroscopic. Every other part of the
MFUP compiler—one-depth capacity, exact owner preservation, and bridge
accounting—is already resolved.
