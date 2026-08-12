# Global necklace rewiring: exact orbit scales, a two-orbit root-star atlas, and the remaining positive-resolution gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, or external input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad k=m-H,\qquad M=m+H,
\]

\[
 W=\binom{2m}{m},\qquad
 N_H=\binom{2m}{m-H},
\]

and assume

\[
 H=(1+o(1))\sqrt{m\log m}
\]

together with the exact critical calibration

\[
 \theta:={MN_H\over W}=1+o(1).
\tag{0.0}
\]

The second assumption is genuinely needed: the displayed first-order
asymptotic for \(H\) by itself permits a subpolynomial deviation of
\(\theta\) from one.

A root is \(A\in\binom{[n]}k\). A directed cyclic frame on
\(U_A=[n]\setminus A\), taken modulo rotation, has middle deck

\[
 {\cal D}(A,\pi)
 =\{A\cup I_\pi(i,H):i\in{\mathbb Z}_M\}.
\tag{0.1}
\]

For a middle target \(D\in\binom{[n]}m\), the compatible-root star and
the one-root uniform hit probability are

\[
 {\cal R}(D)=\{A\in\tbinom Dk\},\qquad
 R:=|{\cal R}(D)|=\binom mH,
\tag{0.2}
\]

\[
 p={M\over\binom MH},\qquad
 Rp=\theta={MN_H\over W}.
\tag{0.3}
\]

This note determines exactly what necklace-group orbits can and cannot
do at the necessary \(R=\binom mH\) correlation scale.

1. Let \(C_n\) be the cyclic coordinate group and let
   \(N_{S_n}(C_n)\) be its full normalizer. Its root orbits have sizes at
   most

   \[
   n\varphi(n)<n^2=o(R).
   \tag{0.4}
   \]

   The orbit of one directed master cycle, modulo rotation, has exactly
   \(\varphi(n)\) members. Any frame system obtained by restricting those
   master cycles covers at most

   \[
   n\varphi(n)2^{-H}W=o(W)
   \tag{0.5}
   \]

   middle targets, even when the choice of master cycle at every root is
   made by one arbitrary global rule.

2. If choices attached to different necklace-normalizer root orbits are
   independent, arbitrary dependence being allowed inside one orbit,
   then their expected number of middle holes is at least

   \[
   (e^{-1}-o(1))W.
   \tag{0.6}
   \]

   More generally, a successful component-product construction must,
   for all but \(o(W)\) targets \(D\), contain in one component

   \[
   {1-o(1)\over p}=(1-o(1))R
   \tag{0.7}
   \]

   roots of \({\cal R}(D)\). Hence that component must join at least

   \[
   (1-o(1)){R\over n\varphi(n)}
   \tag{0.8}
   \]

   distinct normalizer orbits meeting \(D\). Ordinary necklace symmetry
   therefore cannot furnish the required correlation; a successful
   rewiring must cross a superpolynomial number of its orbits.

3. There is no orbit-size obstruction to a genuinely global
   coordinate rewiring. For every fixed \(D\), its set stabilizer

   \[
   K_D=S_D\times S_{D^c}
   \tag{0.9}
   \]

   has one root orbit equal exactly to \({\cal R}(D)\), of size \(R\).
   Still more concretely, fix one coordinate \(x\). The group
   \(G_x=S_{[n]\setminus\{x\}}\) splits the entire rooted-frame catalogue
   into exactly two orbits:

   \[
   {\cal A}_1=\{A:x\in A\},\qquad
   {\cal A}_0=\{A:x\notin A\},
   \tag{0.10a}
   \]

   \[
   {\cal C}_1=\{(A,\pi):A\in{\cal A}_1\},\qquad
   {\cal C}_0=\{(A,\pi):A\in{\cal A}_0\}.
   \tag{0.10}
   \]

   Their exact sizes are

   \[
   |{\cal C}_1|
   =\binom{n-1}{k-1}(M-1)!,
   \qquad
   |{\cal C}_0|
   =\binom{n-1}{k}(M-1)!.
   \tag{0.11}
   \]

   If \(x\notin D\), all \(R\) compatible roots lie in \({\cal A}_0\).
   If \(x\in D\), then

   \[
   |{\cal R}(D)\cap{\cal A}_1|
      =\binom{m-1}{H}={m-H\over m}R,
   \tag{0.12}
   \]

   \[
   |{\cal R}(D)\cap{\cal A}_0|
      =\binom{m-1}{H-1}={H\over m}R.
   \tag{0.13}
   \]

   Thus the root projection of one of two global catalogue orbits
   contains at least \((1-H/m)R=(1-o(1))R\) compatible roots for every
   target. This is an explicit cross-necklace orbit-capacity architecture
   at the necessary scale. It is not yet a switching component.

4. The two-orbit architecture is not yet a middle near-factor. Group
   orbit averaging only permutes the load vector of a seed resolution
   and therefore preserves its exact numbers of holes and repetitions.
   Even if the two orbits are moved by independent uniform group
   elements, Theorem 7.1 below shows that their expected hole count is
   \(o(W)\) if and only if the dominant support in each half-layer is
   already \(W/2-o(W)\); the cross-class spill has support at most
   \(\theta(H/m)W/2=o(W)\).
   What remains is a positive integral resolution inside the two global
   catalogue orbits, with the small \({H/m}\)-spill in (0.13) assigned
   coherently, followed by the simultaneous nested shorter-window
   resolution. This is a strictly sharper gate than an orbit-size or
   marginal question.

The final verdict is therefore a dichotomy. Necklace-axis groups cannot
provide the needed correlation scale. Global cross-necklace coordinate
groups do have root projections large enough to provide it, but their
catalogue orbits are not automatically legal switching components. The
surviving obstruction is positive owner-preserving simultaneous
resolution, not raw group-orbit size.

## 1. Exact root-star parameters

Fix \(D\in\binom{[n]}m\). A root frame can contain \(D\) only when
\(A\subset D\), and then \(J=D\setminus A\) has size \(H\). Conversely,
if \(A\subset D\) and \(J\) is an \(H\)-window of the frame on \(A^c\),
then the corresponding deck member is \(D\). Hence (0.2) is exact.

There are \((M-1)!\) directed cyclic frames on an \(M\)-set. The number
in which a fixed \(H\)-set is a window is

\[
 H!(M-H)!=H!m!.
\tag{1.1}
\]

Indeed contract the \(H\)-set to one cyclic block, order its entries in
\(H!\) ways, and cyclically order that block with the remaining \(m\)
points in \(m!\) ways. Therefore

\[
 p={H!m!\over(M-1)!}
   ={M\over\binom MH}.
\tag{1.2}
\]

Finally,

\[
 {R\over\binom MH}
 ={m!^2\over(m-H)!(m+H)!}
 ={N_H\over W},
\tag{1.3}
\]

which proves the exact identity \(Rp=MN_H/W=\theta\).

At the critical height, the standard factorial expansion gives

\[
 \log{1\over p}
 =\left({1\over2}+o(1)\right)
   \sqrt m\,(\log m)^{3/2},
\tag{1.4}
\]

so every polynomial in \(m\) is \(o(1/p)\) and \(o(R)\).

## 2. The component threshold, with its exact quantifiers

The following form is useful because it measures intersection with a
target star rather than total component size.

### Theorem 2.1 (targetwise independent-component hole floor)

Partition the roots into blocks \({\cal B}_1,\ldots,{\cal B}_s\).
Inside each block choose all frames by an arbitrary joint law. Assume
different blocks are independent and every individual root frame has the
uniform marginal. For a fixed middle target \(D\), put

\[
 r_j(D)=|{\cal B}_j\cap{\cal R}(D)|,\qquad
 \alpha_D=p\max_j r_j(D).
\tag{2.1}
\]

If \(\alpha_D<1\), then

\[
 \Pr(D\hbox{ is missed})
 \ge
 \exp\left(-{\theta\over1-\alpha_D}\right).
\tag{2.2}
\]

Consequently, if the law is supported on selections with \(o(W)\)
middle holes, then for every fixed \(\eta>0\), all but \(o(W)\) targets
\(D\) satisfy

\[
 \max_j r_j(D)>{1-\eta\over p}.
\tag{2.3}
\]

After a diagonal choice \(\eta=\eta_m\downarrow0\), this is

\[
 \max_j r_j(D)\ge {1-o(1)\over p}
                 =(1-o(1))R
\tag{2.4}
\]

for all but \(o(W)\) targets, where the last equality uses
\(\theta=Rp=1+o(1)\).

#### Proof

For \(A\in{\cal R}(D)\), let \(X_{A,D}\) indicate that the frame at
\(A\) contains \(D\), and set

\[
 Y_{j,D}=\sum_{A\in{\cal B}_j\cap{\cal R}(D)}X_{A,D}.
\]

Uniform marginals give

\[
 \mu_j:=\mathbb EY_{j,D}=p\,r_j(D),
\qquad
 \sum_j\mu_j=Rp=\theta.
\tag{2.5}
\]

No within-block independence is used. Markov's inequality gives

\[
 \Pr(Y_{j,D}=0)\ge1-\mu_j.
\tag{2.6}
\]

Independence between blocks and
\(\log(1-u)\ge-u/(1-u)\ge-u/(1-\alpha_D)\) for
\(0\le u\le\alpha_D\) imply

\[
\begin{aligned}
 \Pr(D\hbox{ is missed})
 &\ge\prod_j(1-\mu_j)\\
 &\ge\exp\left(-{\sum_j\mu_j\over1-\alpha_D}\right),
\end{aligned}
\]

which is (2.2). If a positive fraction of targets had
\(\alpha_D\le1-\eta\), summing (2.2) over those targets would give a
positive linear expected hole count. This proves (2.3), and
diagonalization gives (2.4). \(\square\)

Deleting phases, imposing the calibrated vacancy census, or attaching
shorter-window tags cannot turn a missed full-ring target into a hit.
Thus Theorem 2.1 remains a necessary correlation-scale theorem for every
such literal refinement.

The independence hypothesis is essential. A single random group element
may correlate choices belonging to many different root orbits. Orbit
size alone never licenses Theorem 2.1.

## 3. Exact cyclic and necklace-normalizer orbit sizes

Identify the ground set with \({\mathbb Z}_n\), let
\(\tau(z)=z+1\), and put \(C_n=\langle\tau\rangle\).

For a subset \(A\), its \(C_n\)-orbit size is its least cyclic period,
which divides \(n\) and is at most \(n\). The exact number of cyclic
orbits on the \(k\)-th layer is the Burnside count

\[
 {\cal N}(n,k)
 ={1\over n}
 \sum_{d\mid\gcd(n,k)}
 \varphi(d)\binom{n/d}{k/d}.
\tag{3.1}
\]

In the present central range, all but an exponentially small proportion
of roots are aperiodic, so their orbit size is exactly \(n\). For the
scale comparison only the unconditional upper bound \(n\) is needed.

### Lemma 3.1 (full automorphism group of the cyclic axis)

\[
 N_{S_n}(C_n)
 =\{z\mapsto az+b:
       a\in({\mathbb Z}_n)^\times,\ b\in{\mathbb Z}_n\},
\tag{3.2}
\]

and hence

\[
 |N_{S_n}(C_n)|=n\varphi(n).
\tag{3.3}
\]

#### Proof

If \(g\) normalizes \(C_n\), then
\(g\tau g^{-1}=\tau^a\) for some unit \(a\bmod n\). Writing \(b=g(0)\)
and iterating gives

\[
 g(z)=g(\tau^z0)=\tau^{az}g(0)=az+b.
\]

Conversely every such affine map conjugates \(\tau\) to \(\tau^a\).
There are \(n\varphi(n)\) choices. \(\square\)

Thus every normalizer orbit on roots has size at most
\(n\varphi(n)\). The orbit of the directed master cycle

\[
 (0,1,\ldots,n-1)
\]

modulo cyclic rotation has exactly \(\varphi(n)\) elements: translations
fix the same cyclic order modulo rotation, while the unit \(a\) changes
it to the directed step-\(a\) cycle.

The local phase group on one top has even less middle action. Rotating
the \(M\) phases fixes the unlabelled deck (0.1), and reversal merely
reverses the same deck. On phase-labelled states their orbit sizes are at
most \(M\) and \(2M\), respectively, but their root projection is a
singleton.

### Corollary 3.2 (necklace orbits miss the correlation scale)

Suppose blocks in Theorem 2.1 are normalizer root orbits. Then

\[
 \alpha_D\le p\,n\varphi(n)=o(1)
\]

for every \(D\), and therefore

\[
 \mathbb EZ\ge(e^{-1}-o(1))W.
\tag{3.4}
\]

If instead each independent component is a union of at most \(J\)
normalizer orbits, a good law requires, for all but \(o(W)\) targets,

\[
 J\ge {1-o(1)\over p\,n\varphi(n)}
   =(1-o(1)){R\over n\varphi(n)}.
\tag{3.5}
\]

For pure cyclic orbits the corresponding lower bound is
\((1-o(1))R/n\).

In particular,

\[
 \log {R\over n\varphi(n)}
 =\left({1\over2}+o(1)\right)
   \sqrt m\,(\log m)^{3/2}.
\tag{3.6}
\]

This proves a precise sense in which a necklace SCD does not itself
furnish the missing correlation. Its coordinate automorphisms move only
polynomially many roots. Its lowering map moves between ranks; a
symmetric chain has only one middle necklace and therefore supplies no
additional same-rank root orbit. Joining the number of quotient chains
in (3.5) is new cross-orbit structure, not an orbitwise lift of the SCD.

## 4. A deterministic support obstruction for master-cycle orbits

The preceding corollary used component independence. A stronger
deterministic obstruction applies when root frames are restrictions of
a small master-order library.

Fix a directed cyclic order \(\omega\) on \([n]\), and at root \(A\)
use its restriction to \(A^c\). A middle target \(D\) can be hit only if
some cyclic run of \(D\) in \(\omega\) has length at least \(H\).
Equivalently, \(D\) contains one of the \(n\) cyclic \(H\)-intervals of
\(\omega\). For a fixed interval there are
\(\binom{n-H}{m-H}\) possible \(D\)'s. Hence one master order covers at
most

\[
 n\binom{n-H}{m-H}
\tag{4.1}
\]

middle targets, and

\[
 {n\binom{n-H}{m-H}\over W}
 =n{(m)_H\over(n)_H}
 \le n2^{-H}.
\tag{4.2}
\]

A library of \(L\) master orders therefore covers at most
\(Ln2^{-H}W\), even if every root chooses its library member by an
arbitrary globally correlated rule. For the full necklace-normalizer
orbit, \(L=\varphi(n)\), which gives (0.5).

Thus a common cyclic, dihedral, or affine necklace axis fails in two
different ways:

1. its root orbits are \(o(R)\); and
2. as a master-order restriction library, its literal middle support is
   \(o(W)\) even without an independence assumption.

## 5. Full symmetric orbits do reach the necessary scale

The relevant full catalogue consists of rooted directed frames
\((A,\pi)\), where \(A\) is an unordered \(k\)-set and \(\pi\) is a
directed cyclic order on \(A^c\) modulo rotation.

### Lemma 5.1 (the full rooted-frame orbit)

The action of \(S_n\) is transitive on the rooted-frame catalogue, and
the exact orbit size is

\[
 {n!\over k!M}
 =N_H(M-1)!.
\tag{5.1}
\]

#### Proof

Any bijection sending one root to another and one directed top cycle to
another sends the corresponding rooted frames. The stabilizer of
\((A,\pi)\) consists of arbitrary permutations of the unordered root
\(A\), of size \(k!\), and the \(M\) rotations of the top cycle.
Therefore its size is \(k!M\), proving (5.1). \(\square\)

The factor \(k!\) is essential: the root is not internally ordered.

For a fixed middle target \(D\), the group
\(K_D=S_D\times S_{D^c}\) acts transitively on the \(k\)-subsets of
\(D\). The stabilizer of one such root inside \(K_D\) has size
\(k!H!m!\), so its orbit size is

\[
 {|K_D|\over k!H!m!}
 ={m!\over k!H!}
 =\binom mH=R.
\tag{5.2}
\]

Thus a coordinate-group root orbit of the exact required size exists.
This is a root orbit, not one rooted-frame orbit or one selectable trade
component. Its rooted-frame refinement is also exact. For a frame
\((A,\pi)\) with \(A\in{\cal R}(D)\), write the cyclic binary word
\(w=w(A,\pi;D)\) on the top cycle, marking the \(H\) points of
\(D\setminus A\) by \(1\) and the \(m\) points of \(D^c\) by \(0\).
Let

\[
 s(w)=|\operatorname {Stab}_{C_M}(w)|.
\]

Two such rooted frames lie in the same \(K_D\)-orbit if and only if
their binary necklaces agree, and that orbit has exact size

\[
 {|K_D|\over k!\,s(w)}
 ={(m!)^2\over k!\,s(w)}.
\tag{5.3}
\]

Indeed \(K_D\) preserves the binary necklace; conversely, equal patterns
permit an arbitrary bijection between the two roots and the
positionwise label bijections on the two top colours. A stabilizing
permutation is an arbitrary permutation of the \(k\) root labels
together with one of the \(s(w)\) colour-preserving cycle rotations.

The frames which hit \(D\) have the unique binary necklace consisting
of one \(H\)-run followed by one \(m\)-run. It has \(s(w)=1\), so all
hitting rooted frames form one catalogue orbit of size

\[
 {(m!)^2\over k!}
 =R\,H!m!.
\tag{5.4}
\]

Thus every binary-pattern catalogue orbit projects onto the whole root
star, and the hitting orbit has the exact one-root fibre size from
(1.1). The target-specific groups \(K_D\) vary with \(D\), and their
root projections overlap, so none of (5.2)--(5.4) is yet a simultaneous
selection or a switching component.

## 6. The exact two-orbit global atlas

Fix \(x\in[n]\) and let \(G_x\cong S_{n-1}\) fix \(x\) while permuting
all other coordinates.

### Theorem 6.1 (two rooted-frame orbits)

The action of \(G_x\) on the full rooted-frame catalogue has exactly the
two orbits in (0.10), with sizes (0.11).

#### Proof

First suppose \(x\in A\). The group is transitive on the roots
containing \(x\), of which there are \(\binom{n-1}{k-1}\). At a fixed
such root, \(G_x\) induces the full symmetric group on its \(M\)-point
top, so it is transitive on all \((M-1)!\) directed cyclic frames.
Equivalently, the stabilizer of a rooted frame has size
\((k-1)!M\), and

\[
 {|G_x|\over(k-1)!M}
 =\binom{n-1}{k-1}(M-1)!.
\]

Now suppose \(x\notin A\), so \(x\) lies on the top cycle. The group is
transitive on the \(\binom{n-1}{k}\) such roots. At a fixed root,
permuting the other \(M-1\) top coordinates moves a cyclic frame
transitively through all \((M-1)!\) possibilities: cut the cycle at the
fixed label \(x\), after which a frame is precisely a linear order of the
other labels. The rooted-frame stabilizer has size \(k!\), and

\[
 {|G_x|\over k!}
 =\binom{n-1}{k}(M-1)!.
\]

The two cases exhaust the catalogue and cannot mix because \(G_x\)
fixes membership of \(x\). \(\square\)

These are group orbits of catalogue states. They are not, merely by
being orbits, alternating switching components between two integral
resolutions. The latter requires a separate positive incidence pairing.

The target-star intersections are now forced. If \(x\notin D\), every
root \(A\subset D\) avoids \(x\). If \(x\in D\), then roots containing
\(x\) are obtained by omitting \(H\) elements from \(D\setminus\{x\}\),
whereas roots avoiding \(x\) must omit \(x\) and \(H-1\) other
elements. This proves (0.12)--(0.13).

The corresponding exact mean-load split under uniform frame marginals is

\[
\begin{array}{c|cc}
 &{\cal C}_1&{\cal C}_0\\ \hline
 x\notin D&0&\theta\\[1mm]
 x\in D&\theta{m-H\over m}&\theta{H\over m}.
\end{array}
\tag{6.1}
\]

Thus the dominant root class contributes mean \(1-o(1)\) at every
target, and the spill class contributes total mean \(O(H/m)=o(1)\)
precisely where it is needed. At the level of root projection this meets
the targetwise correlation requirement (2.4) uniformly, not merely for
almost every target. It does not prove a joint frame law inside the
classes.

There is a useful exact incidence check. Let

\[
 N_1=\binom{n-1}{k-1}={k\over n}N_H,\qquad
 N_0=\binom{n-1}{k}={M\over n}N_H.
\tag{6.2}
\]

Every frame rooted in \({\cal C}_1\) has all \(M\) middle owners
containing \(x\). Every frame rooted in \({\cal C}_0\) has exactly \(H\)
owners containing \(x\) and \(m=M-H\) owners avoiding \(x\). Therefore

\[
 MN_1+HN_0={MN_H\over2},
\qquad
 mN_0={MN_H\over2}.
\tag{6.3}
\]

These are exactly the forced coordinate-degree totals. Hence the
two-orbit split introduces no point-degree imbalance.

### General frozen-coordinate extension

For completeness, fix a set \(S\) of \(t\) coordinates pointwise and
let \(G_S=S_{[n]\setminus S}\). Its root orbits are indexed by
\(B=A\cap S\), subject to
\(|B|\le k\) and \(k-|B|\le n-t\), with exact size

\[
 |{\cal O}_B|=\binom{n-t}{k-|B|}.
\tag{6.4}
\]

If \(s=|D\cap S|\) and \(B'\subseteq D\cap S\) omits
\(u=s-|B'|\) of those \(s\) marked coordinates, then

\[
 |{\cal O}_{B'}\cap{\cal R}(D)|
 =\binom{m-s}{H-u}.
\tag{6.5}
\]

In particular the dominant orbit \(B'=D\cap S\) contains

\[
 \binom{m-s}{H}
 \ge\left(1-{sH\over m}\right)R
\tag{6.6}
\]

compatible roots. The inequality is the union bound for an \(H\)-subset
of \(D\) meeting one of its \(s\) marked coordinates. Thus any
\(t=o(m/H)\) gives a root-orbit partition in which every target star is
\(1-o(1)\) concentrated in one orbit.

At the frame level, if \(a=|S\setminus B|\) marked coordinates lie on
the top (necessarily \(a\le M\)), then for \(a=0\) there is one
rooted-frame orbit over
\({\cal O}_B\), while for \(a\ge1\) there are exactly

\[
 (a-1)!\binom{M-1}{a-1}
 ={(M-1)!\over(M-a)!}
\tag{6.7}
\]

such orbits. Indeed their invariants are the directed cyclic order of
the \(a\) fixed top markers and the numbers of unmarked top points in the
\(a\) gaps. Conversely, equality of these data permits a permutation of
the unmarked root labels and unmarked top labels carrying one state to
the other. For \(a\ge1\), each such orbit has exact size

\[
 {(n-t)!\over(k-|B|)!};
\tag{6.8}
\]

for \(a=0\), the unique orbit has size

\[
 {(n-t)!\over M(k-t)!}.
\tag{6.9}
\]

These follow from the rooted-frame stabilizers
\(S_{k-|B|}\) when a fixed top marker kills every nontrivial cycle
rotation, and \(S_{k-t}\times C_M\) when no marked coordinate lies on
the top. The one-coordinate choice is special: \(a\in\{0,1\}\), so
there is no frame-orbit fragmentation at all. These remain
catalogue-orbit counts, not switching-component counts.

## 7. Why orbit size is not yet coverage

Let \(F\) be any deterministic choice of one frame at every root and let
\(gF\) be its coordinate relabelling. If \(L_F(D)\) is the middle load,
then exactly

\[
 L_{gF}(D)=L_F(g^{-1}D).
\tag{7.1}
\]

Consequently coordinate relabelling preserves every symmetric load
statistic, including

\[
 |\{D:L_F(D)=0\}|,
\qquad
 \sum_D(L_F(D)-1)_+,
\qquad
 \sum_D\binom{L_F(D)}2.
\tag{7.2}
\]

Averaging the orbit of \(F\) can make its one-root marginals uniform, but
it cannot decrease a single one of these global quantities. A good seed
must exist before orbit averaging helps. If nested tags are transported
with the coordinate relabelling, the same identity holds separately for
every depth and sign, so every symmetric all-depth factorial-energy sum
is also orbit-invariant.

There is a more precise two-orbit version which allows the two classes
to move independently.

### Theorem 7.1 (exact independent anchored-orbit hole formula)

Put

\[
 {\cal X}_1=\{D\in\tbinom{[n]}m:x\in D\},\qquad
 {\cal X}_0=\{D\in\tbinom{[n]}m:x\notin D\},
\]

so \(|{\cal X}_0|=|{\cal X}_1|=W/2\). Let \(F_i\) be any deterministic
choice of one frame at every root in \({\cal A}_i\). Write

\[
\begin{aligned}
 S_{11}&=\{D\in{\cal X}_1:F_1\hbox{ hits }D\},\\
 S_{01}&=\{D\in{\cal X}_1:F_0\hbox{ hits }D\},\\
 S_{00}&=\{D\in{\cal X}_0:F_0\hbox{ hits }D\}.
\end{aligned}
\]

Choose independent uniform \(g_1,g_0\in G_x\) and use the
one-frame-per-root catalogue selection

\[
                         g_1F_1\cup g_0F_0.
\]

Every individual root frame has an exactly uniform marginal, and the
expected number \(Z\) of middle holes is exactly

\[
 \boxed{
 \mathbb EZ
 ={W\over2}-|S_{00}|
 +{W\over2}
  \left(1-{2|S_{11}|\over W}\right)
  \left(1-{2|S_{01}|\over W}\right).}
\tag{7.2a}
\]

Moreover

\[
 {2|S_{01}|\over W}
 \le {2HN_0\over W}
 =\theta{H\over m}=o(1).
\tag{7.2b}
\]

Consequently this two-orbit law has \(\mathbb EZ=o(W)\) if and only if

\[
 |S_{00}|={W\over2}-o(W),
 \qquad
 |S_{11}|={W\over2}-o(W).
\tag{7.2c}
\]

#### Proof

Theorem 6.1 says that \(G_x\) is transitive on each rooted-frame
catalogue \({\cal C}_i\). Fix a root \(A\in{\cal A}_i\) and a frame
\(\pi\) over it. For every input root \(B\in{\cal A}_i\), the number of
group elements carrying the selected state \((B,\pi_B)\) to
\((A,\pi)\) is the common rooted-state stabilizer size. Since
\(|{\cal C}_i|=|{\cal A}_i|(M-1)!\), summing over \(B\) shows that the
output frame at \(A\) is uniform over its \((M-1)!\) possibilities.

The group \(G_x\) is transitive separately on \({\cal X}_0\) and
\({\cal X}_1\). Hence \(g_0S_{00}\) has the same cardinality as
\(S_{00}\), giving exactly \(W/2-|S_{00}|\) holes in \({\cal X}_0\).
For a fixed \(D\in{\cal X}_1\), the events

\[
 D\notin g_1S_{11},
 \qquad
 D\notin g_0S_{01}
\]

are independent and have probabilities
\(1-2|S_{11}|/W\) and \(1-2|S_{01}|/W\), respectively. Summing their
product over \({\cal X}_1\) proves (7.2a).

Every \(F_0\)-frame has exactly \(H\) middle windows containing \(x\).
Thus the total number of its occurrences in \({\cal X}_1\) is \(HN_0\),
which bounds \(|S_{01}|\). Equation (6.2) gives (7.2b). Since the second
factor in (7.2a) is \(1-o(1)\), the two nonnegative terms in that formula
sum to \(o(W)\) exactly under (7.2c). \(\square\)

Thus independent global motion of the two catalogue orbits is an actual
correlated one-frame-per-root law, not merely a dimension count. It can
randomize the overlap between their supports, but the spill orbit is too
small to repair a linear defect. The exact unresolved task is to build
the two near-spanning dominant seeds in (7.2c), with bounded
multiplicities and common nested tags.

Using different coordinate permutations on the two root classes is
physically legitimate here only in the rootwise sense: every image is
still a legal cyclic frame over its own root, and the two root classes
are disjoint. It is not one global coordinate relabelling. Therefore it
does not automatically preserve any cross-class owner constraint,
bounded-excess condition, chronology, or common tagged interface. Those
are deliberately outside Theorem 7.1.

Likewise, the exact \(K_D\)-orbit (5.2) has precisely the support size
needed by a one-target root-star coupling, but target-specific
prescriptions do not tensor. If \(d=|D\setminus E|\), their root stars
have exact overlap

\[
 |{\cal R}(D)\cap{\cal R}(E)|
 =
 \begin{cases}
 \binom{m-d}{H-d},&d\le H,\\
 0,&d>H.
 \end{cases}
\tag{7.3}
\]

Moreover every root belongs to \(\binom MH\) different target stars.
Thus the one-target couplings impose many incompatible prescriptions on
the same frame variable. Their formal signed orbit sum is not one
positive probability law.

There is also a sharp elementary fact about literal deck overlays. For
two distinct roots \(A,B\), any two complete decks satisfy

\[
 |{\cal D}(A,\pi)\cap{\cal D}(B,\rho)|\le H.
\tag{7.4}
\]

Choose \(x\in B\setminus A\). Every common owner must contain \(x\), and
in the \(A\)-ring a fixed top coordinate belongs to exactly \(H\)
cyclic \(H\)-windows. Hence (7.4). In an \(M\)-valent old/new occurrence
overlay with no same-root edges, every root must therefore meet at least
\(\lceil M/H\rceil\) distinct roots on the opposite shore, and every
component contains at least that many roots per shore. This is only a
lower bound; it supplies no upper bound preventing a giant component.

## 8. The exact surviving gate

The necklace-axis conclusion is closed:

* cyclic orbits have size at most \(n\);
* dihedral orbits have size at most \(2n\);
* the full cyclic normalizer has size \(n\varphi(n)\);
* its master-cycle orbit has only \(\varphi(n)\) orders;
* independent products of these orbits have at least
  \((e^{-1}-o(1))W\) expected holes; and
* their ambient-order restrictions have \(W-o(W)\) deterministic holes
  even under arbitrary global coupling.

The global orbit-capacity conclusion is also exact:

* \(K_D\) supplies a root orbit of size exactly \(R\) for one target;
* \(S_n\) has one full rooted-frame orbit of size
  \(N_H(M-1)!\);
* the one-anchor subgroup \(G_x\) has exactly two full catalogue orbits;
  and
* the root projection of one of those two contains a \(1-H/m\) fraction
  of every split target star and all of every unsplit target star.

The remaining positive theorem can therefore be stated without any
orbit ambiguity.

> **Anchored global resolution lemma (open).** Construct an
> owner-preserving positive rewiring, or directly choose one directed
> frame at every root in each of the two \(G_x\)-catalogue orbits, so
> that, after the required calibrated phase vacancies, the combined
> middle decks have \(o(W)\) holes and \(o(W)\) excess over their exact
> integer floor, with the \(\theta H/m\) spill in (6.1) filling the
> unmatched part of the dominant root class. The same choices must admit
> the prescribed nested shorter-window tags with aggregate factorial
> excess \(o(W)\). If the proof is by switching, it must separately show
> that the catalogue orbits decompose into legal owner-preserving
> alternating components.

This lemma is not implied by edge transitivity, orbit size, uniform
marginals, or the one-target star coupling. It is a positive integral
near-resolution across the dense overlap kernel (7.3).

Accordingly, the requested cross-orbit investigation has a definitive
boundary:

\[
\boxed{
\begin{minipage}{0.88\linewidth}
The coordinate automorphism orbits supplied by the cyclic necklace axis
are polynomial and cannot supply the \(\binom mH\) correlation scale; a
typical successful component must fuse a superpolynomial number of them.
The raw capacity for such a fusion does exist: fixing one coordinate
already gives exactly two rooted-frame catalogue orbits whose root
projections have uniform \(1-H/m\) target-star concentration and the
correct degree ledger. This is not itself a legal rewiring. What remains
is to construct positive owner-preserving switching components, or a
direct simultaneous owner-and-tag resolution, inside those two
catalogue classes.
\end{minipage}}
\]
