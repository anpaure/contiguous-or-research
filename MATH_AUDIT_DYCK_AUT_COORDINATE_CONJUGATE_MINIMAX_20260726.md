# Dyck-port automorphisms and the exact scope of conjugate minimax

Date: 2026-07-26

Method: hand mathematics only.

Let \(\mathcal D_s\) be the family of Dyck \(s\)-subsets of
\([2s]\), let \(F_s\) be the canonical anchored exact
\(\mathcal D_s\)-port factor, and put

\[
 H_s=\langle(2i\ \ 2i+1):1\le i\le s-1\rangle,
 \qquad
 \omega_s=\prod_{i=1}^{s-1}(2i\ \ 2i+1).
 \tag{0.1}
\]

This note records the minimax consequence of the structural
classification

\[
                       \operatorname {Aut}(\mathcal D_s)=H_s.
\tag{0.2}
\]

The conclusion is sharp but has an important quantifier boundary.
Equation (0.2) proves that the all-block conjugate is minimax-optimal
among **all coordinate conjugates of the fixed canonical factor** which
remain anchored at \(\mathcal D_s\).  It does not prove optimality among
arbitrary exact factors: allowing the base factor itself to vary turns
the comparison into the unrestricted exact-factor problem.

## 1. Coordinate conjugation and the port-set criterion

Let \(K\) be an anchored exact factor with initial port family
\(\mathcal P\subseteq\binom{[2s]}s\).  For
\(\pi\in S_{2s}\), its literal coordinate relabelling \(\pi K\) has
rows

\[
 X_t^{\pi K}(\pi P)=\pi X_t^K(P),\qquad
 Y_t^{\pi K}(\pi P)=\pi Y_t^K(P),\qquad P\in\mathcal P.
\tag{1.1}
\]

Thus its initial port family is exactly \(\pi\mathcal P\).  If
\(\pi\mathcal P=\mathcal P\), reindexing by the original root
\(P\in\mathcal P\) gives the coordinate conjugate

\[
 X_t^{K,\pi}(P)=\pi X_t^K(\pi^{-1}P),\qquad
 Y_t^{K,\pi}(P)=\pi Y_t^K(\pi^{-1}P).
\tag{1.2}
\]

### Lemma 1.1 (exact port-set criterion)

The literal relabelling of an anchored \(\mathcal D_s\)-port factor is
again an anchored \(\mathcal D_s\)-port factor if and only if

\[
                         \pi\mathcal D_s=\mathcal D_s.
\tag{1.3}
\]

When (1.3) holds, (1.2) preserves every inclusion edge, every Johnson
edge, both complete ownership ledgers, and the complementary endpoint
of every row.

#### Proof

The initial states of the relabelled rows are precisely
\(\{\pi P:P\in\mathcal D_s\}=\pi\mathcal D_s\).  Hence equality with
the prescribed initial port family is necessary.  Conversely, if (1.3)
holds, (1.2) merely reindexes the rows and applies one coordinate
permutation to every state.  Coordinate permutations preserve set size,
inclusion, Johnson adjacency, distinctness, and complement.  Therefore
all exact-factor axioms are preserved. \(\square\)

Assuming (0.2), Lemma 1.1 gives the exact identity

\[
 \{F_s^{\pi}:\pi F_s\text{ is again anchored at }\mathcal D_s\}
       =\{F_s^h:h\in H_s\}.
\tag{1.4}
\]

Every element of \(H_s\) is an involution, so (1.2) becomes the formula
used in the full-swap report,

\[
              X_t^{F_s,h}(P)=hX_t^{F_s}(hP),\qquad
              Y_t^{F_s,h}(P)=hY_t^{F_s}(hP).
\tag{1.5}
\]

Consequently the phrase "the adjacent-block conjugation grammar" is no
longer a restriction after (0.2): it is the complete coordinate
stabilizer of the Dyck port family.

## 2. The deterministic minimax theorem

Let \(\mathcal F_{s,j}\) be the roots with first return at \(2j\).  For
an anchored exact factor \(K\), define its fibre-resolved first load by

\[
 q_K(j,x)=\#\{P\in\mathcal F_{s,j}:b_1^K(P)=x\},
 \qquad
 \Lambda_s(K)=\max_{1\le j\le s,\ x\in[2s]}q_K(j,x).
\tag{2.1}
\]

Let \(R_n\) count Dyck words of semilength \(n\) having no singleton
primitive component.  Equivalently,

\[
 \sum_{n\ge0}R_nz^n={1\over1-z^2C(z)^2},
 \qquad R_0=1,\qquad R_1=0.
\tag{2.2}
\]

### Theorem 2.1 (all coordinate-conjugate canonical seeds)

Assume \(\operatorname {Aut}(\mathcal D_s)=H_s\).  Then

\[
 \min_{\substack{\pi\in S_{2s}\\
                   F_s^\pi\text{ anchored at }\mathcal D_s}}
       \Lambda_s(F_s^\pi)
 =
 \begin{cases}
  1,&s=1,\\
  1,&s=2,\\
  R_{s-1},&s\ge3.
 \end{cases}
\tag{2.3}
\]

The all-block element \(\omega_s\) attains the minimum in every case.
For \(s\ge3\), every allowed coordinate conjugate has the common lower
cell

\[
                         q_{F_s^h}(s,2s)\ge R_{s-1}.
\tag{2.4}
\]

#### Proof

By (1.4), every allowed coordinate conjugate is \(F_s^h\) for some
\(h\in H_s\).  In the two-coloured Motzkin encoding, \(h\) changes only
the colours of selected horizontal steps; it leaves the up/down
skeleton unchanged.  The \(R_{s-1}\) skeletons with no ground
horizontal step therefore remain in first-return class \(s\) both
before and after applying \(h\).  Every \(h\in H_s\) fixes coordinate
\(2s\), and the canonical first target of a class-\(s\) root is \(2s\).
This proves (2.4), hence
\(\Lambda_s(F_s^h)\ge R_{s-1}\).

The exact quota formula for the full swap \(\omega_s\) gives

\[
                         \Lambda_s(F_s^{\omega_s})=R_{s-1}
                         \qquad(s\ge3),
\tag{2.5}
\]

so equality follows.  For \(s=1\), the unique row forces value one.  For
\(s=2\), every integral factor has a nonempty first-load cell, while the
full swap has two unit off-diagonal cells, so the value is again one.
The exceptional formula at \(s=2\) is necessary because \(R_1=0\).
\(\square\)

Thus the earlier theorem described as optimality "inside \(H_s\)" is,
after (0.2), an optimality theorem over every coordinate relabelling of
the canonical seed compatible with the fixed Dyck ports.  No additional
coordinate-conjugate canonical seed lies outside that list.

Since

\[
                         R_n\sim {4\over9}C_n,
 \qquad {C_{s-1}\over C_s}\longrightarrow {1\over4},
\tag{2.6}
\]

the optimal resolved load throughout this complete coordinate-conjugacy
class satisfies

\[
 {1\over C_s}
 \min_{\pi:\,\pi\mathcal D_s=\mathcal D_s}
       \Lambda_s(F_s^\pi)
 \longrightarrow {1\over9}.
\tag{2.7}
\]

Equivalently, in the zero-background normalization
\(\theta=C_s/p\), no fixed-port coordinate relabelling of the canonical
seed improves the all-block range \(\theta\le 9+o(1)\).

## 3. Convexified orbit minimax

The common cell (2.4) also prevents improvement by mixing conjugates.
For a probability distribution \(\mu\) on the allowed coordinate
conjugates, put

\[
 \bar q_\mu(j,x)=\sum_{h\in H_s}\mu(h)q_{F_s^h}(j,x),
 \qquad
 \bar\Lambda_s(\mu)=\max_{j,x}\bar q_\mu(j,x).
\tag{3.1}
\]

### Corollary 3.1 (fractional/orbit robustness)

For every \(s\ge3\),

\[
                  \min_{\mu\in\Delta(H_s)}\bar\Lambda_s(\mu)
                  =R_{s-1}.
\tag{3.2}
\]

#### Proof

Equation (2.4) holds in the same cell \((s,2s)\) for every \(h\), so

\[
 \bar q_\mu(s,2s)
   =\sum_h\mu(h)q_{F_s^h}(s,2s)\ge R_{s-1}.
\]

The point mass at \(\omega_s\) attains \(R_{s-1}\) by (2.5).
\(\square\)

This is stronger than a lower bound obtained by averaging total loads:
the obstruction is row-fibre and target aligned across the entire
orbit.

There is one small fractional exception.  For \(s=2\), write
\(H_2=\{e,(2\ 3)\}\).  The two conjugates place their unit loads in
disjoint cells within each source fibre.  Mixing them with equal weights
gives

\[
                    \min_{\mu\in\Delta(H_2)}
                    \bar\Lambda_2(\mu)=\frac12,
\tag{3.3}
\]

although the deterministic minimax value remains one.  Hence the
qualification \(s\ge3\) in Corollary 3.1 is essential.

## 4. What the automorphism theorem does not prove

Let \(\mathscr E_s\) be the class of **all** anchored exact
\(\mathcal D_s\)-port factors.  If one lets both the base factor
\(K\in\mathscr E_s\) and the coordinate automorphism vary, then

\[
                \{K^h:K\in\mathscr E_s,\ h\in H_s\}
                =\mathscr E_s.
\tag{4.1}
\]

Indeed, conjugation preserves exactness, giving inclusion from left to
right, while \(h=e\) gives the reverse inclusion.  Therefore

\[
 \min_{K\in\mathscr E_s,\ h\in H_s}\Lambda_s(K^h)
       =\min_{K\in\mathscr E_s}\Lambda_s(K).
\tag{4.2}
\]

The classification of \(\operatorname {Aut}(\mathcal D_s)\) contains
no information about the right side of (4.2).  In particular, the
Motzkin no-ground-horizontal core is invariant under coordinate
automorphisms of the **canonical** trajectories; it has not been shown
to be forced in an arbitrary exact factor.

The universal endpoint theorem does not fill this gap.  It forces the
raw first-insertion histogram

\[
             \#\{P\in\mathcal D_s:b_1^K(P)=2s\}=C_{s-1}
\tag{4.3}
\]

for every exact factor \(K\), but it does not force
\(R_{s-1}\) of those rows to lie in the single source fibre
\(\mathcal F_{s,s}\).  The known lower-rank port recursion constrains
which roots may make up (4.3), but is only necessary and has not been
proved to imply the resolved lower bound (2.4).

Accordingly:

1. **Fixed canonical base seed:** the all-block conjugate is minimax
   optimal among every coordinate-conjugate exact seed, assuming (0.2).
2. **Arbitrary base exact seed:** minimax optimality is still open.  A
   proof would require a new invariant common to all exact factors, or a
   classification of exact first matchings, not merely a classification
   of coordinate automorphisms of \(\mathcal D_s\).
3. **Moving port family:** an arbitrary \(\pi\in S_{2s}\) always gives
   an exact factor on the moved family \(\pi\mathcal D_s\), but that is
   not an anchored \(\mathcal D_s\)-seed.  Comparing its first-return
   loads to (2.1) requires an additional identification of the moved
   ports; no such identification is part of coordinate conjugacy.

This is the precise deduction available from
\(\operatorname {Aut}(\mathcal D_s)=H_s\).
