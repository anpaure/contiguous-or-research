# Repaired promotion rings: ideal density for every small matching-number mesh

Date: 2026-07-26

Method: pure mathematics.  This note audits and extends
`MATH_THEOREM_REPAIRED_RING_EKR_AND_NONSTAR_CLIQUES_20260726.md`.

## 0. Outcome

Let \(\mathcal G\) be the packing-side repaired-ring hypergraph.  An edge
has one root and \(M-1\) middle owners, so its size is

\[
 k=M=m+H.
\]

Retain the notation

\[
 D=D_T=M!,\qquad
 C_1={2(M-2)((m-1)!)^2\over(m-H)!},
\]

and put

\[
 s:=\max_{v,\ f\not\ni v}\sum_{z\in f}d_{\mathcal G}(v,z).
\tag{0.1}
\]

The link estimates in the EKR note give

\[
 s\le(4+o(1))C_1
   =\left({8+o(1)\over m^2}\right)D.
\tag{0.2}
\]

The following extends the clique theorem (the case \(r=1\)).

> **Small-mesh density theorem.**  Let \(\mathcal B\subseteq
> E(\mathcal G)\), and write \(r=\nu(\mathcal B)\).  If
> \[
>                 r\le {D\over ks},
> \tag{0.3}
> \]
> then
> \[
> \boxed{|\mathcal B|\le D\,\nu(\mathcal B).}
> \tag{0.4}
> \]

In the repaired-ring parameters,

\[
 {D\over ks}\ge\left({1\over8}-o(1)\right)m.
\tag{0.5}
\]

Consequently every cardinality matching-polytope obstruction

\[
                  |\mathcal B|>D\nu(\mathcal B)
\tag{0.6}
\]

must already have

\[
 \boxed{\nu(\mathcal B)>\left({1\over8}-o(1)\right)m.}
\tag{0.7}
\]

Thus the rooted promotion catalogue has no clique obstruction, no
triangle/odd-cycle gadget of bounded matching number, and in fact no
\(o(m)\)-matching **unweighted odd mesh**.  The first possible cardinality
obstruction is necessarily mesoscopic and globally supported.

This does not prove a near-perfect matching and does not settle arbitrary
weighted fractional-edge-colouring duals.  It does materially sharpen the
boundary: a failure of the desired matching theorem cannot be certified by
replicating any fixed finite obstruction, nor by an obstruction whose
matching number grows sublinearly in \(m\).

## 1. Audit of the EKR link estimates

For completeness, the two inputs used below are valid for the formal
repaired-ring convention.

1. If \(v=U\) is a root and \(f\) avoids \(U\), at most \(H\) owner
   windows of \(f\) lie in \(U\).  Each corresponding root--owner
   codegree is \((M-1)m!H!\).  Hence
   \[
   \sum_{z\in f}d(U,z)
   \le H(M-1)m!H!=o(C_1).
   \tag{1.1}
   \]

2. If \(v=X\) is an owner and \(f\) avoids \(X\), at most four owner
   windows of \(f\) are at Johnson distance one from \(X\).  Their
   codegrees are at most \(C_1\).  The root contribution is \(o(C_1)\),
   and all remaining owner contributions total \(MC_2=o(C_1)\), since
   \(C_2/C_1=4/(m-1)^2\).  Therefore
   \[
   \sum_{z\in f}d(X,z)\le(4+o(1))C_1.
   \tag{1.2}
   \]

The proof of the four-window assertion in the EKR note is also correct.
If \(a=|X\setminus V|\), Johnson distance one forces \(a\in\{0,1\}\)
and forces a cyclic \(m\)-window in \(V\) to contain exactly one zero of
the binary word \(V\setminus X\).  At most two zeroes have adjacent
one-gap sum at least \(m-1\); each supplies at most two windows when
\(a=0\), and at most one when \(a=1\).  Deleting one phase from a repaired
ring can only lower this count.

Equations (1.1)--(1.2) prove (0.2).  Notice also that every vertex degree
is at most \(D\): root degree is exactly \(D\), while owner degree is
strictly smaller.

## 2. A general small-mesh peeling lemma

### Lemma 2.1

Let \(\mathcal H\) be a \(k\)-uniform hypergraph of maximum vertex degree
at most \(D\).  Suppose

\[
 \max_{v,\ f\not\ni v}\sum_{z\in f}d_{\mathcal H}(v,z)\le s.
\tag{2.1}
\]

Then every edge family \(\mathcal B\subseteq E(\mathcal H)\) with
matching number \(r\le D/(ks)\) satisfies

\[
                         |\mathcal B|\le rD.
\tag{2.2}
\]

#### Proof

We induct on \(r\).  The assertion is empty for \(r=0\).  Assume
\(r\ge1\).

First suppose some vertex \(v\) has

\[
                         d_{\mathcal B}(v)>rs.
\tag{2.3}
\]

Put \(\mathcal B'=\{e\in\mathcal B:v\notin e\}\).  If
\(\mathcal B'\) had a matching \(f_1,\ldots,f_r\), then every member of
\(\mathcal B\) containing \(v\) would have to meet
\(f_1\cup\cdots\cup f_r\); otherwise it would augment that matching.
The union bound and (2.1) would give

\[
 \begin{aligned}
 d_{\mathcal B}(v)
 &\le\sum_{i=1}^r\sum_{z\in f_i}d_{\mathcal H}(v,z)\\
 &\le rs,
 \end{aligned}
\]

contrary to (2.3).  Hence \(\nu(\mathcal B')\le r-1\).  By induction and
the maximum-degree bound,

\[
 |\mathcal B|
 =d_{\mathcal B}(v)+|\mathcal B'|
 \le D+(r-1)D=rD.
\tag{2.4}
\]

It remains to treat the case

\[
                         d_{\mathcal B}(v)\le rs
                         \quad\text{for every }v.
\tag{2.5}
\]

Let \(f_1,\ldots,f_r\) be a maximum matching.  Its vertex union is a
vertex cover of \(\mathcal B\), since an edge avoiding it would augment
the matching.  Therefore

\[
 |\mathcal B|
 \le\sum_{v\in f_1\cup\cdots\cup f_r}d_{\mathcal B}(v)
 \le rk\,rs
 \le rD,
\tag{2.6}
\]

where the final inequality is precisely \(r\le D/(ks)\).  This completes
the induction. \(\square\)

## 3. Application and exact constant

Apply Lemma 2.1 with \(k=M\), \(D=D_T\), and (0.2).  Since

\[
 {C_1\over D_T}={2+o(1)\over m^2},\qquad M=(1+o(1))m,
\]

we obtain the conservative bound

\[
 {D_T\over Ms}
 \ge {D_T\over M(4+o(1))C_1}
 =\left({1\over8}-o(1)\right)m.
\]

This proves (0.4)--(0.7).

## 4. Consequences and boundary

### 4.1 What is eliminated

The theorem eliminates every **unweighted** obstruction obtained from a
subcatalogue \(\mathcal B\) with

\[
                  |\mathcal B|>D_T\nu(\mathcal B)
\]

and \(\nu(\mathcal B)=o(m)\).  In particular, fixed odd-cycle gadgets,
bounded projective-plane gadgets, replicated triangle gadgets, and all
other finite matching-number templates cannot create the factor gap.

### 4.2 Why this is not yet fractional edge colouring

The dual of fractional edge colouring permits arbitrary nonnegative
weights \(w\) subject to \(w(Q)\le1\) for every matching \(Q\).  The
unweighted density inequalities (0.4) do not automatically control such
weights.  Threshold integration yields only logarithmic losses in general,
and weighted star peeling requires a spread hypothesis on the weighted
pair links.  Therefore no claim

\[
                       \chi_f'(\mathcal G)=(1+o(1))D_T
\]

is made here.

### 4.3 What remains possible

A cardinality obstruction can survive only with matching number
\(\Omega(m)\); a weighted obstruction can survive only by concentrating
on a globally coherent family not detected by the full-catalogue
codegrees.  Either type is qualitatively different from every local
odd-gadget explanation considered so far.
