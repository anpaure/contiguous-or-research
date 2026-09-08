# K16 H2 non-provider-first closure: exact anchor atlas and the bit-15 exclusive-supply obstruction

Date: 2026-07-30  
Lane: K  
Status: mixed non-provider/provider two-edit face exactly closed

## 1. Result

Let $W$ be the frozen length-$12873$ word

    scratch/k16_ejection_lns_h2_p110_20260730.word

with SHA-256

    5234b77101ac1f22ec1802b4e1f5eccb6f0fc6f540efff9bbd0dc92da8c09fe7

and exact holes

\[
A=0x4879\subset B=0x6879=A\vee0x2000.
\tag{1.1}
\]

The earlier exact atlas closed the branch in which both final endpoints are
source non-providers. The authenticated provider-first rerun closed every
provider endpoint whose one-edit intermediate has at most seven holes.

This note closes the remaining non-provider-first chronology:

- the first lasting edit $p\leftarrow x$ supplies neither $A$ nor $B$ when
  applied alone to $W$;
- the second lasting edit $q\leftarrow y$ is a source-hole provider.

> **Mixed-face closure theorem.** No universal word is obtained from $W$ by
> a source-nonprovider edit followed by one source-provider edit.

Therefore every still-hypothetical two-edit completion of $W$ must have two
source-provider endpoints. Applying either endpoint first must produce at
least eight holes. This note does not close that provider/provider face and
does not claim a complete radius-two no-go.

## 2. Occurrence cores and one-cell intervals

For a word $V$, let $\mathcal W_V(T)$ be the family of interval witnesses of
$T$. Their occurrence core is

\[
J_V(T)=\bigcap_{I\in\mathcal W_V(T)}I.
\tag{2.1}
\]

For intervals this is

\[
J_V(T)=
\left[
\max_{[l,r]\in\mathcal W_V(T)}l,\ 
\min_{[l,r]\in\mathcal W_V(T)}r
\right]
\tag{2.2}
\]

when the endpoints are ordered, and empty otherwise. Thus every $T$-witness
uses position $p$ exactly when $p\in J_V(T)$.

Delete position $p$ and extend through the maximal consecutive fixed context
whose letters are submasks of $T$. Write

\[
c_p^V(T)=\text{its OR},\qquad
r_p^V(T)=T\setminus c_p^V(T).
\tag{2.3}
\]

Replacing $p$ by $x$ creates a $p$-containing $T$-witness exactly when

\[
r_p^V(T)\subseteq x\subseteq T.
\tag{2.4}
\]

Define

\[
\mathcal S_p(V)=
\operatorname{holes}(V)\cup
\{T:\ T\text{ is covered in }V,\ p\in J_V(T)\},
\tag{2.5}
\]

\[
L_p(V)=\bigvee_{T\in\mathcal S_p(V)}r_p^V(T),
\qquad
U_p(V)=\bigcap_{T\in\mathcal S_p(V)}T.
\tag{2.6}
\]

The exact one-cell theorem gives

\[
V^{p\leftarrow x}\text{ universal}
\iff
0\ne x,\qquad L_p(V)\subseteq x\subseteq U_p(V).
\tag{2.7}
\]

The covered $p$-exclusive targets in (2.5) are indispensable. Using only the
current holes gives a necessary relaxation, not a completion theorem.

## 3. Exact mixed orientation

Assume $p\leftarrow x$ is first chronologically and is a source
non-provider, while $q\leftarrow y$ is a source provider. The positions are
distinct; otherwise the first edit has no lasting effect and the final word
would be a forbidden one-edit completion.

After the first edit, $A$ is still missing. Every final $A$-witness is
created by the edit at $q$ and contains $q$. Hence

\[
0\ne y\subseteq A.
\tag{3.1}
\]

Reverse the two commuting edits and put

\[
V=W^{q\leftarrow y}.
\tag{3.2}
\]

The authenticated provider-first theorem forces

\[
|\operatorname{holes}(V)|\ge8.
\tag{3.3}
\]

Let $\Pi_p^W(H)=[r_p^W(H),H]\setminus\{0\}$ be the exact source provider
domain for hole $H$.

### Theorem 3.1 (mixed-row iff)

The ordered pair $(p,x),(q,y)$ is a mixed completion if and only if:

1. $q\ne p$ and $y$ is a source provider satisfying (3.1);
2. the provider state (3.2) satisfies (3.3); and
3.

\[
x\in
\bigl([L_p(V),U_p(V)]\setminus\{0,w_p\}\bigr)
\setminus
\bigl(\Pi_p^W(A)\cup\Pi_p^W(B)\bigr).
\tag{3.4}
\]

#### Proof

Necessity of (3.1) and (3.3) was proved above. Algebraically the final word is
$V^{p\leftarrow x}$, so (2.7) is necessary. The two removed source provider
domains say exactly that $p\leftarrow x$ leaves both holes missing when
performed first.

Conversely, any $x$ satisfying (3.4) is a literal change, is a source
non-provider, and completes $V$ by (2.7). Commuting the edits gives the
required chronology. ∎

Thus every row is the nonzero part of one Boolean interval, minus two Boolean
subintervals and the literal non-change point $w_p$. There is no residual
$65535$-value search.

## 4. Exact useful-first-edit anchor atlas

For a raw first edit $p\leftarrow x$, its collateral debts are exactly

\[
D_{p,x}=
\{T\notin\{A,B\}:
 p\in J_W(T),\
 x\notin[r_p^W(T),T]\}.
\tag{4.1}
\]

If the final provider value is $y$, then every current hole contains $y$:

\[
0\ne y\subseteq
A\cap\bigcap_{T\in D_{p,x}}T.
\tag{4.2}
\]

This is stronger than an unspecified shared coordinate: the debts share every
coordinate of the literal final donor.

For fixed $p$ and $0\ne y\subseteq A$, define

\[
\Gamma_{p,y}=
\{T\notin\{A,B\}:
 p\in J_W(T),\
 y\nsubseteq T\},
\tag{4.3}
\]

\[
L^{\rm anc}_{p,y}
=\bigvee_{T\in\Gamma_{p,y}}r_p^W(T),
\qquad
U^{\rm anc}_{p,y}
=\bigcap_{T\in\Gamma_{p,y}}T.
\tag{4.4}
\]

Here $\bigvee\varnothing=0$ and
$\bigcap\varnothing=0xffff$. In what follows an edit value is always required
to satisfy $x\ne0,w_p$.

Among source non-provider values,

\[
y\subseteq
\bigcap\operatorname{holes}(W^{p\leftarrow x})
\iff
L^{\rm anc}_{p,y}\subseteq x\subseteq U^{\rm anc}_{p,y}.
\tag{4.5}
\]

Every $p$-exclusive target omitting some bit of $y$ must be preserved, and
(2.4) gives exactly the simultaneous interval in (4.4).

Equations (4.3)--(4.5) are the exact anchor-feasibility atlas for useful
non-provider first edits: $12873$ positions times the $127$ nonzero submasks
of $A$, each represented by one Boolean interval, the literal-edit
conditions, and two source-nonprovider clauses. The reverse atlas of
Theorem 3.1 adds the exact final occurrence constraints needed for
completion.

## 5. Compact closure/dominance model

For a retained reverse row $(q,y,p)$, introduce the $16$ bits of $x$. The
exact candidate CNF consists of:

- unit rows $x_e=1$ for $e\in L_p(V)$;
- unit rows $x_e=0$ for $e\notin U_p(V)$;
- one nonzero row;
- one row $x\ne w_p$; and
- for each $H\in\{A,B\}$, the exact non-provider clause

\[
\left(\bigvee_{e\notin H}x_e\right)
\vee
\left(\bigvee_{e\in r_p^W(H)}\neg x_e\right).
\tag{5.1}
\]

First precheck $U_p(V)\ne0$ and $L_p(V)\subseteq U_p(V)$; failure emits one
empty clause. After that precheck, the displayed model uses $16$ variables
and at most $20$ clauses and is satisfiable exactly when the row contains a
mixed completion.

Raw upper closure $x\mapsto U_p(V)$ is not valid: adding bits can turn a
non-provider into a provider. An exact dominance split fixes one witnessing
failure literal from each clause (5.1) and, when needed, one witnessing
literal for $x\ne w_p$, then takes the largest mask in that face.
Equivalently, and without any dominance shortcut, enumerate

\[
2^{|U_p(V)\setminus L_p(V)|}
\tag{5.2}
\]

values. In the frozen census the hole intersection has at most six bits, so
each relaxed row has at most $64$ values. No SAT solver is needed.

## 6. Exact census

Phase one enumerated every source-provider edit:

\[
\begin{array}{c|r}
\text{class} & \text{count}\\ \hline
\text{distinct provider moves} & 44421\\
\text{intermediate holes at most seven} & 284\\
\text{high states with empty hole intersection} & 805\\
\text{high states with nonzero hole intersection} & 43332
\end{array}
\tag{6.1}
\]

The full after-histogram agrees exactly with the independent provider atlas.

The mixed orientation filter and exact hole interval give

\[
\begin{array}{c|r}
\text{class} & \text{count}\\ \hline
\text{nonzero-intersection states with }y\nsubseteq A & 21577\\
\text{oriented high states }(y\subseteq A) & 21755\\
\text{oriented states with no hole-stage position} & 21743\\
\text{hole-stage state/position rows} & 12\\
\text{relaxed first values in those rows} & 27
\end{array}
\tag{6.2}
\]

For each of the $12$ rows, the audit rebuilt the full witness bank and added
every covered target whose occurrence core contains the proposed repair
position. All $12$ exact intervals became empty.

## 7. Uniform bit-15 obstruction

The $12$ rows have the common geometry

\[
y=A=0x4879,\qquad q-p=6438.
\tag{7.1}
\]

In every row,

\[
L_p(V)\mathbin\&\neg U_p(V)=0x8000.
\tag{7.2}
\]

One current hole has residual requirement containing bit $0x8000$, so every
repair value must have that bit. One covered target whose every witness uses
$p$ omits the same bit, so every repair value must omit it. The independently
replayed two-row cores are:

| forcing hole | forbidding $p$-exclusive target |
|---:|---:|
| 0x8838 | 0x0838 |
| 0xa409 | 0x2729 |
| 0xe928 | 0x6928 |
| 0xa888 | 0x688c |
| 0xa08a | 0x208a |
| 0xe802 | 0x684a |
| 0xa8c8 | 0x28c8 |
| 0xa8c4 | 0x28c4 |
| 0xa644 | 0x2674 |
| 0xa237 | 0x2237 |
| 0xa0b8 | 0x28ba |
| 0x897c | 0x097c |

Thus the $12\to0$ step is not an opaque search result. Every row has an
explicit two-target empty-intersection certificate on one coordinate.

## 8. Independent audit

For each of the $12$ rows the independent verifier:

1. reconstructs the reverse provider word;
2. recomputes every interval-OR multiplicity and exact hole list;
3. recomputes the count of witnesses through the repair position;
4. identifies covered targets whose through-count equals their global count;
5. reconstructs the hole-only and full Boolean intervals;
6. checks the two source-nonprovider clauses; and
7. extracts the literal bit-$15$ forcing/forbidding pair.

It passes all $12$ rows and finds zero mixed completions. Its tested-row
payload hash is

    26eabf57459f587f641acb5695244020f29f9e69bbee7f88e9cacd38576c2511.

The global $21755\to12$ enumeration is cross-checked against the frozen
provider atlas and independent phase-one count, rather than re-enumerated by
the Python verifier.

## 9. Resource-safe execution and authentication

No file was written to the full /dev/shm. All H100 work used

    /home/amodo/or15/work/laneK_h2_reverse_closure_20260730

on one CPU, with a $512$ MiB address-space cap and $120$-second timeouts.
Timeout, ENOSPC, signal, or nonzero exit was designated UNKNOWN.

\[
\begin{array}{c|c|c}
\text{stage} & \text{elapsed} & \text{maximum RSS}\\ \hline
\text{provider intersection} & 0.22\text{ s} & 21452\text{ KiB}\\
\text{exact reverse finish} & 7.12\text{ s} & 22016\text{ KiB}\\
\text{independent replay} & 0.92\text{ s} & 103128\text{ KiB}
\end{array}
\tag{9.1}
\]

The package manifest is

    scratch/k16_h2_highdebt_reverse_closure_20260730/manifest.audit.json

with SHA-256

    6cc6f8292dd474332b3ec362561b0f65ac1df3e7d2df9e44e4b5936d99379caa

and payload hash

    83f358e7d4301a8b0e19a18a7bb96c8aa69ffafe01ffa3d889d134147eb2d950.

Primary hashes:

    phase-one source
      87bedd646d96c8ee8930ba84d6bd3377171cebef8bc5dd90536a9fefe2898753
    phase-one audit
      b45b208b876215d02db8b83193e8b1ff7537592c9a4b44bce0501aa1dbe05245
    phase-two source
      0e6ee9e73eddf47c9443a5a8e8f1ed9ba506aaf938736224ac14933a34dae887
    phase-two audit
      093d6fe8feaced995407641a97971dd9a7532c166699e0e7a49cf65a3e716c4d
    independent source
      6106abf82599b8b03f09947d4ab8308f4f466daf40979f5ba33e75536f9b6c4b
    independent audit
      b8cf297034eb50d0bb4717bcf0c57ce10358b2133990a1b744f708f8d09628c9
      payload 99d951c45571ca765326be7e524aba8a210163ec3182cd1e309c4424bbb6658d

The manifest freezes the seed, included provider engine, Linux binaries,
resource transcripts, exits, audits, authenticated low-hole rerun, and the
earlier both-nonprovider audit.

## 10. Sharp boundary

All two-edit chronologies with a source non-provider first endpoint are now
closed:

- non-provider/non-provider by the earlier $335$-corridor theorem;
- non-provider/provider by the exact mixed-face theorem above.

Hence a remaining two-edit completion, if one exists, uses two source-provider
endpoints. The authenticated low-hole theorem applies in either ordering, so
both provider-first intermediate words must have at least eight holes.

This provider/provider high-debt face is the sole remaining radius-two
question at the frozen H2 word.
