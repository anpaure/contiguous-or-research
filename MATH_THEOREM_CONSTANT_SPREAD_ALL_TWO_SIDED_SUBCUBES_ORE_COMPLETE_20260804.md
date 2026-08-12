# Constant-spread reservoir: every two-sided Boolean subcube passes protected Ore

**Date:** 2026-08-04  
**Status:** unconditional asymptotic pure-mathematical theorem.  For the
single alternative-random, constant-spread common-core reservoir, it closes
the protected Ore inequality on every lower-shore Boolean interval
\(\mathcal A(C,S)\).  It combines the exact two-boundary ledger with the
exact singleton-partition gluing identity.  It does not classify arbitrary
positive-defect cuts as Boolean intervals and does not address component
placement or the common cap.

## 0. Setting and frozen inputs

Put

\[
 n=2m-1,\qquad \mathcal L={{[n]}\choose {m-1}}.
\]

Choose the alternative-random constant-spread reservoir `P` from
`MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md`.
For all sufficiently large \(m\), it satisfies

\[
 \ell_P(X):=\lambda_P(\{X\})\le R_0=10
 \qquad(X\in\mathcal L),
\tag{0.1}
\]

and its total incidence size is

\[
                         |E(P)|=2^{m+o(m)}.
\tag{0.2}
\]

Fix

\[
 C\subseteq S\subseteq[n],\qquad
 c=|C|\le m-2,\qquad u=n-|S|,
\]

and write

\[
 \rho=m-c,\qquad
 v=|S|-c=m+\rho-1-u,
\]

so that

\[
 \mathcal A(C,S)
 =\{L\in\mathcal L:C\subseteq L\subseteq S\},
 \qquad
 a:=|\mathcal A(C,S)|={v\choose {\rho-1}}.
\tag{0.3}
\]

The audited exact two-boundary ledger gives

\[
 {\sigma(\mathcal A(C,S))\over a}
 =:\gamma(c,u)
 =u-2+{2(m-u)\over\rho},
\tag{0.4}
\]

and

\[
 b(\mathcal A(C,S))
 =c{v\choose\rho}.
\tag{0.5}
\]

It also proves, with

\[
 N_\rho:=H_\rho(m)+m+H_d,
 \qquad H_\rho(m)=\sum_{j=0}^{\rho}{m\choose j},
\tag{0.6}
\]

that

\[
 \lambda_P(\mathcal A(C,S))
 \le \min\{10,u\}a+2N_\rho.
\tag{0.7}
\]

Here \(d=O(\sqrt m)\) and \(H_d=2^{o(m)}\).

## 1. A constant-spread singleton criterion

We record the specialization of the exact block-gluing identity which is
used below.

### Lemma 1.1

Let \(A\subseteq\mathcal L\) have no full owner fibre, and suppose every
partial owner fibre has size at most \(r_0<m\).  Then \(A\) is safe whenever

\[
 {r_0-1\over m-r_0}\,b(A)
 \le (m-12)|A|.
\tag{1.1}
\]

#### Proof

Partition \(A\) into singleton blocks.  Every singleton has protected Ore
margin at least

\[
 (m-2)-R_0=m-12.
\]

At an owner with fibre size \(q\ge2\), the exact singleton gluing penalty
is at most \(q-1\).  Since \(q\le r_0\),

\[
 q-1\le {r_0-1\over m-r_0}(m-q).
\]

Summing over partial owners bounds the total gluing penalty by the left
side of (1.1).  The exact block-gluing identity then proves safety.
\(\square\)

### Corollary 1.2 (the subcube singleton range)

Assume \(c>0\).  Then \(\mathcal A(C,S)\) is safe whenever

\[
 \boxed{
 u+{m-u\over\rho}\ge12.}
\tag{1.2}
\]

#### Proof

The nontrivial internal owner fibres have the common size
\(r_0=\rho=m-c<m\), while the outside fibres have size one.  Thus there is
no full owner.  Moreover

\[
 { {v\choose\rho}\over {v\choose {\rho-1}}}
 ={m-u\over\rho}.
\]

Substituting (0.5) into (1.1), and cancelling \(a\), gives

\[
 {\rho-1\over c}\,c{m-u\over\rho}\le m-12.
\]

This is equivalent to (1.2). \(\square\)

## 2. Uniform binomial separation

The only asymptotic estimate needed for the complementary range is the
following.

### Lemma 2.1

Fix \(u_0\).  Uniformly for

\[
 0\le u\le u_0,\qquad
 \alpha_0m\le\rho\le m,
\]

where \(\alpha_0>0\) is fixed,

\[
 \boxed{
 {m+\rho-1-u\choose\rho-1}
 \ge 2^{\eta m}\bigl(H_\rho(m)+m+H_d\bigr)}
\tag{2.1}
\]

for some \(\eta=\eta(\alpha_0)>0\) and all sufficiently large \(m\).

#### Proof

Write \(\rho=\alpha m\).  The bounded shifts by \(u+1\) affect all
binomial estimates by only a polynomial factor.

For \(\alpha\le1/2\), Stirling's formula, uniformly on
\([\alpha_0,1/2]\), gives

\[
 \log_2 {m+\rho-1-u\choose\rho-1}
 =m\bigl((1+\alpha)\log_2(1+\alpha)
          -\alpha\log_2\alpha\bigr)+O(\log m),
\]

whereas

\[
 \log_2 H_\rho(m)\le mH_2(\alpha)+O(\log m).
\]

The exponent difference is

\[
 (1+\alpha)\log_2(1+\alpha)
 +(1-\alpha)\log_2(1-\alpha),
\tag{2.2}
\]

which is strictly positive for every \(\alpha>0\), hence has a positive
minimum on the displayed compact interval.

For \(\alpha\ge1/2\), use \(H_\rho(m)\le2^m\).  The first exponent above
is increasing in \(\alpha\) and at \(\alpha=1/2\) equals
\((3/2)H_2(1/3)>1\).  Thus it exceeds \(1\) by a uniform positive
constant.  Finally \(m+H_d=2^{o(m)}\), so it is absorbed in the same
exponential gap. \(\square\)

## 3. Complete two-sided closure

### Theorem 3.1

For the constant-spread common-core reservoir and all sufficiently large
\(m\),

\[
 \boxed{
 \lambda_P(\mathcal A(C,S))
 \le\sigma(\mathcal A(C,S))}
\tag{3.1}
\]

for every \(C\subseteq S\subseteq[2m-1]\) with
\(|C|\le m-2\) and \(|S|\ge m-1\).

#### Proof

The endpoint \(c=0\) is a complete-support equality cut, and the endpoint
\(u=0\) is a principal up-star.  Both are already proved safe for this
same constant-spread bank.  We may therefore assume \(c,u>0\).

If (1.2) holds, Corollary 1.2 proves the result.  Suppose it fails:

\[
                         u+{m-u\over\rho}<12.
\tag{3.2}
\]

Then \(u\le11\) and

\[
 \rho>{m-u\over12-u}\ge {m-11\over12}.
\tag{3.3}
\]

First assume \(c\le u\).  Both \(c\) and \(u\) are bounded by eleven, so
\(\rho=m-O(1)\) and

\[
 a={2m-O(1)\choose m-O(1)}=2^{2m-O(\log m)}.
\tag{3.4}
\]

For \(c>0\), the exact scalar (0.4) satisfies

\[
                         \gamma(c,u)\ge {2\over m-1}.
\tag{3.5}
\]

Every local protected loss is at most the number of protected incidences
at that owner, so \(\lambda_P(A)\le|E(P)|\).  Equations (0.2),
(3.4), and (3.5) give

\[
 \lambda_P(A)\le2^{m+o(m)}
 <{2a\over m-1}\le\sigma(A)
\]

for all sufficiently large \(m\).

It remains to assume \(c>u\).  Then necessarily \(u\le10\), because
when \(u=11\), (3.2) implies \(\rho>m-11\), or equivalently \(c<11\).
The exact two-boundary sufficient condition (0.7) reduces in this range to

\[
                         a(c-u)\ge\rho N_\rho.
\tag{3.6}
\]

By (3.3), Lemma 2.1 applies, for all sufficiently large `m`, with
\(\alpha_0=1/13\).  Since
\(c-u\ge1\) and \(\rho\le m\), it gives (3.6) for all sufficiently large
\(m\).  This proves every remaining case. \(\square\)

## 4. What this closes and what it does not

The theorem closes, for one physical reservoir, the entire canonical
interpolation

\[
 \{L:C\subseteq L\subseteq S,\ |L|=m-1\}
\]

between complete-support cuts and principal up-stars.  In particular it
includes the former common-\(G_2\) exceptional face geometry, although the
proof uses the alternative-random constant-spread bank rather than the
incompatible common-\(G_2\) choice.

It does **not** prove that every connected positive-defect Ore cut is a
two-sided Boolean interval or a bounded perturbation of one.  The exact
remaining factor theorem is now an erosion/classification statement:
after extracting complete support blocks and two-sided interval pieces,
show that the residual partial-colex family has enough singleton margin or
enough protected crossing cancellation.

Nor does this theorem prove component placement, cyclic global residence,
or common-cap compatibility.

## 5. Dependencies

| role | file | SHA-256 |
|---|---|---|
| constant-spread reservoir and endpoint closures | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
| exact two-sided ledger/current bound | `MATH_THEOREM_PROTECTED_ORE_TWO_SIDED_SUBCUBE_EXACT_REDUCTION_20260804.md` | `6499abf7abf9536bdfcf421206ad1e56d3b3f9d2ce05258b92cb8873ddb26dd7` |
| exact singleton block-gluing identity | `MATH_THEOREM_PROTECTED_ORE_POSITIVE_DEFECT_BLOCK_GLUE_AND_SHARP_STABILITY_20260804.md` | `b414ed2dea6a3cc7365a054cbea7e664069ae5c9d84e1bdff1c80d79e6ae0980` |
