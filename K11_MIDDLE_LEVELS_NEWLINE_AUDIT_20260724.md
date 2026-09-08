# Independent audit of `K11_MIDDLE_LEVELS_NEWLINE_20260724.md`

## Verdict

**PASS, with two local wording/definition repairs.**

The mathematical content of Theorems 1 and 2, the rank-four and rank-five
specializations, the internal-seam root normal form, and all displayed global
sum audits are correct consequences of
`K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md`.

In particular, the identity singled out for special audit is correct:

\[
\boxed{e_x^{\rm cen}=R_x^{(3)}-1+\mathbf 1_{x\in H}.}
\]

It remains correct for an internal seam and for either boundary seam. I found
no hidden cyclic-index shift in its derivation.

The two repairs are:

1. the opening paragraph inaccurately describes the middle-level path cover as
   arising "after deleting" matching edges; the final matching edge of each
   component is omitted only from the projected Johnson forest and is included
   in the spanning alternating path;
2. Section 4.2 uses \(i_x\) without defining it locally.

Neither issue changes any theorem, equation, or conclusion.

## 1. Inputs checked against the frozen source

The new note uses exactly the following conclusions of the frozen source, and
uses them with the correct indexing.

* The selected rank-five and rank-six targets are paired by a perfect inclusion
  matching.
* Deleting the transitions between the nonempty endpoint-state blocks gives a
  spanning Johnson linear forest with \(c\le 6\) components and \(462-c\)
  edges.
* If a component is directed toward its root, its vertices and matching colors
  have the form
  \[
  P_0,U_0,P_1,U_1,\ldots,P_\ell,U_\ell,
  \qquad U_j=\mathcal M(P_j),\quad P_{j+1}\subset U_j.
  \]
  The final edge \(P_\ell U_\ell\) is the matching edge not used to expand a
  Johnson-forest edge. It is nevertheless the last edge of the alternating
  middle-level path.
* The central matching rules are exactly
  \[
  C_i\mapsto T_i\quad(i<s),\qquad
  C_i\mapsto T_{i-1}\quad(i>s).
  \]
* The source's zero-run identity is
  \[
  \sum_xR_x^{(3)}=m+8-\rho.
  \]
* At \(n_5=133\), the coordinate budget is
  \[
  Z_x+\lambda_x+r_x=65+h_x+2i_x.
  \]

There is no imported assumption beyond these audited facts.

## 2. Audit of the full matching-extension hierarchy

Fix \(X\subseteq[11]\), \(|X|=t\le6\). Across the full perfect matching,

\[
\sum_{P\mapsto U}
\left(\mathbf1_{X\subseteq U}-\mathbf1_{X\subseteq P}\right)
=
\binom{11-t}{6-t}-\binom{11-t}{5-t}
=\Delta_t.
\]

Because \(P\subset U\), every summand is zero or one. Thus \(\Delta_t\)
really is the number of matching edges completing \(X\). Direct evaluation
gives

\[
(\Delta_1,\ldots,\Delta_6)=(42,42,28,14,5,1),
\]

so (1.1) and (3.8) are correct.

On a used edge \(P_j\mapsto U_j\), a completion of \(X\) either has
\(X\subseteq P_{j+1}\), in which case the forest transition enters the
\(X\)-star, or it does not, in which case that transition is a bypass. The
final unused matching edge contributes \(d_X\). Hence

\[
a_X+z_X+d_X=\Delta_t.
\]

For a final edge, \(X\subseteq U_\ell\) occurs either because
\(X\subseteq P_\ell\) or because that edge completes \(X\), and the two cases
are disjoint. Therefore

\[
\mu_X=\sigma_X+d_X.
\]

Along every oriented five-set path, indicator telescoping gives

\[
a_X-b_X=\sigma_X-\tau_X.
\]

Substitution gives

\[
b_X+z_X=\Delta_t-\mu_X+\tau_X.
\]

For \(t\le5\), every noninitial five-set containing \(X\) is reached either
by an internal-star transition or an entering transition, while every
nonroot five-set containing \(X\) leaves by an internal-star or leaving
transition. This proves

\[
h_X+a_X=v_t-\tau_X,\qquad
h_X+b_X=v_t-\sigma_X.
\]

Thus (3.2)--(3.7) all pass. They also remain valid at the endpoint cases
\(t=0\) and \(t=6\) under the stated out-of-range-binomial convention.

### 2.1 Pair, rank-four, and rank-five consequences

For \(t=1\), a bypass is impossible: two distinct five-subsets of one
six-set cannot both omit the same coordinate. Thus \(a_x+d_x=42\), agreeing
with the source's forest-label law.

For \(X=\{x,y\}\), a bypass forces the two adjacent five-sets to omit \(x\)
and \(y\), respectively, so it is exactly an \(x/y\) swap. Equation (3.9)
is correct.

For \(|X|=4\), if both adjacent five-sets contain \(X\), their four-element
intersection is exactly \(X\). Therefore \(h_X\) is precisely the
multiplicity of \(X\) as a lower intersection color. Since the induced
subgraph on the seven five-sets containing \(X\) is a forest,
\(0\le h_X\le6\). Substitution of \(v_4=7\) and \(\Delta_4=14\) gives

\[
h_X+a_X=7-\tau_X,\qquad
h_X+b_X=7-\sigma_X,
\]

and

\[
z_X-h_X=7+\tau_X+\sigma_X-\mu_X.
\]

For \(|X|=5\), the star has one vertex, so \(h_X=0\),
\(a_X=1-\tau_X\), and \(b_X=1-\sigma_X\). Since \(\Delta_5=5\),

\[
z_X+d_X=4+\tau_X,\qquad
z_X=4+\tau_X+\sigma_X-\mu_X.
\]

The endpoint conclusions following (3.14) are therefore valid. In
particular, if all six supersets of \(X\) are omitted, then the binary
quantities \(\tau_X,\sigma_X\le1\) must both equal one.

## 3. Audit of the central-label identity

Put

\[
\gamma_i=\mathbf1_{x\in C_i},\qquad 0\le i\le m-3.
\]

For \(i<s\), the edge \(C_i\mapsto T_i=C_i\cup C_{i+1}\) adds \(x\)
exactly at a \(0\to1\) transition of \(\gamma\). For \(i>s\), the edge
\(C_i\mapsto T_{i-1}=C_{i-1}\cup C_i\) adds \(x\) exactly at a
\(1\to0\) transition from \(\gamma_{i-1}\) to \(\gamma_i\).

Every zero run of \(\gamma\) strictly left of \(s\) contributes its right
boundary, and every zero run strictly right of \(s\) contributes its left
boundary. If \(\gamma_s=0\), the unique zero run containing \(s\) contributes
neither; if \(\gamma_s=1\), every zero run is counted. Consequently

\[
e_x^{\rm cen}=Z_0(\gamma)-\mathbf1_{\gamma_s=0}.
\]

This reasoning has the correct boundary convention:

* when \(s=0\), only \(1\to0\) transitions with \(i>0\) are counted, so the
  initial zero run is the unique possible uncounted run;
* when \(s=m-3\), only \(0\to1\) transitions with \(i<s\) are counted, so
  the terminal zero run is the unique possible uncounted run.

A zero run of length \(\ell\ge3\) in the \(A\)-incidence word produces the
zero run of triple windows with the same endpoints shortened by one at each
end, hence of length \(\ell-2\). Conversely, every zero run of \(\gamma\)
arises uniquely this way. Thus

\[
Z_0(\gamma)=R_x^{(3)}.
\]

Finally, \(\gamma_s=1\) if and only if \(x\in H=C_s\). Hence

\[
e_x^{\rm cen}
=R_x^{(3)}-\mathbf1_{x\notin H}
=R_x^{(3)}-1+\mathbf1_{x\in H}.
\]

This proves that (1.2)/(4.4) has no off-by-one or seam-boundary error.
The external identity

\[
e_x^{\rm ext}=42-e_x^{\rm cen}
=43-R_x^{(3)}-\mathbf1_{x\in H}
\]

and bounds (1.4) follow immediately.

The global check also closes exactly:

\[
\sum_xe_x^{\rm cen}
=(m+8-\rho)-11+\rho=m-3,
\]

the number of central matching edges. Therefore

\[
\sum_xe_x^{\rm ext}=462-(m-3)=465-m.
\]

### 3.1 Rank-four bridge

From

\[
Z_x=E_{1,x}+E_{2,x}+R_x^{(3)}
\]

and the source identity

\[
Z_x+\lambda_x+r_x=65+h_x+2i_x,
\]

one obtains

\[
e_x^{\rm ext}
=\lambda_x+r_x+E_{1,x}+E_{2,x}-22-2h_x-2i_x.
\]

Thus (4.8) and its nonnegativity consequence (4.9) are algebraically exact.

## 4. Audit of the internal-seam root normal form

For an internal seam, \(P=C_{s-1}\) is the final vertex of the left-oriented
\(02\) state block and \(Q=C_{s+1}\) is the first vertex of the right-oriented
\(13\) block. Those are distinct nonempty state components. By the source's
orientation convention, both are roots. Their unused matching colors are

\[
U=T_{s-1}=P\cup H,\qquad V=T_s=Q\cup H.
\]

Therefore \(c\ge2\), as claimed.

Because \(P,Q\) have size five and \(U,V\) have size six, there are unique

\[
p\in H\setminus P,\qquad q\in H\setminus Q.
\]

The direct window identity \(H\subseteq P\cup Q\) implies
\(p\in Q\), \(q\in P\), and \(p\ne q\). Since
\(|U\cup V|=7+\eta\) and \(U\cup V=P\cup Q\),

\[
|P\cap Q|=10-(7+\eta)=3-\eta.
\]

Writing \(U=P\cup\{p\}\), \(V=Q\cup\{q\}\) gives

\[
U\cap V=(P\cap Q)\cup\{p,q\},\qquad |U\cap V|=5-\eta.
\]

Moreover

\[
H\cap P\cap Q=H\setminus\{p,q\},
\]

so

\[
|(P\cap Q)\setminus H|
=(3-\eta)-(\rho-2)=5-\rho-\eta.
\]

The source localizes the internal seam length-three runs to
\((U\cap V)\setminus H\). Since \(p,q\in H\), this is exactly
\((P\cap Q)\setminus H\). Equations (5.5)--(5.8) pass.

Both final matching edges complete \(\{p,q\}\): the \(P\)-edge adds \(p\)
while \(q\in P\), and the \(Q\)-edge adds \(q\) while \(p\in Q\). Both also
complete \(H\). Hence

\[
d_{\{p,q\}}\ge2,\qquad d_H\ge2.
\]

Subtracting the two unused central labels \(p,q\) from (4.4) gives

\[
f_x^{\rm cen}
=R_x^{(3)}-1+\mathbf1_{x\in H\setminus\{p,q\}},
\]

whose sum is \((m-3)-2=m-5\). Thus (5.9)--(5.10) also pass.

## 5. Audit of the global consistency checks

For a forest transition between two five-sets:

* exactly one rank-four star is internal to the transition (its four-set
  intersection);
* exactly four rank-four stars are entered;
* exactly six rank-four stars are bypassed.

For an unused matching edge from a five-set to a six-set, exactly ten
rank-four sets are completed. Hence, with \(|E(F)|=462-c\),

\[
\sum_{|X|=4}(h_X+a_X)
=(1+4)(462-c)=5(462-c),
\]

and

\[
\sum_{|X|=4}(a_X+z_X+d_X)
=(4+6)(462-c)+10c
=4620
=14\binom{11}{4}.
\]

The sums in Section 6 are therefore correct and do not conceal a missing
boundary term.

## 6. Exact repairs required in the source note

### Repair 1: opening description of the alternating path cover

Current wording:

> the complete rank-five and rank-six layers are paired by inclusion, and
> after deleting at most six matching edges they form a spanning alternating
> path cover of the middle-level graph.

This is misleading. The \(c\) final matching edges are unused only by the
projected Johnson forest; they are included as the terminal edges of the
alternating paths. Replace the sentence by:

> the complete rank-five and rank-six layers are paired by inclusion, and
> together with the \(462-c\) nonmatching inclusion edges induced by the
> Johnson forest they form a spanning alternating path cover of the
> middle-level graph by \(c\le6\) paths. The \(c\) final matching edges are
> unused by the projected Johnson forest but are the terminal edges of those
> alternating paths.

No later proof uses the inaccurate "after deleting" wording.

### Repair 2: define \(i_x\) in Section 4.2

Immediately before (4.8), replace

> where \(h_x=\mathbf1_{x\in H}\).

by

> where \(h_x=\mathbf1_{x\in H}\) and
> \(i_x=\mathbf1_{x\in I}\), with \(I=B_s\cap B_{s+1}\), as in the source
> note's \(n_5=133\) coordinate budget.

## 7. Final status

After those two local repairs, the note is mathematically sound as written.
It proves new necessary identities but no contradiction, and it does not
alter the finite bound \(\nu(11)\in[465,477]\).
