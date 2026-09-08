# Audit: frozen PBBS host fibres are zero-or-one, and the successor coatom is not a source letter

**Date:** 2026-08-07  
**Status:** PASS for the frozen-owner fibre-one correction, with an exact
indexing qualification. The former \(d+2\) candidate bound is not valid.
The source letter must be distinguished from both its fresh exterior and
the resulting depth-\(d\) coatom.

## 1. Index convention

Let \(A=(A_p)\) be the source word and use the forward derivative convention

\[
 T_i=(D^dA)_i=\bigcup_{p=i}^{i+d}A_p.
\tag{1.1}
\]

For suffixes ending at physical source position \(e\), write

\[
 Z_{e,j}=A_{e-j+1}\cup\cdots\cup A_e.
\tag{1.2}
\]

The owner ending at \(e\) is therefore

\[
 \widehat T_e:=Z_{e,d+1}=T_{e-d}.
\tag{1.3}
\]

This shift matters: a theorem which writes \(T_e=Z_{e,d+1}\) is using
endpoint-indexed owners, not the start-indexed owners in (1.1).

The maximal envelope at source position \(p\) is

\[
 P_p=\bigcap_{h=0}^{d}T_{p-h}.
\tag{1.4}
\]

Hence every safe set \(C_p\subseteq P_p\) is contained in every owner
window through \(p\), in particular

\[
 C_p\subseteq T_{p-d}=\widehat T_p.
\tag{1.5}
\]

Since \(\widehat T_p\) has rank \(m\),

\[
 |C_p|\le m.
\tag{1.6}
\]

Thus the claimed containment of \(C_p\) in a rank-\(m\) owner is correct,
provided the endpoint/start index shift (1.3) is made explicit.

## 2. Exact successor recurrence

Let an upper flag occur at endpoint \(e\), and put

\[
 M=Z_{e,d-1},\qquad U=Z_{e,d}=M\cup\{u\}.
\tag{2.1}
\]

Its immediate successor source position is \(q=e+1\). Directly from
(1.2),

\[
 Y:=Z_{q,d}=M\cup A_q,
\qquad
 \widehat T_q:=Z_{q,d+1}=U\cup A_q.
\tag{2.2}
\]

If \(Y\) is a rank-\((m-1)\) coatom of the rank-\(m\) owner
\(\widehat T_q\), with entering coordinate \(u\), define

\[
 B=A_q\setminus U.
\tag{2.3}
\]

Then

\[
 |B|=d+1,\qquad
 B=\widehat T_q\setminus U,\qquad
 Y=M\cup B=\widehat T_q\setminus\{u\}.
\tag{2.4}
\]

The actual source letter need not equal \(B\). Its most general harmless
form relative to this central edge is

\[
 A_q=B\cup K,\qquad K\subseteq M.
\tag{2.5}
\]

The filler \(K\) may be needed by a mandatory core, a positive-hit cut, or
a phase type. It changes neither \(Y\) nor \(\widehat T_q\).

Consequently:

* \(Y\) is a width-\(d\) suffix union, not a source letter;
* \(B\) is the fresh exterior of the source letter, not necessarily the
  entire source letter;
* an exact typed edge test must quantify over a legal filler
  \(K\subseteq M\cap C_q\).

## 3. Degree collapse

### Theorem 3.1 (frozen-owner fibre one)

Fix the flag \((M,u)\), the successor position \(q\), and its endpoint
owner \(\widehat T_q\). There is at most one central host edge. If it
exists, it is

\[
 B=\widehat T_q\setminus U,\qquad
 Y=\widehat T_q\setminus\{u\}.
\tag{3.1}
\]

#### Proof

The owner equation is

\[
 \widehat T_q=U\mathbin{\dot\cup}B.
\]

Thus \(B\) is forced by set difference, and then so is \(Y=M\cup B\).
No envelope or phase test can create a second choice. \(\square\)

The safe envelope is therefore a legality test on this forced edge, not a
binomial menu at a fixed owner occurrence.

Before the owner is fixed, an envelope-only relaxation has at most

\[
 \binom{|C_q\setminus U|}{d+1}
 \le \binom m{d+1}
\tag{3.2}
\]

possible exteriors, by (1.6). But this is still not the degree of a frozen
occurrence: changing \(B\) changes \(\widehat T_q=U\cup B\), and therefore
changes the owner history from which \(C_q\) was computed.

The former bound

\[
 |C_q\setminus U|\le d+2
\tag{3.3}
\]

was based on \(M\subseteq C_q\). PBBS suffix indexing does not imply that
containment: \(M\) is the union of the preceding \(d-1\) source letters,
whereas \(C_q\) constrains the new source letter at \(q\). Hence (3.3) and
the resulting \(d+2\) candidate count must not be cited.

## 4. Exact fixed-occurrence compatibility

For a genuinely frozen occurrence, the right-hand state must retain more
than \((Y,\widehat T_q,C_q)\). Define

\[
 M_q=Z_{q-1,d-1},\qquad U_q=Z_{q-1,d}.
\tag{4.1}
\]

A flag \(f=(M_f,u_f)\), \(U_f=M_f\cup\{u_f\}\), is compatible with the
occurrence only if

\[
 (M_f,U_f)=(M_q,U_q).
\tag{4.2}
\]

After (4.2), its central exterior and edge are forced by (3.1). Literal
legality additionally requires either:

* if the source letter is fixed, its actual exterior is
  \(A_q\setminus U_f=B\); or
* if the slot may be reselected inside its envelope, there is
  \(K\subseteq M_f\cap C_q\) such that
  \(A_q=B\cup K\) passes the mandatory-core, positive-hit, phase, residence,
  and other protected-history tests.

Thus the proof-safe frozen right vertex is an occurrence record containing

\[
 (q,M_q,U_q,A_q,Y_q,\widehat T_q,C_q,\text{type}),
\tag{4.3}
\]

not merely a central edge \(Y_q\subset\widehat T_q\).

If the history is not frozen, all of the data in (4.3) must travel in one
prospective hyperedge. One may then use the complete ideal host family, but
one may not first freeze \(C_q\) and subsequently vary
\(\widehat T_q=U_f\cup B\) independently.

## 5. Audit verdict on the patched theorems

1. The central statement of
   *MATH_THEOREM_PBBS_FROZEN_OCCURRENCE_FIBRE_ONE_AND_PROSPECTIVE_HOST_QUANTIFIER_20260807.md*
   is correct: fixed owner plus fixed flag gives zero or one host edge.
2. The occurrence-envelope bound \(|C_q|\le m\) is correct, with the
   endpoint indexing (1.3).
3. The old \(d+2\) bound is incorrect and has correctly been superseded.
4. The phrase “candidate successor letter is \(Y\)” is incorrect.
   Equations (2.2)--(2.5) are the sharp replacement.
5. Any purported exact frozen-history matching must include (4.2) and the
   actual-letter/filler test. Conditions such as
   \(M_f\subseteq Y_q\subseteq C_q\) are not correctly typed:
   \(C_q\) bounds \(A_q\), not the suffix union \(Y_q\).

The surviving all-dimensional gate is therefore an occurrence matching
whose right vertices are full records (4.3), or an equivalent joint
history-factor hypermatching. A pointwise binomial degree theorem at a
frozen reset occurrence is unavailable.
