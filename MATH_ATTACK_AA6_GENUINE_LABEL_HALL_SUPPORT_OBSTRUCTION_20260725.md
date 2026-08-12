# Sixth-wave AA: genuine label-Hall robustness under rowwise support

Date: 2026-07-25

Method: pure mathematics only.  No search, computation, solver, or
external black box is used.

## 0. Outcome

This note gives a **conditional robustness lemma on genuine integral
SCDs**.  It shows that, if a stationary-frame source SCD and per-color
rowwise lineage are supplied, then the resulting obstruction survives the
logarithmic nonaligned-support escape for invariant packet seeds.  No proof
is known here that a centrally \(\mathcal P\)-paired full SCD exists for
every \(m\), and generic packet-palette/Birkhoff rounding does not preserve
the lineage hypothesis below.

Let \(\mathcal D,\mathcal E\) be full SCDs of \(B_{2m}\), clipped at the
same depth \(H\).  Suppose there is a radius-preserving bijection

\[
\phi:\mathcal D^{(H)}\longrightarrow\mathcal E^{(H)}
\]

such that every chain state has a rowwise coordinate-permutation lineage

\[
\phi(\omega)=g_\omega\omega,
\qquad
g_\omega\in\operatorname{Sym}(B),
\tag{0.1}
\]

for one common coordinate support \(B\subseteq[2m]\), \(|B|=b\).  The
permutation \(g_\omega\) may depend arbitrarily on the state.  No common
relabeling is assumed.

For every Johnson-label Hall witness at depth \(q\), at most

\[
b\lambda_q,
\qquad
\lambda_q
=\binom{2m-1}{m+q-1}-\binom{2m-1}{m-q-1},
\tag{0.2}
\]

state labels can move.  Consequently every Hall deficiency degrades by at
most \(2b\lambda_q\).  This yields the exact robust lower bound

\[
\boxed{
P_q(\mathcal E)
\ge
\bigl(
\mu_q^{\mathcal D}(\mathcal S)
-\mu_q^{\mathcal D}(\Gamma_q\mathcal S)
-2b\lambda_q
\bigr)_+}
\tag{0.3}
\]

for every label family \(\mathcal S\).

In particular, if \(\mathcal D\) is centrally paired in one fixed perfect
matching \(\mathcal P\), then

\[
\boxed{
\widehat\Phi_H(\mathcal E)
\ge
2\left(1-\frac{2b}{m}\right)_+N_1.}
\tag{0.4}
\]

Since \(N_1=(m/(m+1))W\), an \(o(W)\)-toll descendant of this form requires

\[
\boxed{b\ge m/2-o(m).}
\tag{0.5}
\]

If the stronger stationary-frame condition

\[
Z_q(\omega)\in
\mathcal U_q(\mathcal P)
:=\{\text{unions of }q\text{ edges of }\mathcal P\}
\tag{0.6}
\]

holds at every controlled depth, then the full robust bound is

\[
\boxed{
\widehat\Phi_H(\mathcal E)
\ge
2\sum_{q=1}^H
\left(1-\frac{2bq}{m}\right)_+N_q.}
\tag{0.7}
\]

In particular, for \(H=\lceil A\sqrt m\rceil\) and \(b=o(\sqrt m)\),

\[
\frac{\widehat\Phi_H(\mathcal E)}{W\sqrt m}
\ge
2\int_0^Ae^{-x^2}\,dx-o(1).
\tag{0.8}
\]

Thus, **within these two hypotheses**, a nonaligned common support of order
\(\log m\), although sufficient
to defeat every invariant suspended-seed count in the odd-factor packet
lane, cannot rescue a **lineage-preserving** rotor/SCD rounding from a
stationary-pair source.  The proof uses the actual Boolean chain states,
actual rotor Johnson labels, and a final integral SCD, so exact middle and
all-rank ownership are preserved.

The missing hypotheses are substantial, not cosmetic.  A successful
target-palette rounding
must reassign states between colors so that no per-color bijection (0.1)
survives, or it must start from a label distribution with no macroscopic
Hall witness.  Odd-wreath row lineage does not automatically imply SCD
chain-state lineage; proving such a bridge would make (0.4) apply to that
route, while failure of the bridge identifies the required cross-color
rebundling.

## 1. The Johnson-label ledger

For a radius-\(d\) state

\[
\omega=(L;z_1,\ldots,z_{2d};R)
\]

and \(1\le q\le d\), put

\[
Z_q(\omega)
=\{z_{d-q+1},\ldots,z_{d+q}\}
\in\binom{[2m]}{2q}.
\tag{1.1}
\]

Let

\[
\mathcal V_q(\mathcal D)
=\bigcup_{d=q}^H\mathcal D_d,
\qquad
\mu_q^{\mathcal D}(Z)
=\#\{\omega\in\mathcal V_q(\mathcal D):Z_q(\omega)=Z\}.
\tag{1.2}
\]

The exact SCD ownership equations give

\[
|\mathcal V_q(\mathcal D)|=N_q
\tag{1.3}
\]

and the one-design margins

\[
\sum_{Z\ni i}\mu_q^{\mathcal D}(Z)=\lambda_q
\qquad(i\in[2m]),
\tag{1.4}
\]

with \(\lambda_q\) as in (0.2).  These identities hold for every full
integral SCD, including the clipped top class.

Let \(J_q=J(2m,2q)\), joining labels whose intersection has size \(2q-1\),
and define

\[
\Gamma_q(\mathcal S)
=\{Z':\exists Z\in\mathcal S, |Z\cap Z'|=2q-1\}.
\tag{1.5}
\]

If \(P_q(\mathcal E)=\sum_{d=q}^Hp_d(\mathcal E)\) for any spanning rotor
path forests, the exact label-Hall theorem is

\[
P_q(\mathcal E)
\ge
\bigl(
\mu_q^{\mathcal E}(\mathcal S)
-\mu_q^{\mathcal E}(\Gamma_q\mathcal S)
\bigr)_+.
\tag{1.6}
\]

## 2. Only labels meeting the support can move

Coordinate relabeling commutes with the central-label map:

\[
Z_q(g\omega)=gZ_q(\omega).
\tag{2.1}
\]

If \(g\in\operatorname{Sym}(B)\) and

\[
Z_q(\omega)\cap B=\varnothing,
\]

then \(gZ_q(\omega)=Z_q(\omega)\).  Hence the only atoms of
\(\mu_q^{\mathcal D}\) which can change under (0.1) belong to

\[
\mathcal X_q(B)
=\{\omega\in\mathcal V_q(\mathcal D):Z_q(\omega)\cap B\ne\varnothing\}.
\]

By the union bound and (1.4),

\[
\boxed{
|\mathcal X_q(B)|
\le\sum_{i\in B}\sum_{Z\ni i}\mu_q^{\mathcal D}(Z)
=b\lambda_q.}
\tag{2.2}
\]

This estimate is independent of the geometry of \(B\).  In particular it
does not distinguish aligned from reflection supports.

### Theorem 2.1 -- support robustness of every label-Hall witness

Under (0.1), for every \(q\le H\) and every label family \(\mathcal S\),

\[
\boxed{
\begin{aligned}
&\mu_q^{\mathcal E}(\mathcal S)
-\mu_q^{\mathcal E}(\Gamma_q\mathcal S)\\
&\qquad\ge
\mu_q^{\mathcal D}(\mathcal S)
-\mu_q^{\mathcal D}(\Gamma_q\mathcal S)
-2b\lambda_q.
\end{aligned}}
\tag{2.3}
\]

Consequently (0.3) holds.

#### Proof

The bijection \(\phi\) moves at most
\(|\mathcal X_q(B)|\le b\lambda_q\) labelled atoms.  For any fixed label
family \(\mathcal A\), moving \(R\) atoms changes its mass by at most \(R\):

\[
|\mu_q^{\mathcal E}(\mathcal A)
-\mu_q^{\mathcal D}(\mathcal A)|\le b\lambda_q.
\tag{2.4}
\]

Apply (2.4) once to \(\mathcal S\) and once to
\(\Gamma_q\mathcal S\), with the adverse signs.  This proves (2.3).
Combining with (1.6) proves (0.3).  \(\square\)

No linearity or common choice of the permutations \(g_\omega\) was used.
They may be selected adversarially and adaptively, provided their common
support stays inside \(B\).

## 3. Stationary-pair consequence

Let \(\mathcal P\) be a perfect matching of the \(2m\) coordinates, viewed
as an independent set in \(J(2m,2)\).  Suppose

\[
Z_1(\omega)\in\mathcal P
\qquad
(\omega\in\mathcal V_1(\mathcal D)).
\tag{3.1}
\]

Then

\[
\mu_1^{\mathcal D}(\mathcal P)=N_1,
\qquad
\mu_1^{\mathcal D}(\Gamma_1\mathcal P)=0,
\tag{3.2}
\]

because two different matching edges are disjoint, while
\(\Gamma_1\mathcal P\) contains only pairs meeting some matching edge in
exactly one coordinate and is therefore disjoint from \(\mathcal P\).
All mass lies on \(\mathcal P\).

At \(q=1\), summing the one-design margins over \(2m\) coordinates gives

\[
2m\lambda_1=2N_1,
\qquad
\lambda_1=N_1/m.
\tag{3.3}
\]

Use \(\mathcal S=\mathcal P\) in Theorem 2.1.  Equations
(3.2)--(3.3) give

\[
P_1(\mathcal E)
\ge
\left(1-\frac{2b}{m}\right)_+N_1.
\tag{3.4}
\]

Finally,

\[
\widehat\Phi_H(\mathcal E)
=2\sum_{q=1}^HP_q(\mathcal E)
\ge2P_1(\mathcal E),
\]

which is (0.4).

Since

\[
N_1=\binom{2m}{m-1}=\frac{m}{m+1}W,
\tag{3.5}
\]

the condition \(\widehat\Phi_H(\mathcal E)=o(W)\) forces

\[
1-2b/m=o(1),
\]

and hence (0.5).  \(\square\)

## 4. Frozen-resolution implication

### 4.1 All-depth stationary frames

Assume the stronger condition (0.6).  The label family
\(\mathcal U_q(\mathcal P)\) is independent in \(J(2m,2q)\): two distinct
unions of \(q\) matching edges intersect in at most \(2q-2\) coordinates.
All of the \(\mathcal D\)-mass lies on this family, so its Hall deficiency
is \(N_q\).

The exact one-design margin simplifies to

\[
2m\lambda_q=2qN_q,
\qquad
\lambda_q=\frac q mN_q,
\tag{4.1}
\]

because every label has size \(2q\).  Theorem 2.1 therefore gives

\[
P_q(\mathcal E)
\ge
\left(1-\frac{2bq}{m}\right)_+N_q.
\tag{4.2}
\]

Summing through
\(\widehat\Phi_H=2\sum_{q=1}^HP_q\) proves (0.7).  If
\(H=\lceil A\sqrt m\rceil\) and \(b=o(\sqrt m)\), the multiplier in
(4.2) is \(1-o(1)\) uniformly, while

\[
\frac1{W\sqrt m}\sum_{q=1}^HN_q
\longrightarrow\int_0^Ae^{-x^2}\,dx.
\]

This proves (0.8).

### 4.2 Consequence for a prescribed target orbit

Consider a prescribed target SCD color \(\mathcal D\) satisfying (3.1),
or its complete labelled coordinate orbit.  Suppose a rounding procedure
allows arbitrary statewise permutations supported in one set \(B\), but
keeps a per-color state lineage of the form (0.1) and outputs an exact SCD
color.  Then every output color satisfies (0.4).  In particular, if

\[
b=O(\log m),
\]

its exact rotor-prefix toll is at least

\[
(2-o(1))W.
\tag{4.3}
\]

This conclusion is unaffected by whether \(B\) is aligned with a Catalan
prefix or is the nonaligned reflection support

\[
\{1,\ldots,s,2m+1-s,\ldots,2m\}.
\]

Thus the reflection construction closes the invariant-seed obstruction but
not this genuine Johnson-label obstruction.

The hypothesis which a general packet-palette recoloring can violate is
per-color lineage.  Statewise Birkhoff bijections may transfer a state from
one ancestral color to another.  The exact next dichotomy is therefore:

1. **lineage-preserving rounding:** obstructed by (0.4) until the common
   support is linear, or until the source label-Hall deficiency is removed;
2. **cross-color rebundling:** must be analyzed by the packet-palette
variation \(V_d^*\) or the constrained recursive Hall lift, because no
   rowwise support theorem applies after ancestry is discarded.

## 5. Scope audit

1. Both \(\mathcal D\) and \(\mathcal E\) are genuine full integral SCDs.
2. The bijection preserves radius, as every coordinate permutation does.
3. The permutations may depend on the state; only their common support is
   bounded.
4. The estimate \(b\lambda_q\) is a union bound, so overlaps inside \(B\)
   only improve it.
5. The factor two in (2.3) is necessary in the worst case because moved
   atoms may leave \(\mathcal S\) and enter \(\Gamma_q\mathcal S\).
6. Equation (0.4) is a rotor/SCD theorem, not an FSP packet theorem.
7. Odd-wreath row lineage from component switching does not by itself give
   (0.1) for the chain states of one resolved SCD color.  No such bridge is
   silently assumed.
8. The theorem does not obstruct a source SCD whose label measure is already
   Hall-diffuse, nor a recoloring which performs genuine cross-color
   rebundling.
9. No repository theorem constructs a centrally
   \(\mathcal P\)-paired full SCD satisfying (3.1) for all \(m\); the
   all-depth condition (0.6) is stronger still.  Equations (0.4)--(0.8) are
   conditional applications of Theorem 2.1, not unconditional construction
   barriers.

The unconditional advance is Theorem 2.1: every **already existing**
label-Hall witness is stable under rowwise common-support relabeling with
the exact loss \(2b\lambda_q\).  Its stationary-frame consequences apply
only when that source and the lineage-preserving rounding are independently
constructed.
