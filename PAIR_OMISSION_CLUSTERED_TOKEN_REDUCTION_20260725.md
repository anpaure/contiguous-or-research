# Pair-omission rows reduce the positive gate to a clustered token matching

Date: 2026-07-25

The full-row edge-colouring proposed in
`PAIR_OMISSION_TIGHT_ROW_MULTICOVER_20260725.md` is sufficient, but stronger
than necessary.  The first-avoided-pair extraction in that note points to a
sharper integral object: a matching of *start tokens* which is clustered
into a small number of consecutive runs of physical rows.

This note gives the exact token formulation and an exact audit of the first
upper shadow.  It does not prove the remaining multidepth token lemma.

## 1. The central token multigraph

For each omitted pair \(P\), each row
\(\pi=(x_0,\ldots,x_{2m-2})\) of the chosen local factor \(F_P\), and each
cyclic start \(i\), define

\[
 S_i=I_\pi(i,m-1),\qquad
 Y_i=I_\pi(i-1,m).
\tag{1.1}
\]

The start token is the bipartite edge

\[
 e(P,\pi,i)=(S_i,Y_i)
\tag{1.2}
\]

between

\[
 V_-={ [n]\choose m-1},\qquad V_0={ [n]\choose m}.
\]

Parallel edges are retained.  Let \(\mathcal B\) be this bipartite
multigraph.

### Proposition 1.1

The two degrees of \(\mathcal B\) are

\[
 d_-=\binom{m+2}{2},\qquad d_0=\binom{m+1}{2}.
\tag{1.3}
\]

Consequently \(\mathcal B\) has a matching saturating \(V_-\).

### Proof

A lower target \(S\) supplies one token for each omitted pair
\(P\subseteq S^c\), giving \(d_-\).  A middle target \(Y\) supplies one
token for each \(P\subseteq Y^c\), giving \(d_0\).  For
\(\mathcal A\subseteq V_-\), incidence counting gives

\[
 d_-|\mathcal A|\le d_0|N(\mathcal A)|.
\]

Since \(d_-/d_0=(m+2)/m>1\), Hall's condition follows.  \(\square\)

Thus exact lower ownership and distinct middle ownership are an ordinary
integral bipartite-matching problem once rows are split into tokens.  The
physical issue is not existence of that matching; it is clustering its
chosen tokens along their source rows.

## 2. Every token carries a full two-parent flag

For \(1\le q\le H\), define

\[
 L_q(e)=I_\pi(i+q-1,m-q),
 \qquad
 U_q(e)=I_\pi(i-1,m+q).
\tag{2.1}
\]

If consecutive tokens of one row are selected, their middle owners are
consecutive length-\(m\) windows, and (2.1) is exactly their consecutive
intersection/union flag.  In particular the token already contains both
parents of every Pascal diamond; no one-parent contraction is being used.

Let \(M\) be a lower-saturating matching of \(\mathcal B\).  In every
cyclic source row, break the selected token positions into maximal
consecutive runs, and let \(J(M)\) be the total number of runs.  By adding
the standard \(H\)-entry context at each cut, all flags (2.1), including
those at run endpoints, are literal.  The word cost is

\[
 |V_-|+O(HJ(M)).
\tag{2.2}
\]

There is no \(O(H^2J)\) boundary loss: the context positions are emitted as
initialization, rather than deleting the endpoint witnesses.

The first-avoided-pair construction of Theorem 5.1 in the source note gives
one such matching \(M_0\) with

\[
 J(M_0)=O\left(\frac{W\log^2m}{m}\right)
 =o(W/H)
\tag{2.3}
\]

for every Gaussian \(H=O(\sqrt{m\log m})\).  Hence lower ownership, middle
ownership, the complete two-parent chronology, and the reset ledger are
already simultaneously solved.

## 3. Exact first-upper defect of the extracted matching

Take the matching \(M_0\) from first-avoided-pair extraction.  In phase
\(j\), a selected token has

\[
 \kappa(S_i)=j,
\]

and its first upper flag is

\[
 Z_i=U_1(e)=I_\pi(i-1,m+1).
\tag{3.1}
\]

Since

\[
 S_i\subset Z_i\subseteq Q_{P_j},
\]

the set \(Z_i\) avoids \(P_j\) and meets every earlier pair met by
\(S_i\).  Therefore

\[
 \boxed{\kappa(Z_i)=\kappa(S_i)=j.}
\tag{3.2}
\]

Thus upper collisions between different phases are impossible.  Write
\(\mu_j(Z)\) for the phase-\(j\) multiplicity of \(Z\), and put

\[
 C_j=\sum_Z(\mu_j(Z)-1)_+.
\tag{3.3}
\]

### Proposition 3.1 (exact upper ledger)

The number of distinct rank-\((m+1)\) targets represented by the first
upper flags of \(M_0\) is

\[
 |V_-|-\sum_j C_j.
\tag{3.4}
\]

Consequently its rank-\((m+1)\) hole count is exactly

\[
 \boxed{
 M_1^+=W-|V_-|+\sum_jC_j
 =\frac{2W}{m+2}+\sum_jC_j.}
\tag{3.5}
\]

### Proof

There are \(|V_-|\) selected tokens.  Within phase \(j\), replacing every
positive multiplicity by one loses exactly \(C_j\) distinct targets.
Equation (3.2) makes the phase supports disjoint.  Subtract from the total
rank size \(W\).  \(\square\)

This pinpoints the first unresolved load.  In phase \(j=1\), every start of
the local factor \(F_{P_1}\) is selected.  Hence \(C_1\) is exactly the
collision excess of its length-\((m+1)\) cyclic intervals.  Category
thinning gives no saving in that phase.  Therefore Theorem 5.1 alone does
not imply \(M_1^+=o(W)\); one must either choose a locally near-rainbow
factor, or replace the first-avoided assignment by a genuinely balanced
token matching.

The unavoidable part of \(C_1\) is only lower order.  Put

\[
 A=\binom{2m-1}{m-1},\qquad
 B=\binom{2m-1}{m+1}=\binom{2m-1}{m-2}.
\]

There are \(A\) length-\((m+1)\) occurrences in \(F_{P_1}\), but only
\(B\) possible targets, so

\[
 C_1\ge A-B=\frac{2A}{m+1}=O(W/m).
\tag{3.6}
\]

Equality holds exactly when every possible target occurs at least once.
Thus the arithmetic baseline is harmless; the missing assertion is that
the *excess above* (3.6) is \(o(W)\).

## 4. The noncircular positive gate

For a token matching \(M\), let \(\mu_q^\pm\) be the load vectors of the
flags \(L_q,U_q\).  Let \(\mathcal E_H(M)\) be any of the already audited
weighted defect functionals which charges holes or balanced overload at
every signed depth and whose value \(o(W)\) suffices for literal repair.

The pair-omission route is reduced to the following statement.

> **Clustered balanced token-matching lemma.**  For Gaussian
> \(H=\Theta(\sqrt{m\log m})\), choose the local row factors and a matching
> \(M\) of \(\mathcal B\) saturating all but \(o(W/H)\) lower vertices such
> that
> \[
>   J(M)=o(W/H),\qquad \mathcal E_H(M)=o(W).
> \tag{4.1}
> \]

This formulation is genuinely two-parent: all flags are attached to start
tokens in complete Pascal ladders.  It is also strictly weaker than a
\((d_-+o(d_-/H))\)-edge-colouring of whole rows, because tokens from one row
may be used only on a controlled number of long runs rather than forcing
the entire row into one colour.

There are two exact endpoints around the open lemma:

1. ignoring \(J(M)\), the central matching is integral by Proposition 1.1,
   and abstract nested balanced flags are integral by the lower-bounded-flow
   theorem;
2. ignoring \(\mathcal E_H(M)\), Theorem 5.1 supplies the clustered matching
   (2.3).

The missing operation is therefore a sequence of alternating-cycle switches
in the bipartite token graph which moves the clustered matching toward the
balanced flag flow while increasing the number of source-row runs by only
\(o(W/H)\).  This is not the invalid one-chain contraction: every switched
token retains its complete flag (2.1).

Equivalently, if \(M_0\) is the first-avoided matching and \(M_1\) is a
balanced token matching, their symmetric difference is a union of even
alternating cycles in \(\mathcal B\).  It would suffice to choose a family
of those cycles which removes all but \(o(W)\) weighted flag defect while
creating only \(o(W/H)\) new row-run boundaries.  That is the sharp
positive switching theorem exposed by the pair-omission construction.

No proof of this final cycle-selection statement is supplied here.
