# Audit: the collision objective is not controlled by fractional flow or pair codegrees

Date: 2026-07-27

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Verdict

For the fixed-core configuration hypergraph of
`MATH_AUDIT_AND_THEOREM_COMMON_CORE_TIGHT_PATH_FUSION_20260726.md`, the
right integral objective is indeed

\[
 K^*=\min \sum_{v:\lambda_v>0}(\lambda_v-1).
\tag{0.1}
\]

It is strictly weaker than finding a near-perfect matching.  However, it
does **not** follow from any combination of the following presently audited
inputs:

* a fractional point of value one in every root fibre and load at most one
  on every physical target;
* exact integrality of every individual root fibre (in particular, a
  Birkhoff or network extended formulation);
* exact regularity of roots and targets;
* arbitrarily large catalogue degree; and
* maximum normalized pair codegree \(O(m^{-2})\).

Theorem 2.1 below constructs a catalogue with all of these properties in
the same parameter range

\[
       N\asymp W/m,\qquad k\asymp m^{3/2},\qquad
       \Delta_2/D=O(m^{-2}),
\tag{0.2}
\]

but for which every one-configuration-per-root selection has

\[
                         K\ge {1\over8}Nk.
\tag{0.3}
\]

Thus \(K\) is not merely non-\(o(W)\); it is a positive fraction of the
entire target-occurrence mass \(Nk\asymp W\sqrt m\).

This is not a counterexample inside the literal interval catalogue
\(\mathcal K_{\mathbf Q}\).  Its conclusion is instead a rigorous audit
boundary: a proof of \(K^*(\mathcal K_{\mathbf Q})=o(W)\) must use a
higher-order interval/diagonal-shell property.  Fractional flow, local
order integrality, degree regularity, and pair spread alone cannot prove
it.  The depth-one common-support cut is genuinely useful locally, but it
does not address the collective obstruction exhibited here.

## 1. Exact max-coverage formulation

Let the roots be \(u\in\mathcal U\), with one configuration fibre
\(\mathcal E(u)\) at each root.  Every configuration contains exactly
\(k\) physical targets.  For an integral selection \(e_u\in\mathcal E(u)\),
write

\[
 \lambda_v=|\{u:v\in e_u\}|,
 \qquad
 K(e)=\sum_v(\lambda_v-1)_+.
\tag{1.1}
\]

If \(B\) is the number of protected targets and

\[
                         \Delta=B-k|\mathcal U|,
\tag{1.2}
\]

then, exactly as in Theorem 6.0 of the common-core audit,

\[
 B-|\{v:\lambda_v>0\}|=\Delta+K(e).
\tag{1.3}
\]

Consequently

\[
 K^*=k|\mathcal U|-\max_{e_u\in\mathcal E(u)}
                      |\bigcup_u e_u|.
\tag{1.4}
\]

So \(K^*\) is exactly the integral gap of a partition-constrained maximum
coverage problem.

Its standard relaxation is

\[
 \sum_{e\in\mathcal E(u)}x_e=1,qquad x_e\ge0,
\tag{1.5}
\]

\[
 0\le y_v\le1,qquad
 y_v\le\sum_{e\ni v}x_e,
\tag{1.6}
\]

with objective \(\max\sum_vy_v\).  The dual can be written

\[
 \min_{0\le a_v\le1}
 \left[
   \sum_v(1-a_v)
   +\sum_{u\in\mathcal U}
       \max_{e\in\mathcal E(u)}\sum_{v\in e}a_v
 \right].
\tag{1.7}
\]

For the fixed-core fractional point, (1.5)--(1.6) has value
\(B-\Delta\).  Formula (1.7) shows why this by itself gives no integral
rounding: it is the concave closure of coverage, whereas (1.4) asks for an
integral point of the partition product.

The next theorem shows that this gap remains maximal under exact
regularity and vanishing normalized pair codegree.

## 2. A regular low-codegree statewise obstruction

### Theorem 2.1 (rainbow-line obstruction)

Let \(m\to\infty\).  There are integers

\[
 R\in[m^2,2m^2],\qquad k=\lfloor m^{3/2}\rfloor,
\tag{2.1}
\]

and arbitrarily large root sets \(\mathcal U\), together with a
\((k+1)\)-uniform configuration hypergraph whose vertices consist of the
roots and a physical target set \(\mathcal V\), such that:

1. every configuration contains one root and exactly \(k\) targets;
2. every root and every target has the same degree \(D\), where \(D\) may
   be made arbitrarily large;
3. every pair of distinct vertices has codegree at most
   
   \[
                              {D\over R}=O(D/m^2);
   \tag{2.2}
   \]
4. the uniform vector \(x_e=1/D\) saturates every root and every target;
5. every root fibre is a simplex, hence is integrally closed and has an
   exact local network formulation; but
6. every integral choice of one configuration at every root satisfies
   
   \[
                 K(e)\ge {1\over8}|\mathcal U|k.
   \tag{2.3}
   \]

Moreover

\[
                       |\mathcal V|=|\mathcal U|k,
\tag{2.4}
\]

so the scalar deficit \(\Delta\) in (1.2) is exactly zero.

#### Proof

By Bertrand's postulate choose a prime \(R\in[m^2,2m^2]\).  Work first on
one copy of the affine space

\[
                             \mathcal U_0=\mathbb F_R^3.
\tag{2.5}
\]

Choose \(k\) distinct one-dimensional directions.  This is possible
because the number of directions is

\[
                         R^2+R+1>k.
\tag{2.6}
\]

Let \(\mathcal C\) be all affine lines in those directions.  Every line
contains \(R\) roots, every root lies on exactly \(k\) selected lines, and
two distinct lines meet in at most one root.  Hence, writing
\(N_0=|\mathcal U_0|\) and \(M_0=|\mathcal C|\),

\[
                              M_0R=N_0k.
\tag{2.7}
\]

For every incidence \(u\in C\), independently choose a uniform
permutation

\[
                         \pi_{C,u}:[R]\longrightarrow[R].
\tag{2.8}
\]

We first prove that the permutations can be chosen so that every labeling
\(a:\mathcal U_0\to[R]\) has large rainbow defect.  For a line \(C\), put

\[
 Z_C(a)=R-
   |\{\pi_{C,u}(a(u)):u\in C\}|,
 \qquad Z(a)=\sum_{C\in\mathcal C}Z_C(a).
\tag{2.9}
\]

For one fixed labeling \(a\), the \(RM_0=N_0k\) displayed values in
(2.9) are independent uniform elements of ([R]).  Thus

\[
 \mathbb E Z_C(a)
 =R\left(1-{1\over R}\right)^R\ge {R\over4},
\tag{2.10}
\]

and

\[
                              \mathbb EZ(a)\ge {N_0k\over4}.
\tag{2.11}
\]

Changing one displayed value changes \(Z(a)\) by at most one.  McDiarmid's
bounded-difference inequality therefore gives

\[
 \Pr\left(Z(a)<{N_0k\over8}\right)
 \le \exp(-N_0k/32).
\tag{2.12}
\]

There are \(R^{N_0}\) labelings.  Since \(k/32>\log R\) for all
sufficiently large \(m\), the union bound is less than one.  Hence there
is one deterministic choice of all permutations for which

\[
                         Z(a)\ge {N_0k\over8}
 \quad\hbox{for every }a:\mathcal U_0\to[R].
\tag{2.13}
\]

Take any number of disjoint copies of this incidence system; (2.13) adds
over the copies, giving arbitrarily large root sets.

For every line \(C\) and label \(b\in[R]\), create a target vertex
\(v_{C,b}\).  At a root \(u\), for every label \(a\in[R]\), create the
configuration

\[
 e_{u,a}=\{u\}\cup
          \{v_{C,\pi_{C,u}(a)}:C\ni u\}.
\tag{2.14}
\]

It contains exactly one target for each of the \(k\) lines through \(u\).
Finally, replace every \(e_{u,a}\) by \(L\) parallel labeled copies, where
\(L\ge1\) is arbitrary.  Then

\[
                              D=RL.
\tag{2.15}
\]

Every root has degree \(RL\).  A target \(v_{C,b}\) has, for each of the
\(R\) roots \(u\in C\), exactly one label
\(a=\pi_{C,u}^{-1}(b)\), hence also has degree \(RL\).

For codegrees, a root and one incident target occur together in exactly
\(L\) configurations.  Two targets belonging to the same line never occur
together.  If they belong to different lines, those lines have at most one
common root, and at that root at most one label can realize both prescribed
values.  Their codegree is therefore at most \(L=D/R\).  Two roots never
occur together.  This proves (2.2).

The uniform weight (1/D) plainly gives load one at every root and every
target.  Also

\[
 |\mathcal V|=M_0R=N_0k
\tag{2.16}
\]

on each copy, proving (2.4).

An integral one-per-root selection is exactly a labeling \(a(u)\); the
parallel-copy index is irrelevant.  On line \(C\), its target collision
excess is

\[
 \sum_{b\in[R]}(\lambda_{C,b}-1)_+
 =R-|\{\pi_{C,u}(a(u)):u\in C\}|=Z_C(a).
\tag{2.17}
\]

Summing (2.17) and using (2.13) gives (2.3).  Finally, each root fibre is
just the convex hull of finitely many unit vectors (with harmless parallel
labels), so it is a simplex and is integral. \(\square\)

## 3. What the theorem rules out

Set abstractly

\[
                     |\mathcal U|\asymp {W\over m},
 \qquad k\asymp m^{3/2}.
\tag{3.1}
\]

Then Theorem 2.1 has the same root count, configuration rank, and diffuse
pair-codegree scale as the common-core gate, but

\[
 K^*\ge c|\mathcal U|k\asymp W\sqrt m.
\tag{3.2}
\]

In particular, none of the following implications is valid in general:

\[
 \begin{gathered}
 \hbox{fractional root saturation + target capacities}
 \Longrightarrow K^*=o(W),\\
 \hbox{the above + }\Delta_2/D=O(m^{-2})
 \Longrightarrow K^*=o(W),\\
 \hbox{the above + integral local root polytopes}
 \Longrightarrow K^*=o(W).
 \end{gathered}
\tag{3.3}

The obstruction is genuinely collective.  Its constraint supports are
affine lines and any two meet in at most one root.  Each individual line
admits a perfect rainbow labeling, and every individual root choice is a
complete legal local history.  Nevertheless the independently twisted
line requirements cannot be made even approximately rainbow
simultaneously.

This is the global analogue of the determinant-\(2\) triangle from the
common-core audit, amplified to the full asymptotic scale while preserving
vanishing pair codegree.  A first- or second-moment rounding theorem cannot
distinguish it from the desired catalogue.

## 4. Consequence for the fixed-core route

Theorem 2.1 does **not** prove that

\[
                    K^*(\mathcal K_{\mathbf Q})\not=o(W).
\tag{4.1}
\]

The affine-line target system need not be representable by literal
sliding deletion intervals.  What it proves is that the presently audited
scalar data stop strictly before (4.1): the literal interval geometry has
to be used at order at least three.

The first depth-one common-support theorem identifies the first such local
condition,

\[
 r_-(A)+r_+(\mathcal X\setminus A)\ge b.
\tag{4.2}
\]

But (4.2) is a one-top, two-sided flow cut.  The rainbow-line obstruction
has no one-top defect at all; its failure is a simultaneous cocycle of many
target rows.  Therefore even proving every depth-one common-support cut for
every top would not, by itself, imply \(K^*=o(W)\).

The next viable positive theorem must exclude the rainbow-line mechanism
by a property specific to sliding intervals.  Three concrete candidates
are:

1. a higher-order diagonal-shell/cocycle identity which forces the target
   twists around every affine-line analogue to have zero holonomy;
2. a literal multi-top exchange theorem whose moves generate all such
   cocycles while charging \(o(W)\) collision mass; or
3. a hereditary all-weights decomposition theorem for the actual interval
   catalogue, stronger than degree and pair-codegree control.

Absent one of these, the exact status remains

\[
 \boxed{
 \text{the fractional fixed-core flow is complete, but }K^*=o(W)
 \text{ is still an independent global theorem.}}
\tag{4.3}
\]
