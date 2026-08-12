# Long-cycle coordinate bridges: exact mixing without fixed targets

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let (F) be any exact middle wreath factor on (n=2m+1) coordinates,
and let ({\cal Z}_q) be its holes at depth (q).  There is one
coordinate permutation (\sigma), which may be required to be a single
(n)-cycle, that simultaneously has large hole-to-covered opportunity
at every weighted collection of depths.

The exact class-average identity is

\[
 \mathbb E_{\sigma\text{ an }n\text{-cycle}}
 |\{R\in{\cal Z}_q:\sigma R\notin{\cal Z}_q\}|
 = {h_q(N_q-h_q)\over N_q}
   +{\|P_1\mathbf1_{{\cal Z}_q}\|_2^2\over n-1}.
 \tag{0.1}
\]

Here (P_1) is projection onto the degree-one Johnson harmonic.  In
particular the expectation is at least the uniform-permutation value,
not smaller.

Unlike a transposition, a single (n)-cycle fixes no nonempty proper
subset.  Thus this bridge has no setwise-fixed hole floor at any depth.

At depth one, exact middle ownership also implies

\[
 \mu_1(S)\le\left\lfloor{m+2\over2}\right\rfloor.
 \tag{0.2}
\]

Consequently some (n)-cycle maps at least

\[
 \boxed{{2h_1\over m}}
 \tag{0.3}
\]

first-shadow holes to covered targets.  This is the correct
(h_1/m) opportunity scale, with no frozen-target obstruction.

This does not yet prove descent inside the exact-factor fibre: the
ownership overlap graph for a long-cycle bridge may have large
components.  The remaining question is now sharply isolated as
fragmentation/leakage for a nonlocal bridge, rather than availability
of productive images or fixed targets.

## 1. The class average of coordinate (n)-cycles

Fix a rank (1\le r\le n-1), and let

\[
 V_r=\mathbb R^{\binom{[n]}r}.
 \tag{1.1}
\]

The permutation module has the multiplicity-free Johnson decomposition

\[
 V_r=U_0\oplus U_1\oplus\cdots\oplus U_s,
 \qquad s=\min(r,n-r),
 \tag{1.2}
\]

where (U_j) is the Specht module indexed by ((n-j,j)).  Let
({\mathscr C}_n) be the conjugacy class of coordinate permutations
which are one (n)-cycle, and define the class average

\[
 K={1\over|{\mathscr C}_n|}
   \sum_{\sigma\in{\mathscr C}_n}P_\sigma.
 \tag{1.3}
\]

### Theorem 1.1 (exact long-cycle spectrum)

The operator (K) acts by

\[
 \boxed{
 K|_{U_0}=1,\qquad
 K|_{U_1}=-{1\over n-1},\qquad
 K|_{U_j}=0\quad(j\ge2).}
 \tag{1.4}
\]

#### Proof

Because (1.3) is a conjugacy-class average, Schur's lemma says that its
eigenvalue on an irreducible Specht module (S^\lambda) is the character
ratio

\[
 {\chi^\lambda((n))\over\dim S^\lambda}.
 \tag{1.5}
\]

By the Murnaghan--Nakayama rule, the character of an (n)-cycle is
zero unless (\lambda) is a hook.  Among the two-row shapes
((n-j,j)), only (j=0) and (j=1) are hooks.  Their characters are
(1) and (-1), respectively, and

\[
 \dim S^{(n-1,1)}=n-1.
 \tag{1.6}
\]

This proves (1.4). \(\square\)

## 2. Exact hole-to-covered opportunity

Let ({\cal Z}\subseteq\binom{[n]}r), put

\[
 z=\mathbf1_{\cal Z},\qquad
 h=|{\cal Z}|,\qquad N=\binom nr,
 \tag{2.1}
\]

and decompose

\[
 z={h\over N}\mathbf1+u+v,
 \qquad u\in U_1,quad
 v\in U_2\oplus\cdots\oplus U_s.
 \tag{2.2}
\]

For (\sigma\in{\mathscr C}_n), define

\[
 A_\sigma({\cal Z})
 =|\{R\in{\cal Z}:\sigma R\notin{\cal Z}\}|.
 \tag{2.3}
\]

### Theorem 2.1 (exact long-cycle crossing identity)

\[
 \boxed{
 \mathbb E_{\sigma\in{\mathscr C}_n}A_\sigma({\cal Z})
 ={h(N-h)\over N}+{\|u\|_2^2\over n-1}.}
 \tag{2.4}
\]

In particular some (n)-cycle (\sigma) satisfies

\[
 \boxed{A_\sigma({\cal Z})\ge {h(N-h)\over N}.}
 \tag{2.5}
\]

#### Proof

The inverse of an (n)-cycle is again in the same conjugacy class, so
there is no convention issue in writing

\[
 \mathbb E_\sigma A_\sigma({\cal Z})
 =\langle z,K(\mathbf1-z)\rangle.
 \tag{2.6}
\]

By (1.4),

\[
 K(\mathbf1-z)
 =\left(1-{h\over N}\right)\mathbf1+{u\over n-1}.
 \tag{2.7}
\]

Orthogonality of the decomposition (2.2) now gives (2.4), and (2.5)
follows by averaging. \(\square\)

### Corollary 2.2 (one common bridge at many depths)

For arbitrary nonnegative weights (w_q), some single (n)-cycle
(\sigma) satisfies

\[
 \boxed{
 \sum_qw_q
 |\{R\in{\cal Z}_q:\sigma R\notin{\cal Z}_q\}|
 \ge
 \sum_qw_q\left[
 {h_q(N_q-h_q)\over N_q}
 +{\|P_1\mathbf1_{{\cal Z}_q}\|_2^2\over n-1}
 \right].}
 \tag{2.8}
\]

#### Proof

Apply (2.4) at every depth to the same uniformly random (n)-cycle,
sum, and choose an outcome attaining at least the expectation. \(\square\)

## 3. There are no fixed nontrivial targets

### Proposition 3.1

If (\sigma) is an (n)-cycle and

\[
 \varnothing\ne R\ne[n],
 \tag{3.1}
\]

then (\sigma R\ne R).

#### Proof

A set invariant under a permutation is a union of its coordinate
orbits.  An (n)-cycle has only one coordinate orbit, so its only
invariant sets are (\varnothing) and ([n]). \(\square\)

Thus the positive fixed-hole floor proved for many transposition cubes
has no analogue caused by pointwise set invariance for a long-cycle
bridge.  There may still be other componentwise invariants, so this is
not by itself a mixing theorem.

## 4. Exact occurrence cap at every depth

Let (F) be an exact middle wreath factor.  At depth (q), put

\[
 r=m-q,qquad M=m+q+1.
 \tag{4.1}
\]

### Lemma 4.1 (extension consumption by one occurrence)

Every target (S\in\binom{[n]}r) satisfies

\[
 \boxed{
 (q+1)\mu_q(S)\le\binom Mq.}
 \tag{4.2}
\]

#### Proof

One cyclic occurrence of (S) in a wreath row lies in exactly (q+1)
length-(m) intervals of that row: extend it by a total of (q)
positions split arbitrarily between its two ends.  These middle sets are
distinct.

Across all occurrences of (S), no middle extension is charged twice.
Indeed, every middle (m)-set has a unique owning row, and inside that
row a fixed proper cyclic interval occurs at most once.  There are
exactly

\[
 \binom{n-r}{m-r}=\binom Mq
 \tag{4.3}
\]

middle extensions of (S).  This proves (4.2). \(\square\)

Put

\[
 L_q=\left\lfloor{1\over q+1}\binom{m+q+1}{q}\right\rfloor.
 \tag{4.4}
\]

If (t_q=N_q-h_q) is the number of covered targets, then the total
occurrence mass is (W), so Lemma 4.1 gives

\[
 \boxed{t_q\ge {W\over L_q}.}
 \tag{4.5}
\]

Combining this with (2.5) gives:

### Corollary 4.2 (explicit opportunity from exact ownership)

Some (n)-cycle satisfies, at a fixed depth (q),

\[
 \boxed{
 |\{R\in{\cal Z}_q:\sigma R\notin{\cal Z}_q\}|
 \ge {h_qW\over L_qN_q}
 ={h_q\lambda_q\over L_q},
 \qquad\lambda_q={W\over N_q}.}
 \tag{4.6}
\]

For fixed (q), this is

\[
 \left((q+1)q!+o_q(1)\right){h_q\over m^q}.
 \tag{4.7}
\]

The same permutation can be selected simultaneously across depths by
using (2.8); in particular

\[
 \sum_qw_q A_{\sigma,q}
 \ge\sum_qw_q{h_q\lambda_q\over L_q}
 \tag{4.8}
\]

for some one (n)-cycle.

## 5. The depth-one bound

At (q=1), Lemma 4.1 is

\[
 2\mu_1(S)\le m+2,
 \tag{5.1}
\]

and hence

\[
 L_1=\left\lfloor{m+2\over2}\right\rfloor.
 \tag{5.2}
\]

Since

\[
 {W\over N_1}={m+2\over m},
 \tag{5.3}
\]

we have

\[
 {\lambda_1\over L_1}\ge {2\over m}.
 \tag{5.4}
\]

Corollary 4.2 therefore proves:

### Theorem 5.1 (productive fixed-point-free bridge)

For every exact middle wreath factor, some coordinate (n)-cycle
(\sigma) maps at least

\[
 \boxed{{2h_1\over m}}
 \tag{5.5}

first-shadow holes to covered first-shadow targets, while fixing no
first-shadow target setwise.

This improves the deterministic transposition guarantee by a factor
asymptotic to two and removes the transposition's setwise-fixed target
family entirely.

## 6. What is still missing

Overlay (F) with (\sigma F).  As for every pair of exact factors,
each ownership component admits an independent legal left/right side
choice.  The productive count (5.5) says that the right factor has
covered occurrences available for at least (2h_1/m) old holes.

It does **not** say that these occurrences split across enough ownership
components, nor that switching their components creates fewer new holes.
At the opposite extreme, if the overlap graph is connected, its cube
has only the two endpoints (F) and (\sigma F), which have the same
number of holes.

The new bridge therefore isolates a concrete next theorem:

\[
 \boxed{
 \begin{gathered}
 \text{Choose the productive (n)-cycle in (2.8) so that the overlap}\
 \text{graph (F\cup\sigma F) has enough fragmentation, and its}\
 \text{common-target leakage is smaller than its exclusive opportunity.}
 \end{gathered}}
 \tag{6.1}
\]

This is genuinely different from the failed fixed-transposition lane:
continuous rank mixing is exact, all higher Johnson harmonics are
annihilated in class average, and no nontrivial target is frozen by the
coordinate bridge.  The only unresolved part is integral ownership
component geometry.
