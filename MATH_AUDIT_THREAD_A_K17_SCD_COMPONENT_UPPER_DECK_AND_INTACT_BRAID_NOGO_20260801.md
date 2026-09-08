# The authenticated `m=9` SCD forest: exact upper deck and an intact-component braid obstruction

Date: 2026-08-01  
Lane: A, finite `k=17` SCD multi-component carrier  
Status: **RETRACTED AS AN ARBITRARY-WIDTH CLAIM.**  The census below fixes
the owner-window length to `q+1`; arbitrary interval witnesses may be longer
while retaining rank `9+q`.  It therefore audits only the shortest-window
subdeck and does not prove an intact-braid no-go.  A corrected all-interval
resident-piece audit supersedes it.

Former status: exact certificate replay, complete internal upper-deck census, and a
solver-free characterization plus finite certificate showing that no
permutation/reversal of the intact components can be arbitrary-width upper
complete.  Component depth-three source factorability, residence and the
generalized lower compiler are separate rows and are not decided here.

## 0. Verdict

The authenticated parity-completed rotation forest on the rank-nine layer of
`B_18` has

\[
 48620\text{ owners},\qquad 43758\text{ edges},\qquad
 C=4862=\operatorname{Cat}_9\text{ path components}.             \tag{0.1}
\]

Its intact-component arbitrary-width upper deck is complete at widths
`q=1,6,7,8,9`, but not at widths `q=2,3,4,5`.  The exact missing-bank sizes
are

\[
 \begin{array}{c|rrrrrrrrr}
 q&1&2&3&4&5&6&7&8&9\\ \hline
 |\mathcal E_q|&0&7848&3513&774&54&0&0&0&0.
 \end{array}                                                   \tag{0.2}
\]

More strongly, keep every component intact and allow an arbitrary ordering,
either orientation of every nontrivial path, and even arbitrary
**non-Johnson** jumps at the `4861` component seams (the most permissive
interpretation of omitted lower-seam cells).  Then 126 of the rank-eleven
targets in `\mathcal E_2` still have no possible crossing occurrence.  They
form the seven full `C_18`-orbits with canonical representatives

\[
  \boxed{37f5,\ a9fb,\ b5cf,\ b7ab,\ cf6d,\ d767,\ f55b}.        \tag{0.3}
\]

Consequently the proposed intact `4862`-block concatenation is not
upper-complete, independently of scalar slack, generalized-lower matching,
or common-cap feasibility.  A successful construction must split/rethread at
least one component, insert an additional owner state at a seam, or otherwise
change the endpoint occurrence bank.

If every seam is required to be a literal Johnson connector (and hence to
belong to the connector-repeat cocycle palette), the corresponding unsupported
rank-eleven bank is larger: 936 targets.

## 1. Authentication

The compact selected-orbit certificate is

`scratch/catalan_rotation_m9_half_full_20260801.audit.json`, SHA-256

`f48e74dbfaad4e761db2cee374ea5e01cfa2c2db6ce18f887192a12240a83bde`.

The independent literal replay in

`scratch/audit_catalan_rotation_m9_half_certificate_20260801.py`

certifies the physical-edge SHA-256

`005dfdc24b643e4bd3176548ee2ae0deeb00d31ec3b9404d4a4c7f2e0982f7c1`,

all rank-eight and rank-ten colours exactly once, maximum middle degree two,
and exactly 4,862 path components with no cycle.  Its audit is

`scratch/catalan_rotation_m9_half_certificate_20260801.audit.json`, SHA-256

`6f5a44176a6ca177d67b18d3ac7ecd1aaabe39c89806fc20bda55f86bd18e3eb`.

The component census independently gives 938 isolated vertices, 7,848
degree-one vertices, and 39,834 degree-two vertices.

The new upper-deck replay streams the canonical candidate catalogue rather
than retaining its 108,000-plus candidates.  It reconstructs the selected
physical edge set byte-identically before doing any upper calculation:

* script:
  `scratch/audit_threadA_catalan_m9_component_upper_decks_20260801.py`;
* audit:
  `scratch/threadA_catalan_m9_component_upper_decks_20260801.audit.json`.

Their SHA-256 values are, respectively,

`8a3403e435bdf4316166668a5d33ddf7e24348f933112e97f1dc7597d1feb20a`

and

`0f0682030bc935984b246dcb896cc7c049455af73cd9dd7f5b47d5e1b1ca89d0`.

The audit payload SHA-256 is

`9ba038030eae2521889afee768cd940bb54cec3a9b0dd2a96359aa8edb201171`.

## 2. The exact internal upper deck

Let a forest component be the owner path

\[
                 P=(O_0,O_1,\ldots,O_s),
       \qquad O_i\in\binom{[18]}9.                    \tag{2.1}
\]

For `q>=1`, define its width-`q` upper deck by

\[
 \mathcal W_q(P)=
 \left\{
   O_i\cup O_{i+1}\cup\cdots\cup O_{i+q}:
   0\le i\le s-q,\ 
   \left|\bigcup_{j=0}^qO_{i+j}\right|=9+q
 \right\}.                                           \tag{2.2}
\]

For the whole forest `F`, put

\[
                  \mathcal W_q(F)=\bigcup_P\mathcal W_q(P),
 \qquad
 \mathcal E_q(F)=\binom{[18]}{9+q}\setminus\mathcal W_q(F).      \tag{2.3}
\]

This deck is invariant under component permutation and reversal.  It is the
complete upper information that survives automatically when all components
are retained as blocks.  No source word is needed to define it.

### Theorem 2.1 (exact internal-deck census)

For the authenticated forest, the full row is

\[
\begin{array}{c|r|r|r|r|r}
q&\binom{18}{9+q}&\text{internal windows}&
 \text{exact-rank windows}&|\mathcal W_q(F)|&|\mathcal E_q(F)|\\ \hline
1&43758&43758&43758&43758&0\\
2&31824&39834&39834&23976&7848\\
3&18564&36279&32157&15051&3513\\
4& 8568&33102&22230& 7794& 774\\
5& 3060&30123&13050& 3006&  54\\
6&  816&27450& 6102&  816&   0\\
7&  153&24984& 2286&  153&   0\\
8&   18&22788&  576&   18&   0\\
9&    1&20790&   81&    1&   0.
\end{array}                                                    \tag{2.4}
\]

In particular the minimal exterior upper witness bank for an intact-block
construction is exactly the four banks in (0.2), with total cardinality

\[
                      7848+3513+774+54=12189.          \tag{2.5}
\]

#### Proof

The replay orders each path from an endpoint and enumerates every consecutive
`q+1` owner block.  It retains the OR exactly when its rank is `9+q`, stores
the distinct mask, and compares with the complete rank-`9+q` layer.  Reversal
does not alter the set of consecutive blocks.  The streamed reconstruction
first reproduces the frozen physical-edge hash, so the enumeration is on the
authenticated forest.  This gives (2.4).  Equation (2.5) is a sum over
different ranks. \(\square\)

The q1 row is the original exact upper palette.  It does not imply q2: the
q2 deck already has 7,848 holes.

## 3. Exact crossing classification at width two

The q2 row is decisive because a length-three owner window can cross at most
two component seams.

For a nontrivial component, call `(w,u)` an endpoint edge when `u` is an
endpoint and `w` its unique neighbour.  For every component, including an
isolated one, call `u` an endpoint owner when it can be placed first or last
by orienting that component.

### Lemma 3.1 (all intact-block q2 crossing forms)

Let `X` have rank eleven and suppose `X` is realized by a length-three owner
window in a concatenation of whole, pairwise distinct components.  If the
window is not internal to one component, exactly one of the following holds.

1. **One seam.**  There is an endpoint edge `(w,u)` of one component and an
   endpoint owner `v` of a different component such that

   \[
                              w\cup u\cup v=X.         \tag{3.1}
   \]

2. **Two seams.**  There are three distinct components with endpoint owners
   `u,v,w`, the middle component is the isolated singleton `(v)`, and

   \[
                              u\cup v\cup w=X.         \tag{3.2}
   \]

Conversely, either datum can be placed as a local whole-component
concatenation by orienting the endpoint components appropriately.  If seams
must be Johnson edges, add respectively

\[
 |u\triangle v|=2,
 \qquad	ext{or}\qquad
 |u\triangle v|=|v\triangle w|=2.                    \tag{3.3}
\]

#### Proof

A three-owner window crossing one seam splits as `2+1` or `1+2`; reversing
the local picture gives (3.1).  A window crossing two seams splits as
`1+1+1`, so the entire middle component consists of its one owner, giving
(3.2).  No third seam is possible.  Conversely, endpoints may be made
terminal/initial by reversing their paths.  The extra conditions (3.3) are
exactly Johnson adjacency at the seam. \(\square\)

This lemma is a local support theorem.  It does not assert that individually
available occurrences can be packed simultaneously into one component
permutation.

### Theorem 3.2 (126-target intact-braid obstruction)

For the authenticated forest, exactly 126 members of `\mathcal E_2(F)` admit
neither (3.1) nor (3.2), even without the Johnson restrictions (3.3).  They
are the seven rotation orbits in (0.3).  Therefore no ordering and reversal
of the intact components, with arbitrary omitted-seam jumps, has complete
rank-eleven upper deck.

If (3.3) is imposed, exactly 936 members of `\mathcal E_2(F)` have no local
provider.

#### Proof

There are 8,786 distinct endpoint owners and 7,479 endpoint-edge upper
labels.  For each of the 7,848 q2 holes, the audit enumerates its 55 rank-nine
facets and 11 rank-ten facets.  It tests every component-distinct pair in
(3.1), then every isolated-middle triple in (3.2).  This is exhaustive by
Lemma 3.1.  Exactly 126 masks fail.  Rotating each mask shows seven disjoint
orbits of length 18 with the representatives (0.3).  Repeating the same test
with (3.3) leaves 936 masks. \(\square\)

The obstruction is stronger than a bad canonical order: it quantifies over
all whole-component orders and orientations.  It is weaker than a global
`k=17` impossibility: splitting components, adding seam owners, or changing
the forest invalidates Lemma 3.1's intact-block hypothesis.

## 4. A canonical raw concatenation is far from enough

For calibration, orient every path from its smaller endpoint and sort paths
lexicographically.  Form the raw owner list by concatenation, without
claiming a common source.  Its crossing windows add only

\[
 \begin{array}{c|rrrr}
 q&2&3&4&5\\ \hline
 \text{new missing-bank targets filled}&148&173&126&38\\
 \text{holes remaining}&7700&3340&648&16.
 \end{array}                                             \tag{4.1}
\]

Widths 6 through 9 were already complete internally.  The q1 crossing
values add no new target because the internal q1 deck is exact.

Equation (4.1) is not an optimization result and is not used in Theorem 3.2.
It simply shows that a neutral ordering does not accidentally solve the
exterior bank.

## 5. Relation to the connector cocycle palette

For a Johnson braid of the `C` components, the repeated connector-upper
multiset `R` must satisfy the exact coordinate cocycle

\[
 \deg_R(x)=2c+\mathbf1_{x\in K_0}
 -\mathbf1_{x\in T^-}-\mathbf1_{x\in T^+}.           \tag{5.1}
\]

With adjacent endpoints, adjoining `R_0=T^-\cup T^+` gives a size-`C`
rank-ten multiset regular of coordinate degree `2c`.  Abstract such palettes
exist by the biregular incidence construction.

Theorem 3.2 identifies a strictly later row.  The abstract cocycle palette
does not choose endpoint occurrences, and 936 q2 holes have no occurrence
even before the cocycle degrees are imposed on a Johnson intact-component
braid.  Thus the connector palette is necessary for q1 accounting but cannot
by itself make this fixed forest all-width upper exact.

On the omitted-seam face the Johnson/cocycle restriction is dropped, yet the
126-target obstruction survives.  Hence allowing all 4,861 lower seam cells
to be omitted does not close the upper row while the components remain
intact.

## 6. Exact remaining finite gate

The intact-block face is closed at q2.  The smallest legitimate extensions
of the finite model are:

1. split/rethread selected components, thereby creating new endpoint edges
   or endpoint owners for the seven missing rotation orbits;
2. place additional owner states at selected seams; or
3. alter the central forest while preserving its exact q1 palettes and cap
   two.

Any such extension must then be retested jointly for:

* component depth-three maximal-source reconstruction;
* signed residence;
* all upper widths, including casualties of every cut component edge;
* the generalized lower compiler/common-Q state; and
* final length/slack.

The present result decides none of those expanded faces.  It does decide the
specific proposal consisting only of the authenticated 4,862 intact path
blocks plus 4,861 omitted seams: that proposal cannot be arbitrary-width
upper complete.
