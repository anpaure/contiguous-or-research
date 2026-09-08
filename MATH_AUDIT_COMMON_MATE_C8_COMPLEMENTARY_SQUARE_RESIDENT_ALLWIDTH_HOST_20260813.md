# Independent audit of the complementary-square resident all-width host

**Date:** 2026-08-13  
**Verdict:** **PASS** for the theorem's stated local and spanning-host scope.  
**Audited theorem:**
`MATH_THEOREM_COMMON_MATE_C8_COMPLEMENTARY_SQUARE_RESIDENT_ALLWIDTH_HOST_20260813.md`  
**Audited theorem SHA-256:**
`8a6899e0aa19a2a64782f9069d159af51a6b5075e754a132665748d3784b2e02`

No source correction was needed.

## 1. Independent literal reconstruction

I independently reconstructed the displayed construction from equations
(1.2)--(1.16), including the exact one-neutral-label return departure

\[
 (Z-\{d_j\},q_{j+3},d_j,q_{j+2}),
\]

the insertion of (q_j) at position (w=n-q), and the two wrap corrections
(c_1,c_2) on path three.  The independent replay is

`scratch/audit_common_mate_c8_complementary_square_literal_text_20260813.py`

with SHA-256

`cfa7edc76ca16f28123ddf7c97bb17d645fbc92254377363c91455c7decf0ca4`.

It does not import the repository replay or copy its builder.

For every admissible pair ((m,q)) with (18\le m\le40), namely all 213
pairs satisfying

\[
 q\ge5,\qquad m\ge\max\{q+8,2q+2\},
\]

the independent replay verifies:

* the endpoint identities (F_{j,n}=B_j), the four displayed return-tail
  states, (G_{j,n-1}=R_j), and (G_{j,n}=U_j);
* every owner has rank (m), and every consecutive pair is one Johnson
  exchange;
* all owners, rank-((m-1)) lower facets, and rank-((m+1)) adjacent unions
  are globally distinct;
* every nonconstant positive and zero run on every old cycle has length at
  least (q);
* after concatenating the output paths in switched order, every positive and
  zero run on the merged cycle also has length at least (q);
* the exact exposure values are (alpha=eta=3), hence certainly at most
  eight; and
* the prefix-union identity holds for every (0\le s\le n), and the terminal
  prefix is the full ground set.

The repository replay

`scratch/audit_common_mate_c8_complementary_square_resident_allwidth_20260813.py`

has SHA-256

`670fa5a537eb4fcfac5fac296945209f577162d175c76837b933d263f028308c`.

It independently passes its 105 default cases through (m=120), again with
(alpha=eta=3).

## 2. Proof audit

### 2.1 Parameters and endpoints

The ground-size identity is exact:

\[
 |C|+|Z|+|Q|+1=(m-3)+(m-3)+4+1=2m-1.
\]

Both forward lists have length (n=m-1), enumerate respectively
(U_j-\{p_j\}) and its complement, and therefore end at

\[
 B_j=\{p_j\}\cup([2m-1]-U_j).
\]

The return lists also have length (n).  Immediately before the last three
exchanges the only absent core label is (t_j), yielding the four states in
(1.15).  The last edge is indeed (R_j-U_j), whose intersection is the
specified lower socket (L_j).  Hence the bank consists of four literal
closed alternating incidence cycles, not paths with an implicit closure.

### 2.2 Residence

Lemma 2.1's run formula follows by counting the two arcs between departure
position (u) and return position (v).  For the four old cycles, the
displayed return order gives the claimed displacement bounds.  In particular,
(q_j) is restored at (n-q), while the late (t_j) and the path-three
corrections obey the endpoint inequalities allowed by
(m\ge\max\{q+8,2q+2\}).

The switched cycle needs a separate splice check; the theorem supplies it.
At the ordinary three splices, consecutive cyclic core orders shift by only
one place.  At the wrap splice, putting (c_1,c_2) at (w+1,w+2) makes the
two critical runs exactly (q).  The active label dropped at splice
(j\to j+1) is (q_j), whose restoration at (n-q) makes its terminal run
exactly (q).  The literal switched-run census agrees with these formulas.

### 2.3 Simplicity and exposure

The pair

\[
 (|V\cap C|,|V\cap Z|)
\]

separates all different nonterminal stages except the stated boundary
comparisons.  The cyclic deleted-core interval, omitted label (p_j), return
hole (t_j), neutral label (d_j), and active triple then separate the
remaining cases.  Applying the same signatures after deleting or adjoining
the unique exchange label proves lower- and upper-colour simplicity.

The direct conclusion used later is only the conservative bound
(alpha,eta\le8).  The literal census obtains the stronger value three.
Thus

\[
 e_m=4(4m-4)=16m-16,
 \qquad e_m=2^{o(m)},\quad\alpha,eta=o(m).
\]

### 2.4 All-width identity and socket action

For fixed incoming (R_i), equation (4.2) leaves only (q_{i+3}) absent.
That label occurs in both missing pairs for output paths (i) and (i+1),
and parity puts it at the same final position in both forward-arrival lists.
Every earlier arrival is either the same (Z)-label at the same time or an
active label already present in (R_i).  Therefore the accumulated unions
are equal occurrence-by-occurrence through the complete forward path.

At the forward endpoint the accumulated union is the full ground set, so an
interval extending into the return remains full in either phase.  An interval
not crossing a switched incidence is unchanged literally.  This is enough
for the all-width signed current to vanish; no equality of return prefixes is
needed.  The reconnection sends output (i) to (i+1), so it merges the four
cycles and induces the asserted odd socket action.

### 2.5 Spanning host

The protected bank is a union of vertex-disjoint, properly phased incidence
cycles and satisfies the exact hypotheses

\[
 e_m=2^{o(m)},\qquad\alpha_m=o(m),\qquad\beta_m=o(m)
\]

of the cited subexponential low-exposure coinstantiation theorem.  The
application in Corollary 5.1 is therefore within the cited theorem's stated
quantifiers.  Saturation of protected lower vertices also prevents the four
new switch incidences from already belonging to the old factor.

## 3. Exact scope retained

The theorem correctly does **not** claim that the private sockets are already
the inherited recursive MNW terminals, that common-cap prefixes or the typed
suffix router are present, or that the global positive owner/flag factor has
been selected around the bank.  Those are separate occurrence-level rows.

Within its stated scope, the construction simultaneously proves all-width
transparency, old- and switched-phase two-sided residence, resource
simplicity, a spanning phased host, and the odd/crossed socket action.
