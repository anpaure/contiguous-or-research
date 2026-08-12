# Thread A: the Hall-21 \(C_{8218}\) laminar-router filter

Date: 2026-07-28

Status: superseded as a frontier note by the subsequently audited
\(H21\to H21\to H20\) route.  The \(C_{8218}\) literal-transplant
obstruction and filter below remain valid branch-local statements; see
THREAD_A_H21_H20_COORDINATE_CONJUGATE_DEFECT_TRANSPOSITION_20260728.md
for the successful route.

## 1. Audited input and direct one-braid floor

The input is

    scratch/k15_segment_braid_hall21_zero6.json

with SHA-256

    8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447.

Its lower-compiler matching number is \(16362\), its Hall deficiency is
\(21\), and it has six zero-candidate targets. Its canonical deficient DM
shore has size \(846/825\) and consists of exactly twenty-one connected
components, every one of gap one. The 825 right-shore cells have 825
distinct valid native traces.

An H100 run of scratch/search_k15_segment_braid_native.cpp over the full
three-cut catalogue FF/RF/FR/RR, with exact Johnson, depth-three residence,
all-upper-support, and at-most-four immediate-lower-hole filters, returned

    SUMMARY johnson=546890 resident=12012 upper_safe=9185 target=9185
            best_hall=21 best_zero=6

There were 7,300 Hall-scored moves after the immediate-lower-hole cutoff:

    (21,6):7120  (21,7):2  (22,6):121  (22,7):5
    (23,6):43    (23,7):2  (24,6):3    (25,6):2  (26,6):2.

The 7,120 entries at \((21,6)\) contain 6,433 copies of the trivial move
\(RR(a,a)\), hence 687 nontrivial protected-neutral first braids. There is
no Hall-20 one-braid descendant in this exact move class. This is not a
no-go for arbitrary path surgery.

## 2. Reusable six-boundary identity

Let \(K\) be a six-set and let \(a,b,c,d\notin K\) be distinct. Put

\[
 L_{ab}=K\cup\{a,b\},\quad L_{bc}=K\cup\{b,c\},\quad
 L_{ca}=K\cup\{c,a\},
\]

and

\[
 R_a=K\cup\{a,d\},\quad R_b=K\cup\{b,d\},\quad
 R_c=K\cup\{c,d\}.
\]

The bipartite Johnson graph induced by these six vertices is a \(C_6\).
Its two perfect matchings have the same lower turn-colour multiset

\[
 \{K\cup\{a\},K\cup\{b\},K\cup\{c\}\},                 \tag{2.1}
\]

and upper turn-colour multiset

\[
 \{K\cup\{a,b,d\},K\cup\{b,c,d\},K\cup\{c,a,d\}\}.     \tag{2.2}
\]

Indeed, an edge \(L_{ij}R_i\) has intersection \(K\cup\{i\}\) and union
\(K\cup\{i,j,d\}\), and either perfect matching uses every active
coordinate and pair once. Thus switching the two matchings is exactly
neutral at both depth-one shores.

This is the Boolean/laminar boundary identity behind

\[
 FF(1320,5339,6194)
\]

on the Hall-22 carrier, where

\[
 K=\{1,6,7,8,10,11\},\qquad \{a,b,c\}=\{0,3,4\},\qquad d=12.
\]

It proves only the depth-one ledger. Residence, deeper collars, DM
incidence, and common-\(Q\) remain statewise conditions.

## 3. Why \(C_{8218}\) is the first component

The unique Hall-21 component with the size and rank profile of the component
compressed by the preceding router is

\[
 C_{8218}:\quad 160/159,\qquad
 (n_4,n_5,n_6,n_7)=(1,9,43,107).                       \tag{3.1}
\]

Every target in it contains

\[
 8218=\{1,3,4,13\}.                                    \tag{3.2}
\]

The old \(C_{449}\) target family is coordinate-isomorphic to the complete
\(C_{8218}\) target family. A map maximizing restricted-bank overlap is

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
x&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\ \hline
\phi(x)&1&12&9&14&5&11&3&4&13&0&6&7&8&2&10.
\end{array}                                             \tag{3.3}
\]

It maps \(449=\{0,6,7,8\}\) to \(8218\). The mapped old target-family
digest equals the direct \(C_{8218}\) digest:

    e4a882118400bd1ad3de87ffb49573b1ec63a853eb0f9a19c600f8486d2c5638.

Of 576 coordinate bijections compatible with the levelwise point degrees,
exactly 192 map the complete target family onto \(C_{8218}\). None maps the
complete restricted physical incidence bank. The maximum common
multiplicity is \(142/159\), attained by twenty-four maps including (3.3);
even the best map leaves seventeen old and seventeen new shores. The
common-count distribution is

\[
98^{(72)},105^{(24)},111^{(24)},113^{(24)},121^{(24)},142^{(24)}. \tag{3.4}
\]

Thus \(C_{8218}\) is the correct laminar target, but the old router is not
an incidence conjugacy. Both component banks separately have 159 distinct
valid native traces, with digests

    C449:  f9ac1178c98ad8ffb8588dccce6460e8f32d7f4bb3bcc417dd3648074da6b185
    C8218: c88f7d91a4efa9baac59c7f6d9774d22036d6d9b819abe06acf19003d5a1170f

## 4. Obstruction to the literal transported router

Transport the three old \(C_6\) seam edges by each of the 192 target-family
isomorphisms and require all three transported edges to occur as physical
adjacent edges of the Hall-21 path. Exactly twenty-four maps pass. They
collapse to two cut triples and six possible braids:

\[
\begin{array}{c|c|c}
(a,u,v)&\text{kind}&\text{first exact failure}\\ \hline
(1254,3146,3982)&FF&\text{one new seam has Hamming distance }4\\
                 &RF&\text{new seams have Hamming distance }4\\
                 &FR&\text{internal runs of lengths }1,2,3\\ \hline
(1934,3485,4141)&FF&\text{one new seam has Hamming distance }4\\
                 &RF&\text{internal runs of lengths }3,2\\
                 &FR&\text{internal runs of lengths }1,2.
\end{array}                                             \tag{4.1}
\]

The residence failures of the three Johnson-legal rows are

\[
\begin{aligned}
FR(1254,3146,3982):&\ (1;2090,2090),(7;1253,1254),(13;2089,2091),\\
RF(1934,3485,4141):&\ (3;4140,4142),(7;1933,1934),\\
FR(1934,3485,4141):&\ (1;4141,4141),(7;1933,1934).
\end{aligned}                                           \tag{4.2}
\]

Here \((x;s,t)\) denotes the internal run of coordinate \(x\) on
\([s,t]\). Each length is below four.

**Proposition 4.1.** No coordinate image of the exact Hall-22 \(C_6\)
boundary packet which maps the whole \(C_{449}\) target ideal to
\(C_{8218}\), and whose three old seam edges are physical Hall-21 edges,
gives a legal one-braid router.

This does not exclude a different physical \(C_6\), temporary ideal
changes, or a compound neutral router.

## 5. Proof-safe H100 search for \(H21\to H20\)

Generate exactly the 687 nontrivial neutral states by running on H100

    ./search_k15_segment_braid_native \
      k15_segment_braid_hall21_zero6.json 0 hall 4 0 21 6

and discarding every \(RR(a,a)\). Deduplicate complete middle paths.

For every state \(G_1\):

1. Reconstruct the complete compiler graph. Verify the middle permutation,
   every Johnson edge, full residence, at most six zero targets, at most
   four immediate-lower holes, and complete upper support for
   \(1\le q\le7\).
2. Verify \(\nu(G_1)=16362\), hence Hall deficiency 21.
3. Compute the full DM decomposition. In the prioritized
   \(C_{8218}\)-compression branch require that the old \(160/159\)
   component no longer survives as the same connected component, that its
   old right bank meets the exact changed-cell collar, and that a
   replacement gap-one component \(C'\) is created. Rank by \(|C'|\).
4. Cancel old and new full cell-shore multisets with multiplicity. If \(r\)
   is the common-bank matching rank, require the neutral equality
   \[
      \nu(G_0)-r=\nu(G_1)-r.                            \tag{5.1}
   \]
5. Require the canonical DM-right bank of \(G_1\) to have pairwise distinct
   valid native traces in its canonical left shore.

For each survivor, enumerate all second braids whose exact changed-cell
collar meets \(C'\). The audited general collar bound is ninety physical
cells for a three-cut move, so this intersection condition is necessary for
a splitter of \(C'\).

Accept an endpoint \(G_2\) only if all structural tests above hold and

\[
 \nu(G_2)=16363,\qquad h(G_2)=20.                       \tag{5.2}
\]

After cancelling the \(G_1,G_2\) full shore multisets, with common-bank rank
\(r'\), require

\[
 \nu(G_2)-r'=\nu(G_1)-r'+1.                             \tag{5.3}
\]

In the clean component-discharge branch also require

\[
 C'\subseteq L(G_1)\setminus L(G_2),\qquad L(G_2)\subseteq L(G_1), \tag{5.4}
\]

and check directly that new boundary cells saturate \(C'\) while the common
bank retains a matching off \(C'\). This proves the gain independently of
one arbitrary maximum matching.

For an all-shore audit, if \(A_i\) is the canonical DM-left shore of \(G_i\),
compute

\[
 g_{ij}=|A_j|-|N_{G_i}(A_j)|.                          \tag{5.5}
\]

The sharp router/splitter pattern to seek is

\[
 (g_{ij})=
 \begin{pmatrix}21&20&20\\20&21&20\\20&20&20\end{pmatrix},       \tag{5.6}
\]

with smaller off-diagonal entries also favourable. The full matching
calculation in (5.2), not this \(3\times3\) sample alone, certifies all
other shores.

## 6. Exact common-\(Q\) filter

Let \(P_p\) be the maximal erosion letter at physical position \(p\). A
cell \(c=(s,d)\) has \(I_c=[s,s+d]\) and native trace

\[
 \tau(c)=\bigcup_{p\in I_c}P_p.                         \tag{6.1}
\]

The fast sufficient test is native current: retain one cell for every
distinct trace in the claimed critical shore. The unchanged word \(P\)
realizes all such pins simultaneously. At a Hall-20 endpoint require at
least \(|A|-20\) distinct native traces on every critical shore \(A\) being
transported, and require the final canonical DM-right bank itself to be
native-injective.

For fixed nonnative pins \(\mathcal M=\{(S,c)\}\), the exact test is also
finite. For every coordinate \(x\), put

\[
 A_x=\{p:x\in P_p\},\qquad
 B_x=\bigcup_{(S,c)\in\mathcal M,\ x\notin S}I_c,\qquad
 Q_x=A_x\setminus B_x.                                  \tag{6.2}
\]

A common physical word for these fixed pins exists if and only if:

1. every physical position belongs to some \(Q_x\);
2. for every middle owner \(T_i\) and \(x\in T_i\),
   \(Q_x\cap[i,i+3]\ne\varnothing\);
3. for every pin \((S,c)\) and \(x\in S\),
   \(Q_x\cap I_c\ne\varnothing\).

Necessity is immediate. For sufficiency, put \(x\) at exactly the positions
\(Q_x\). Equation (6.2) enforces every negative pin constraint and the
three conditions give nonempty letters, central reconstruction, and every
positive pin. Conversely, enlarging any feasible word to the maximal
surviving \(Q_x\) cannot destroy a positive condition.

This test must be applied to one selected matching, not separately to cell
marginals.

## 7. Proved boundary

The direct protected one-braid floor \(h=21\), the \(C_6\) identity, the
complete \(C_{449}\to C_{8218}\) target-family isomorphism census, and the
failure of every literal transported router are established. No explicit
\(H21\to H20\) sequence has been found. The minimum surviving route is one
of the 687 genuinely statewise neutral braids changing the physical
incidence bank of \(C_{8218}\) (or another unit component), followed by a
collar-intersecting splitter satisfying (5.2)--(6.2).
