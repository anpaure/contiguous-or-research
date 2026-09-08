# Optional middle cores: threshold families defeat small-centre containers

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional structural obstruction and exact collar audit.
The canonical one-point DM condition, sublinear protected-owner exposure,
and balanced-collar transition identities do **not** imply that an optional
core is a union of \(o(\sqrt{\log r})\) principal stars or two-sided
Boolean intervals. This note does not construct a positive canonical DM
maximizer for the audited three-palette bank.

## 0. Threshold family

Put

\[
 n=2r-1,\quad k=r-1,\quad
 \mathcal L=\binom{[n]}k,\quad
 \mathcal U=\binom{[n]}r,\quad W=|\mathcal L|=|\mathcal U|.
\tag{0.1}
\]

Fix an even \(g=2t\), where \(4\le g=o(r)\), and
\(S\subset[n]\), \(|S|=g\). Define

\[
 \mathcal A=\{x\in\mathcal L:|x\cap S|\ge t\},\qquad
 \mathcal B=\{x\in\mathcal L:|x\cap S|\le t-1\}.
\tag{0.2}
\]

## 1. Exact interval-cover complexity

A two-sided Boolean interval has rank-\(k\) slice

\[
 [C,T]_k=\{x\in\mathcal L:C\subseteq x\subseteq T\}.
\tag{1.1}
\]

### Lemma 1.1 (row-or-column rigidity)

Let \([C,T]_k\ne\varnothing\) be contained in \(\mathcal B\). On

\[
 \mathcal E=\{x\in\mathcal L:|x\cap S|=t-1\},
\tag{1.2}
\]

the interval fixes either the complete \(S\)-part or the complete
\([n]\setminus S\)-part. Namely, if
\(x=R\mathbin{\dot\cup}O\in[C,T]_k\cap\mathcal E\), then

\[
 R=T\cap S\qquad\hbox{or}\qquad O=C\setminus S.
\tag{1.3}
\]

#### Proof

The largest possible \(S\)-intersection of a rank-\(k\) member of the
interval is

\[
 \min\{|T\cap S|,\ k-|C\setminus S|\}.
\tag{1.4}
\]

It is at most \(t-1\). If the interval contains \(x\), both arguments of
the minimum are at least \(t-1\). Hence one equals \(t-1\), giving the
corresponding equality in (1.3). \(\square\)

### Theorem 1.2 (exact interval-cover number)

For all sufficiently large \(r\),

\[
 \boxed{\tau_\square(\mathcal B)=\binom g{t-1}.}
\tag{1.5}
\]

This remains a lower bound for covers mixing arbitrary two-sided
intervals and principal up-stars.

#### Proof

Identify \(\mathcal E\) with the edges of

\[
 K_{a,b},\qquad
 a=\binom g{t-1},\qquad
 b=\binom{n-g}{k-t+1}=\binom{n-g}{r-t}.
\tag{1.6}
\]

Lemma 1.1 puts the boundary part of each interval in one row-star or one
column-star. Fewer than \(a\) rows and fewer than \(b\) columns leave an
edge uncovered, so a cover has size at least \(\min\{a,b\}=a\);
eventually \(b>a\) because \(g=o(r)\).

Conversely, for every \(R\in\binom S{t-1}\), take

\[
 [\varnothing,([n]\setminus S)\cup R]_k.
\tag{1.7}
\]

These \(a\) intervals cover exactly \(\mathcal B\). \(\square\)

Thus

\[
 \tau_\square(\mathcal B)=\exp(\Theta(g)).
\tag{1.8}
\]

For even \(g=(\log r)^{2/3}+O(1)\), this is far larger than
\(o(\sqrt{\log r})\), despite the one-line threshold description.

## 2. The one-point DM property does not force a small cover

Let \(P\) be any protected path forest and put

\[
 Z=\{x\in\mathcal L:d_P(x)=2\},\quad
 X=\mathcal L\setminus Z,
\tag{2.1}
\]

\[
 \alpha(P)=\max_{x\in X}|\{U\supset x:d_P(U)>0\}|.
\tag{2.2}
\]

Set \(B=\mathcal B\cap X\). For \(x\in B\), let \(q_B^-(x)\) count
owners satisfying

\[
 |B\cap G_U|\ge g_U-c_U+1,\qquad
 G_U=N(U)\cap X,\quad g_U=|G_U|,\quad c_U=2-d_P(U).
\tag{2.3}
\]

### Theorem 2.1 (robust full-gap threshold family)

\[
 \boxed{q_B^-(x)\ge r-g-\alpha(P)\qquad(x\in B).}
\tag{2.4}
\]

#### Proof

Write \(j=|x\cap S|\le t-1\). There are

\[
 |[n]\setminus(S\cup x)|=r-g+j\ge r-g
\tag{2.5}
\]

choices \(a\notin S\cup x\). For \(U=x\cup\{a\}\), every facet still has
\(S\)-intersection at most \(j\), so \(G_U\subseteq B\). If \(U\) is
unprotected, \(c_U=2\) and

\[
 |B\cap G_U|=g_U\ge g_U-1=g_U-c_U+1.
\]

At most \(\alpha(P)\) of the owners are protected. \(\square\)

Hence \(g=o(r)\) and \(\alpha(P)=o(r)\) give
\(q_B^-(x)=\Omega(r)\), much stronger than the canonical lower bound
three. This is independent of

\[
 \beta(P)=\max_U|N(U)\cap Z|,
\]

because every witnessing optional gap above is completely full. Therefore

\[
 q_B^-(x)\ge3,\qquad \alpha(P),\beta(P)=o(r)
\tag{2.6}
\]

cannot alone imply a small-centre representation.

This is scoped: \(B\) is not asserted to be a positive or canonical
maximizer. The theorem shows that the strongest presently used *local
consequence* of canonical minimality is compatible with interval-cover
complexity \(\exp(\Theta(g))\).

## 3. A literal oscillating balanced collar

Let \(g\le h\le r-2\). Choose disjoint

\[
 Q,\quad\lambda_1,\ldots,\lambda_h,\quad
 \rho_1,\ldots,\rho_h,\quad z,
\tag{3.1}
\]

where \(|Q|=r-h\), \(Q\cap S=\varnothing\), and \(z\notin S\).
Arrange the rails by

\[
 \begin{array}{c|cc}
  &\lambda_i&\rho_i\\ \hline
  i\le g,\ i\ {\rm odd}&S&[n]\setminus S\\
  i\le g,\ i\ {\rm even}&[n]\setminus S&S\\
  i>g&[n]\setminus S&[n]\setminus S,
 \end{array}
\tag{3.2}
\]

using every member of \(S\) exactly once among the first \(g\) rail
labels. Put

\[
 M_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
          \cup\{\rho_1,\ldots,\rho_j\},\quad0\le j\le h.
\tag{3.3}
\]

For \(q_-,q_+\in Q\), define seam owners

\[
 P_-=M_0-q_-+\rho_1,\qquad P_+=M_h-q_++z.
\tag{3.4}
\]

The outside-coordinate count leaves \(r-h-2\ge0\) unused coordinates,
so these data exist. They are exactly a generalized balanced collar.

### Theorem 3.1 (exact threshold oscillation)

For

\[
 \mathcal C=(P_-,M_0,\ldots,M_h,P_+),
\]

\[
 \boxed{\sum_{e\in E(\mathcal C)}w_{\mathcal A}(e)=g.}
\tag{3.5}
\]

#### Proof

Exactly the \(t\) odd-indexed \(\lambda\)-labels of \(M_0\) lie in \(S\).
Thus \(|M_j\cap S|\) alternates

\[
 t,t-1,t,t-1,\ldots,t-1,t
\tag{3.6}
\]

through the first \(g\) transitions and then stays \(t\). For
\(j\le g\), the common lower colour has \(S\)-intersection \(t-1\), and
exactly one endpoint belongs to \(N(\mathcal A)\), so the charge is one.
For \(j>g\), the common lower colour belongs to \(\mathcal A\), so the
charge is zero. Both seam lower colours have \(S\)-intersection \(t\),
because all four seam labels lie outside \(S\); their charges vanish.
\(\square\)

Thus literal balanced-collar geometry does not restore a constant
threshold aperture: one collar makes \(g\) coherent crossings even though
every coordinate is exchanged at most twice.

## 4. Exact slack and conditional aligned-bank failure

Put

\[
 N_j=\binom gj\binom{n-g}{r-j}.
\tag{4.1}
\]

### Theorem 4.1 (threshold Ore slack)

If \(r-t\ge2\), then

\[
 \boxed{\sigma(\mathcal A)={2t\over r}N_t={g\over r}N_t.}
\tag{4.2}
\]

If \(g=o(\sqrt r)\) and \(g\to\infty\), then

\[
 {N_t\over W}
  =(1+o(1))\binom g{g/2}2^{-g}
  =(\sqrt{2/\pi}+o(1))g^{-1/2}.
\tag{4.3}
\]

#### Proof

Owners below \(t\) have no selected facet. At level \(t\), exactly
\(r-t\ge2\) facets are selected. Above \(t\), all \(r\) are selected.
Therefore

\[
 \sigma(\mathcal A)=2(|N(\mathcal A)|-|\mathcal A|).
\tag{4.4}
\]

Counting lower-to-upper incidences gives

\[
 r|\mathcal A|=(r-t)N_t+r\sum_{j>t}N_j.
\tag{4.5}
\]

Since \(|N(\mathcal A)|=N_t+\sum_{j>t}N_j\), (4.2) follows.
Equation (4.3) is the central-binomial estimate; sampling
\(g=o(\sqrt r)\) fixed coordinates without replacement differs
multiplicatively from Bernoulli-\(1/2\) sampling by
\(\exp(O(g^2/r))=1+o(1)\). \(\square\)

### Corollary 4.2 (conditional exact Hall failure)

Suppose a three-palette-disjoint bank \(P\) consists of

\[
 b={W\over2r-1}-1
\tag{4.6}
\]

collars from Theorem 3.1 and satisfies

\[
 \beta(P)\le r-t-2.
\tag{4.7}
\]

Then the residual Hall cut \(\mathcal A\setminus Z\) has exact slack

\[
 \boxed{\sigma(\mathcal A)-bg,}
\tag{4.8}
\]

and is deficient for all sufficiently large \(g\).

#### Proof

Every owner in \(N(\mathcal A)\) has at least \(r-t\) selected facets
before deleting \(Z\). Condition (4.7) leaves at least two, so every owner
saturates its residual capacity. Hence

\[
 \begin{aligned}
 \kappa(\mathcal A\setminus Z)-2|\mathcal A\setminus Z|
  =\sigma(\mathcal A)
  -\left(\sum_{U\in N(\mathcal A)}d_P(U)
         -2|Z\cap\mathcal A|\right).
 \end{aligned}
\tag{4.9}
\]

Expanding the parenthesized term over protected incidences and grouping
the two incidences through each protected lower colour identifies it with
\(c_P(\mathcal A)=\sum_{e\in P}w_{\mathcal A}(e)\). Theorem 3.1 gives
\(c_P=bg\). Finally,

\[
 {bg\over\sigma(\mathcal A)}
   =(\sqrt{\pi/8}+o(1))\sqrt g\longrightarrow\infty
\tag{4.10}
\]

by (4.2)--(4.3) and \(b=(1+o(1))W/(2r)\). \(\square\)

No existence of the globally disjoint aligned bank assumed in Corollary
4.2 is claimed. The result is exact about what a future co-selection
theorem must forbid. Neither scalar capacity, the isotropic all-edge
identity, nor one-collar geometry forbids it.

## 5. Correct replacement target

Take even \(g=(\log r)^{2/3}+O(1)\). Then

\[
 g=o(h),\qquad g=o(\sqrt r),\qquad
 \binom g{g/2-1}=\exp(\Theta((\log r)^{2/3})).
\tag{5.1}
\]

The desired “few stars/subcubes” conclusion cannot be derived from the
current local inputs. But threshold families have low **description
entropy**: for fixed \(g\), there are at most

\[
 (g+1)\binom ng=\exp(O(g\log r))
\tag{5.2}
\]

such descriptions. The plausible replacement is therefore:

> **Global optional-core container gate.** Use full canonical maximality,
> not merely \(q_B^-\ge3\), to place every positive middle core inside a
> low-entropy exact coordinate-profile container; then co-select the
> collar bank so that
> \[
>   \sum_{C\in P}w_A(C)\le\sigma(A)
> \]
> for every such container.

The present note proves that deleting “coordinate-profile” and retaining
only “few principal stars/two-sided subcubes” makes that statement false
at the level of the currently available structural inputs.

## 6. Exact scope

This note does **not** prove:

1. that \(\mathcal B\cap X\) is a positive or canonical maximizer for
   the audited collar bank;
2. that the aligned bank in Corollary 4.2 exists;
3. that the actual three-palette bank fails its factor gate; or
4. that no broader low-entropy exact-container theorem exists.

It proves a scoped no-go for the small-centre deduction and identifies
global energy/container co-selection as the missing premise.

## 7. Dependencies

The notation and identities are from
MATH_THEOREM_OPTIONAL_CO_SMALL_CHARGING_LP_EXACT_FACTOR_EQUIVALENCE_20260804.md,
MATH_THEOREM_SUBLINEAR_EXPOSURE_PROTECTED_FACTOR_SMALL_CUT_AND_OPTIONAL_CORE_REDUCTION_20260805.md,
MATH_THEOREM_PIVOT_GLUING_UPPER_Q1_CAPACITY_AND_BALANCED_SEAM_COLLAR_20260805.md,
and MATH_THEOREM_CATALAN_COLLAR_ORE_ISOTROPIC_MEAN_AND_ENTROPY_BARRIER_20260805.md.
