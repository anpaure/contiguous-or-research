# Thread A: exact H21-to-H20 Boolean signature compression

Date: 2026-07-28

Status: proved for the frozen carriers below.  The result gives an exact,
full-catalogue criterion for recognizing another neutral compression and its
splitter.  It does not prove an iteration to Hall zero, a length-6438 word,
or one global common-\(Q\) compiler matching.

## 1. The exact route

Let \(G(P)\) denote the depth-three compiler graph of a rank-eight Johnson
path \(P\).  The audited route is

\[
 H21\xrightarrow{\operatorname{RF}(1510,5017,6136)}
 H21^{\mathrm{comp}}
 \xrightarrow{\operatorname{RF}(885,1393,3668)}H20 .       \tag{1.1}
\]

The three certificates are

```text
scratch/k15_segment_braid_hall21_zero6.json
scratch/k15_segment_braid_hall21_compressed_dm702.json
scratch/k15_segment_braid_hall20_zero6.json
```

with SHA-256 values

```text
8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447
ea5259c4bb8a15444da135f7c6369e11fbc059f322c570fd3db2e6b8509af337
9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1
```

Their matching ranks and canonical DM shores are

\[
\begin{array}{c|ccc}
 &H21&H21^{\rm comp}&H20\\ \hline
\nu&16362&16362&16363\\
\text{deficiency}&21&21&20\\
|X_{\rm DM}|/|Y_{\rm DM}|&846/825&702/681&677/657\\
\text{zero targets}&6&6&6.
\end{array}                                                     \tag{1.2}
\]

Every state is the exact middle deck of all \(6435\) rank-eight masks, is a
Johnson path, is depth-three resident, and has complete upper support at
every depth \(q=1,\ldots,7\).  The lower-hole vectors are

\[
 (4,18,9,1,0,0,0),\quad
 (4,18,11,1,0,0,0),\quad
 (4,18,11,1,0,0,0).                                           \tag{1.3}
\]

Thus the first braid loses the two depth-three lower targets \(1801\) and
\(5000\).  This is a Hall/common-owner descent, not an all-lower-shadow
preservation theorem.

## 2. Full-profile collar capacity

For a physical compiler cell \(y\), let \(\Gamma(y)\) be its **full** shore
in the common producer/consumer catalogue.  For a carrier \(P\), let
\(\mathcal P(P)\) be the multiset of all \(19311\) full shores.  If two
carriers have profile multisets

\[
 \mathcal P_0=\mathcal C\mathbin{\dot\cup}\mathcal E_0,
 \qquad
 \mathcal P_1=\mathcal C\mathbin{\dot\cup}\mathcal E_1,       \tag{2.1}
\]

where \(\mathcal C=\mathcal P_0\wedge\mathcal P_1\) is their multiset
intersection, define

\[
 \kappa_{\mathcal C}(\mathcal E)
   :=\nu(\mathcal C\mathbin{\dot\cup}\mathcal E)-\nu(\mathcal C).
                                                                    \tag{2.2}
\]

### Lemma 2.1 (exact physical collar identity)

For any two carriers evaluated on the same full catalogue,

\[
 \nu(G(P_1))-\nu(G(P_0))
 =\kappa_{\mathcal C}(\mathcal E_1)
  -\kappa_{\mathcal C}(\mathcal E_0).                         \tag{2.3}
\]

#### Proof

By (2.1), \(G(P_i)\) is exactly the profile graph
\(\mathcal C\dot\cup\mathcal E_i\).  Subtract \(\nu(\mathcal C)\) from
both matching numbers.  No endpoint maximum or pair-face relaxation enters
the identity. \(\square\)

For the two transitions in (1.1), the exact values are

\[
\begin{array}{c|ccccc}
 &|\mathcal C|&\nu(\mathcal C)&|\mathcal E_0|&|\mathcal E_1|
 &\kappa(\mathcal E_0)\to\kappa(\mathcal E_1)\\ \hline
H21\to H21^{\rm comp}&19282&16338&29&29&24\to24\\
H21^{\rm comp}\to H20&19279&16345&32&32&17\to18.
\end{array}                                                     \tag{2.4}
\]

This proves neutrality of the first braid and the one-unit gain of the
second using the identical full-cell catalogue.

## 3. The normalized six-to-seven source identity

For a mask \(K\) and a set \(I\) of coordinate indices, write
\(K_I=K\cup I\).  Define the following two column banks on six distinct
axes \(a,b,c,d,e,f\):

\[
\begin{aligned}
\Lambda^-:=\{&
 \{K,K_a,K_{ab}\},
 \{K,K_a,K_c,K_{ac}\},
 \{K_d,K_{ad},K_{cd},K_{acd}\},\\
&\{K_{af},K_{abf}\},
 \{K_c,K_{ac},K_{bc},K_{abc}\},
 \{K_e,K_{ae},K_{ce},K_{ace}\}\},                            \tag{3.1}\\
\Lambda^+:=\{&
 \{K,K_a\},\{K_{ab}\},\{K_{abf}\},\{K_c,K_{ac}\},\\
&\{K_c,K_{ac},K_{cd},K_{acd}\},
 \{K_{bc},K_{abc}\},\{K_{ce},K_{ace}\}\}.                  \tag{3.2}
\end{aligned}
\]

The columns of \(\Lambda^-\) have rank six.  The columns of
\(\Lambda^+\) have rank seven: match them, in displayed order, to

\[
 K, K_{ab}, K_{abf}, K_c, K_{cd}, K_{bc}, K_{ce},       \tag{3.3}
\]

which are distinct.  This is the local associator refinement.

In the H21 carrier take

\[
 K=1920,qquad (a,b,c,d,e,f)=(3,0,12,6,2,13).                 \tag{3.4}
\]

The six lost restricted shores are

\[
\begin{gathered}
\{1920,1928,1929\},
\{1920,1928,6016,6024\},
\{1984,1992,6080,6088\},\\
\{10120,10121\},
\{6016,6017,6024,6025\},
\{1924,1932,6020,6028\},                                    \tag{3.5}
\end{gathered}
\]

and the seven gained restricted shores are

\[
\begin{gathered}
\{1920,1928\},\ \{1929\},\ \{10121\},\ \{6016,6024\},\\
\{6016,6024,6080,6088\},\ \{6017,6025\},\ \{6020,6028\}.
                                                                    \tag{3.6}
\end{gathered}
\]

The unchanged restricted bank on the old root-\(1920\) component has
\(162\) columns and rank \(162\).  The exact restricted matching audit
also verifies that the displayed boundary columns extend this bank
compatibly.  Therefore (3.5) and (3.6) give

\[
 168\longrightarrow169,                                      \tag{3.7}
\]

and saturate the entire old \(169/168\) component.

## 4. The normalized three-to-two compensation coin

Let

\[
 L=1801,qquad c=12,qquad d=6.                               \tag{4.1}
\]

On the replacement target set the changed restricted bank is

\[
 \Theta^-=
 \bigl\{\{L\},\{L_c\},\{L_{cd}\}\bigr\}
 \quad\longrightarrow\quad
 \Theta^+=
 \bigl\{\{L,L_c\},\{L_d,L_{cd}\}\bigr\}.                  \tag{4.2}
\]

Numerically,

\[
 \{\{1801\},\{5897\},\{5961\}\}
 \longrightarrow
 \{\{1801,5897\},\{1865,5961\}\}.                         \tag{4.3}
\]

The unchanged bank has \(22\) columns and rank \(22\), and the exact audit
verifies compatible extensions by both displayed boundary banks.  Hence (4.3)
changes its rank from \(25\) to \(24\), creating one new unit-deficient
component.  The complete canonical DM comparison is exact:

* the old root-\(1920\) component is \(169/168\);
* the new root-\(1801\) component is \(25/24\);
* the two target sets meet only in target \(1933\);
* the other twenty DM components and all of their restricted profile
  multisets are unchanged.

Thus the first RF does not shrink one incidence graph.  It saturates the
large component and transfers its deficiency token to a smaller component.

## 5. Exact comparison with the old root-449 compression

The earlier neutral FF had the same normalized banks:

\[
\begin{array}{c|cc|cc}
 &|A|&\operatorname{rank}(C_A)&|B|&\operatorname{rank}(C_B)\\ \hline
449\to458&160&153=160-7&24&21=24-3\\
1920\to1801&169&162=169-7&25&22=25-3.
\end{array}                                                     \tag{5.1}
\]

In both cases \(C_A+\Lambda^-\) has rank \(|A|-1\),
\(C_A+\Lambda^+\) has rank \(|A|\),
\(C_B+\Theta^-\) has rank \(|B|\), and
\(C_B+\Theta^+\) has rank \(|B|-1\).  Both neutral braids change exactly
29 full cell shores and have full collar capacity \(24\to24\).

This equality of normalized banks is the reusable identity.  Equality of
component sizes, target histograms, or marginal degrees is not required.

There is a stronger physical recurrence.  The coordinate permutation

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
x&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\ \hline
\phi(x)&7&3&4&0&6&13&8&9&10&5&12&2&14&11&1
\end{array}                                                     \tag{5.2}
\]

maps the complete old \(449\to458\) router collar to the complete new
\(1920\to1801\) router collar.  More precisely, it maps the unordered
multisets of the three deleted seam edges and three inserted seam edges,
all 29 deleted **full** shores, and all 29 inserted full shores exactly.
Thus the recurrence is not inferred from the restricted ledgers: it is a
literal coordinate conjugacy of the whole physical router signature.  The
Thread-A audit script verifies (5.2) directly from the four frozen carriers.

The neutral arrow also has a literal critical-shore common-\(Q\)
certificate.  In the compressed carrier, depth-zero cells `1510` and `5216`
both have native trace \(1928\).  Set \(Q_{1510}=1920\), deleting coordinate
3 from that one controller state; use cell `1510` for root \(1920\) and
retain cell `5216` for \(1928\).  Together with the other native pins this
gives 826 distinct simultaneous pins on the former 846-target H21 shore,
so the literal shore gap is 20.  The verifier checks all 6435 central owner
equalities and every selected pin; it does not assert a global 16363-pin
compiler.

## 6. The root-1801 square splitter

In the compressed state, put \(\alpha=1\) and \(\beta=5\).  The second RF
replaces one Boolean-square column by its two parallel \(\beta\)-fibres:

\[
 \{1801,1803,1833,1835\}
 \longrightarrow
 \{1801,1833\},\ \{1803,1835\}.                              \tag{6.1}
\]

The unchanged restricted bank has \(23\) columns and rank \(23\).  The
left side of (6.1) has rank one and the right side rank two, so the component
rank is

\[
 24\longrightarrow25.                                        \tag{6.2}
\]

Consequently the entire root-\(1801\) component disappears.  The final
canonical DM shore is exactly the original H21 shore with the root-\(1920\)
component removed; its other twenty components remain.

The physical cells in (6.1) are

```text
old square: cell 14269, depth 2, start 1394
new edge : cell  9334, depth 1, start 2896, shore {1801,1833}
new edge : cell 16035, depth 2, start 3160, shore {1803,1835}
```

The final carrier has two native trace-\(1833\) cells, `9334` and `9599`.
Deleting coordinate 5 on positions `2896,2897` changes their controller
values from `(1577,809)` to `(1545,777)`, redirects cell `9334` to root
`1801`, and retains cell `9599` at `1833`.  The independent literal audit
keeps all other selected pins and every central owner equality, producing
682 simultaneous pins on the former 702-target critical shore, hence exact
gap 20.  This is shore-local and is not a global 16363-pin common-word
certificate.

## 7. Why the restricted identity alone is insufficient

The full physical shores are larger than their restrictions.  For example,

\[
\begin{aligned}
\{1920,1928\}&\rightsquigarrow
 \{1152,1160,1408,1416,1664,1672,1920,1928\},\\
\{1929\}&\rightsquigarrow\{1665,1673,1921,1929\},\\
\{1801\}&\rightsquigarrow
 \{1280,1281,1288,1289,1792,1793,1800,1801\},\\
\{1801,5897\}&\rightsquigarrow
 \{1792,1793,1800,1801,5888,5889,5896,5897\}.
                                                                    \tag{7.1}
\end{aligned}
\]

Moreover, twenty changed full profiles do not meet either distinguished
restricted component.  Their collateral is exactly what the full-catalogue
capacities in (2.4) audit.  Therefore a future search may not use
\(\Lambda/\Theta\) ranks, endpoint maxima, or component-restricted Hall
alone as a global certificate.

## 8. Predictive physical-signature criterion

The following is a sufficient, proof-safe filter for another two-braid
descent.

### Theorem 8.1 (Lambda-Theta compression and splitter criterion)

Let \(P_0,P_1,P_2\) be legal resident Johnson carriers evaluated with one
identical full-cell catalogue.  Suppose:

1. On one unit-deficient component \(A\) of \(G(P_0)\), the common
   restricted bank has rank \(|A|-7\), the residual exchange is a
   coordinate image of \(\Lambda^-\to\Lambda^+\), and the two complete
   restricted banks have ranks \(|A|-1\) and \(|A|\), respectively.
2. On a connected target set \(B\), the common restricted bank has rank
   \(|B|-3\), the residual exchange is a coordinate image of
   \(\Theta^-\to\Theta^+\), and the two complete restricted banks have
   ranks \(|B|\) and \(|B|-1\), respectively.
3. Every other canonical DM component has the same restricted profile
   multiset in \(P_0\) and \(P_1\), while the new deficient part on \(B\)
   is connected and has gap one.
4. After cancellation of the **full** profile multisets,
   \(\kappa_{\mathcal C}(\mathcal E_0)
    =\kappa_{\mathcal C}(\mathcal E_1)\).
5. Between \(P_1\) and \(P_2\), the common restricted bank on \(B\) has
   rank \(|B|-2\), one residual column of relative rank one is replaced by
   two columns of relative rank two, the complete restricted rank rises
   from \(|B|-1\) to \(|B|\), all other DM component banks remain fixed,
   and the full collar capacity rises by one.

Then \(P_0\to P_1\) is rank-neutral, saturates \(A\), and transfers its
unit deficiency to \(B\); while \(P_1\to P_2\) raises the global matching
rank by one and discharges \(B\).

#### Proof

Conditions 1 and 2 give the restricted ranks

\[
 (|A|-1,|B|)\longrightarrow(|A|,|B|-1).                       \tag{8.1}
\]

Conditions 2 and 3 identify the unique replacement deficient component,
with all other canonical components unchanged.  Condition 4 and Lemma 2.1
prove that no full-shore collateral changes the global rank.  Condition 5
raises the restricted rank of \(B\) by one; its full collar-capacity clause
and Lemma 2.1 raise the global rank by exactly one. \(\square\)

The theorem is predictive in the precise sense needed for a safe search.
The strongest first filter is a coordinate image of the complete 29-cell
full-shore template (5.2), including all six seam edges.  A more general
candidate may instead be recognized from the small normalized restricted
banks.  In either case one must then compute the full 29- or 32-cell collar
capacity against the common profile graph.  The intermediate DM shore size
is an output, not a search objective.

## 9. Reproducibility and remaining boundary

The primary route audit is

```text
scratch/audit_k15_h21_h20_compression_descent.json
```

The two shore-local common-\(Q\) verifiers are

```text
scratch/audit_k15_h21_neutral_root1920_common_q.py
scratch/audit_k15_h21_h20_rooted_native_common_q.py
```

and the Thread-A signature audit is

```text
scratch/threadA_k15_h21_h20_signature_compression_audit.json
scratch/threadA_audit_k15_h21_h20_signature_compression.py
```

The latter independently verifies the twenty unchanged component banks,
the normalized \(\Lambda\), \(\Theta\), and square-split identities, and
the two full collar capacities.

The exact advance is Hall \(21\to20\) with six zeros and a rooted-native
critical shore.  The remaining obstruction is not local rank algebra: it is
to find another legal carrier whose full catalogue satisfies Theorem 8.1 (or
another capacity-increasing identity) while controlling the accumulated
lower-depth collateral and, ultimately, lifting the complete global owner
matching into one word.
