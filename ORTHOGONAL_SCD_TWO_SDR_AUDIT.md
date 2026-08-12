# Orthogonal SCDs versus the depth-one orthogonal two-SDR

## Verdict

Two orthogonal symmetric-chain decompositions do **not** prove the
orthogonal two-SDR lemma.  They canonically give the two injective extension
maps, and orthogonality makes the two extensions at each lower set distinct,
but it does not make their unions distinct.  This failure occurs already in
`Q_4`.

There are nevertheless two useful consequences.

1. An orthogonal pair gives two edge-disjoint perfect matchings on the
   non-singleton middle chains: a lower-colour-perfect matching and an
   upper-colour-perfect matching.  Their union is an exact alternating-cycle
   decomposition.  This is a canonical packet structure for future
   augmentation.
2. Three pairwise orthogonal minimum chain decompositions reduce
   the missing lemma to a three-choice
   upper-colour matching with one explicit covering clause for every
   triple-covered middle vertex.  Every lower vertex then has exactly three
   candidates and every middle vertex occurs in at most six candidates.

Neither statement includes acyclicity of the projected middle graph, nor any
shadow beyond ranks `m-1,m,m+1`.

Throughout, use the conventional almost-orthogonal interpretation for SCDs:
the two longest chains may share `emptyset` and `[2m]`.  Those two extreme
vertices never enter the argument.  Equivalently, move `emptyset` as in the
standard conversion to strictly orthogonal minimum chain decompositions.

The central successor arguments below need only an orthogonal decomposition
into the minimum number `W` of chains.  Symmetry is invoked
explicitly only for the cycle-only conclusion in Section 4.

Put

\[
 \mathcal L=\binom{[2m]}{m-1},\qquad
 \mathcal M=\binom{[2m]}m,\qquad
 \mathcal U=\binom{[2m]}{m+1},
\]

\[
 W=|\mathcal M|,\qquad N=|\mathcal L|=|\mathcal U|,
 \qquad C=W-N=\frac{W}{m+1}=\operatorname{Cat}_m.
\tag{0.1}
\]

## 1. What an orthogonal pair gives for free

Let `D` be a chain decomposition with exactly `W` chains.  For
`S\in\mathcal L`, let

\[
 f_D(S)\in\mathcal M
\]

be the next member of the `D`-chain containing `S`.  Let

\[
 H_D^-=\mathcal M\setminus\operatorname{im}f_D
\tag{1.0}
\]

be its lower-hole family.  If `D` is symmetric, these are precisely the
middle masks whose `D`-chains are singletons.

### Lemma 1 (central successor matching)

The map `f_D` is injective and

\[
 \operatorname{im}f_D=\mathcal M\setminus H_D^-,
 \qquad |H_D^-|=C.
\tag{1.1}
\]

If `D,E` are orthogonal, then

\[
 f_D(S)\ne f_E(S)\qquad(S\in\mathcal L).
\tag{1.2}
\]

#### Proof

Every chain contains at most one middle member.  There are `W` chains and
`W` middle masks, so every chain contains exactly one.  A chain meeting rank
`m-1` therefore has a next, middle member.  Distinct lower masks lie in
distinct chains, proving injectivity and (1.1).  In the symmetric case, a
chain has no rank-`m-1` member precisely when it is a middle singleton.  If
the two successors in
(1.2) were the same `X`, the `D`-chain and `E`-chain containing `S` would
intersect in both `S` and `X`, contrary to orthogonality.  QED.

Consequently, for an orthogonal pair `D,E`,

\[
 f_0=f_D,\qquad f_1=f_E
\tag{1.3}
\]

satisfy the first three conditions of the orthogonal two-extension theorem:
both are injective extensions and they differ pointwise.  The selected
Johnson edges

\[
 f_D(S)f_E(S)
\tag{1.4}
\]

have every lower colour exactly once and middle degree at most two.  The only
unresolved condition is injectivity of

\[
 u_{D,E}(S)=f_D(S)\cup f_E(S).
\tag{1.5}
\]

Thus the central consequence of orthogonality is exactly the easy
`b`-matching half of the depth-one problem, not the upper-colour half.

For a fixed `U\in\mathcal U`, orient every edge with union `U` from its
`D`-successor to its `E`-successor.  Injectivity of the two maps implies that
this local graph has indegree and outdegree at most one.  It is a disjoint
union of directed paths and directed cycles (with no directed 2-cycle), and
in particular

\[
 \#u_{D,E}^{-1}(U)\le m+1.
\tag{1.6}
\]

This is the full collision bound supplied by the two injections alone.

## 2. Explicit `Q_4` counterexample

Here are two almost-orthogonal SCDs of `Q_4`.  Concatenation denotes a chain;
commas separate chains.

\[
\begin{aligned}
D={}&(\varnothing,1,12,123,1234),
 (2,23,234),(3,13,134),(4,14,124),(24),(34),\\
E={}&(\varnothing,4,24,234,1234),
 (1,14,134),(2,12,124),(3,23,123),(13),(34).
\end{aligned}
\tag{2.1}
\]

Direct inspection shows that every cross-pair of chains intersects in at
most one mask, except that the longest chains share the two allowed extreme
masks.

Their central successor maps are

\[
\begin{array}{c|cccc}
S&1&2&3&4\\ \hline
f_D(S)&12&23&13&14\\
f_E(S)&14&12&23&24.
\end{array}
\tag{2.2}
\]

Therefore

\[
 u(1)=u(4)=124,
 \qquad
 u(2)=u(3)=123.
\tag{2.3}
\]

Only two of the four rank-three masks occur.  Hence even a genuine
orthogonal pair can fail the union condition maximally enough to leave half
the upper layer uncovered.

The exhaustive checker `scratch/enumerate_q4_oscd.py` independently
enumerates all 240 SCDs of `Q_4`.  It finds 408 unordered almost-orthogonal
pairs, of which 324 fail union injectivity.  It also recovers (2.1)--(2.3).

### A positive product seed on `Q_6`

The same enumeration contains 84 pairs that *do* have injective unions.
One useful pair is

\[
\begin{aligned}
D_4={}&(\varnothing,1,12,123,1234),(2,23,234),(3,34,134),
       (13),(4,24,124),(14),\\
E_4={}&(\varnothing,4,34,234,1234),(1,14,134),(2,12,124),
       (3,13,123),(23),(24).
\end{aligned}
\tag{2.4}
\]

For a chain `C=(c_0,...,c_h)` and a new coordinate `z`, write

\[
\begin{aligned}
T_z(C)&= (c_0,\ldots,c_h,c_h+z)
       \ \sqcup\ (c_0+z,\ldots,c_{h-1}+z),\\
B_z(C)&= (c_0,c_0+z,\ldots,c_h+z)
       \ \sqcup\ (c_1,\ldots,c_h),
\end{aligned}
\tag{2.5}
\]

omitting an empty second chain.  These are the two standard
Littlewood--Offord decompositions of `C times Q_1`.  Apply `B_5` and then
`B_6` to every chain of `D_4`, and apply the opposite choices `T_5,T_6` to
every chain of `E_4`.  The resulting SCDs `D_6,E_6` remain almost
orthogonal.  Their central successors are:

\[
\begin{array}{c|c|c|c@{\qquad}c|c|c|c}
S&f_D(S)&f_E(S)&u(S)&S&f_D(S)&f_E(S)&u(S)\\ \hline
56&156&456&1456&16&126&146&1246\\
26&256&126&1256&12&123&124&1234\\
36&356&136&1356&13&136&123&1236\\
23&236&235&2356&46&456&346&3456\\
14&146&134&1346&24&246&245&2456\\
34&346&234&2346&15&125&145&1245\\
25&235&125&1235&35&345&135&1345\\
45&245&345&2345&&&&
\end{array}
\tag{2.6}
\]

The last column consists of all fifteen four-subsets of `[6]`, exactly once.
Moreover, orienting every edge from `f_D(S)` to `f_E(S)` gives no directed
cycle.  Its five path components are

\[
\begin{gathered}
236-235-125-145,\qquad 246-245-345-135,\\
156-456-346-234,\qquad 256-126-146-134,\\
356-136-123-124.
\end{gathered}
\tag{2.7}
\]

Hence (2.6) is not just union-perfect: it is a spanning linear forest with
all rank-two intersection colours and all rank-four union colours.

This is a genuine positive depth-one construction for `m=3` obtained from an
orthogonal SCD pair.  It does not iterate under the same globally uniform
lift rule.  Exhaustively starting from all 84 good `Q_4` pairs, trying both
opposite modes at each of four successive one-coordinate lifts, and retaining
all almost-orthogonal outcomes gives:

\[
\begin{array}{c|c|c}
\text{dimension}&\text{orthogonal lift histories}&\text{union-perfect}\\\hline
6&288&24\\
8&1152&0.
\end{array}
\tag{2.8}
\]

At dimension eight the best history has only 50 of 56 upper colours.  Thus
global opposite-mode duplication is a valid `Q_6` constructor but not an
induction.  Per-chain mode choices and non-product SCD pairs remain open.
The construction and exhaustive counts are independently reproduced by
`scratch/lift_good_q4_oscd_to_q6.py`,
`scratch/iterate_good_oscd_lifts.py`, and
`scratch/check_oscd_product_successors.py`.

## 3. A new necessary lower-hole moment law

For `z in [2m]`, put

\[
 h_D(z)=|\{X\in H_D^-:z\in X\}|,
 \qquad
 h_E(z)=|\{X\in H_E^-:z\in X\}|.
\tag{3.1}
\]

For the union multiplicities

\[
 c(U)=|\{S\in\mathcal L:u_{D,E}(S)=U\}|,
\tag{3.2}
\]

define their first-moment defect

\[
 \Delta_z=\sum_{U\ni z}(c(U)-1).
\tag{3.3}
\]

### Theorem 2 (lower-hole moment identity)

For every coordinate `z`,

\[
 \boxed{\Delta_z=C-h_D(z)-h_E(z).}
\tag{3.4}
\]

In particular, union injectivity requires

\[
 h_D(z)+h_E(z)=C\qquad(z\in[2m]).
\tag{3.5}
\]

If `q` upper masks are missing, then

\[
 q\ge \max_z|C-h_D(z)-h_E(z)|,
\tag{3.6}
\]

and

\[
 q\ge
 \left\lceil
 \frac{\sum_z|C-h_D(z)-h_E(z)|}{2(m+1)}
 \right\rceil.
\tag{3.7}
\]

#### Proof

There are

\[
 \binom{2m-1}{m-2}
\]

lower masks containing `z`.  The number of lower masks not containing `z`
whose `D`-successor adds `z` is

\[
 \left(\binom{2m-1}{m-1}-h_D(z)\right)
 -\binom{2m-1}{m-2}
 =C-h_D(z).
\tag{3.8}
\]

The analogous count for `E` is `C-h_E(z)`.  The two added coordinates at a
fixed lower mask are distinct by (1.2), so these two event families are
disjoint.  Hence the number of selected union occurrences containing `z` is

\[
 \binom{2m-1}{m-2}+2C-h_D(z)-h_E(z).
\tag{3.9}
\]

The complete upper layer contains

\[
 \binom{2m-1}{m}
 =\binom{2m-1}{m-2}+C
\tag{3.10}
\]

members containing `z`.  Subtraction proves (3.4).

Since `sum_U c(U)=N`, the total positive surplus of `c(U)-1` equals the
number `q` of zeros, and so does its total negative mass.  This gives
`|Delta_z|<=q`.  Finally,

\[
 \sum_z|\Delta_z|
 \le\sum_U|c(U)-1||U|=2(m+1)q,
\]

which proves (3.6)--(3.7).  QED.

For the pair (2.1), `C=2` and the defect vector is

\[
 (\Delta_1,\Delta_2,\Delta_3,\Delta_4)=(1,1,-1,-1).
\]

The condition is not sufficient.  For the standard Greene--Kleitman SCD and
its complement, `H_E^-={X^c:X in H_D^-}`, so (3.5) holds identically.  Nevertheless,
on `Q_6` the two unions

\[
 1346,\qquad2345
\]

each occur twice, while `1234` and `3456` are missing.  The two collisions
come respectively from the lower pairs

\[
 13,46\qquad\text{and}\qquad25,34.
\]

This is checked for `m=1,...,8` by
`scratch/check_oscd_two_sdr.py`.

## 4. The dual upper matching and an alternating path/cycle skeleton

For `U\in\mathcal U`, let `p_D(U)` be the rank-`m` predecessor of `U` in its
`D`-chain, and define `p_E(U)` similarly.  Put

\[
 H_D^+=\mathcal M\setminus\operatorname{im}p_D,
 \qquad
 H_E^+=\mathcal M\setminus\operatorname{im}p_E.
\tag{4.1}
\]

Both `p` maps are injective and both upper-hole families have size `C`.
Make bipartite copies of the full middle layer and define

\[
 F_- =\{(f_D(S),f_E(S)):S\in\mathcal L\},
\tag{4.2}
\]

\[
 F_+ =\{(p_D(U),p_E(U)):U\in\mathcal U\}.
\tag{4.3}
\]

### Theorem 3 (colour-polarized alternating paths and cycles)

`F_-` is a perfect matching from `\mathcal M\setminus H_D^-` to
`\mathcal M\setminus H_E^-`, and `F_+` is a perfect matching from
`\mathcal M\setminus H_D^+` to `\mathcal M\setminus H_E^+`.  They are
edge-disjoint.  Consequently

\[
 F_-\cup F_+
\]

is a disjoint union of alternating paths and even cycles.  If `D,E` are
symmetric, then `H_D^-=H_D^+` and `H_E^-=H_E^+`, so there are no paths and
every component is an alternating cycle of length at least four.
Every edge of `F_-` is a Johnson edge, and its intersection colours enumerate
`\mathcal L` exactly once.  Every edge of `F_+` is a Johnson edge, and its union
colours enumerate `\mathcal U` exactly once.

#### Proof

The matching statements follow from Lemma 1 and its rank-reversed analogue.
If an ordered middle pair `(X,Y)` occurred in both matchings, the `D`-chain
centred at `X` and the `E`-chain centred at `Y` would share both the
corresponding lower mask and the corresponding upper mask.  Orthogonality
forbids this, proving edge-disjointness.  A union of two matchings has the
asserted alternating path/cycle decomposition.  In a symmetric chain, rank
`m-1` occurs if and only if rank `m+1` occurs, proving equality of the active
families and the cycle-only conclusion.

For an `F_-` edge, its two distinct middle endpoints contain the same
rank-`m-1` set, so their intersection is that set.  The dual argument proves
the union statement for `F_+`.  QED.

This is a genuine augmentation scaffold supplied by an orthogonal pair.
It is not itself the desired matching: taking the `F_-` parity makes all
lower colours correct, while taking the `F_+` parity makes all upper colours
correct.  Flipping an alternating component generally destroys the colour
ledger on the opposite side.  The two 4-cycles printed by the `Q_4` checker
give the smallest example.

## 5. What a third orthogonal decomposition buys

Let `D_0,D_1,D_2` be three pairwise orthogonal decompositions into `W`
chains and write

\[
 f_i:\mathcal L\longrightarrow\mathcal M
\]

for their successor maps.  For each `S`, the three masks `f_i(S)` are
distinct.  For `o in {0,1,2}`, define the candidate obtained by omitting
colour `o`:

\[
 e_o(S)=\{f_i(S):i\ne o\},
 \qquad
 u_o(S)=\bigcup_{i\ne o}f_i(S).
\tag{5.1}
\]

The three upper candidates `u_0(S),u_1(S),u_2(S)` are distinct.

For a middle mask `X`, put

\[
 t_X=|\{i:X\in\operatorname{im}f_i\}|.
\tag{5.2}
\]

When `X in im f_i`, let `S_i(X)` be its unique preimage.

### Theorem 4 (exact three-decomposition reduction)

The three decompositions contain a feasible depth-one diamond selection if
and only if there is a function

\[
 o:\mathcal L\longrightarrow\{0,1,2\}
\tag{5.3}
\]

such that

1. the `N` upper masks `u_{o(S)}(S)` are all distinct; and
2. for every `X` with `t_X=3`,

   \[
   o(S_i(X))=i\quad\text{for at least one }i\in\{0,1,2\}.
   \tag{5.4}
   \]

The chosen diamond for `S` is `e_{o(S)}(S)`.

#### Proof

Every choice uses one Johnson edge with lower colour `S`.  Distinct chosen
upper colours are automatically all of `\mathcal U`, since both layers have
size `N`.

For a fixed middle mask `X`, colour `i` contributes one selected incidence
exactly when `X in im f_i` and the choice at its unique preimage does not omit
`i`.  Its load is therefore

\[
 t_X-|\{i:o(S_i(X))=i\}|.
\tag{5.5}
\]

This is automatically at most two for `t_X<=2`, and for `t_X=3` it is at
most two exactly under (5.4).  QED.

This is a sparse, bounded-choice reformulation:

* every lower set has exactly three candidate diamonds;
* a middle mask occurs in at most six candidates (two for each successor
  colour in whose image it lies);
* a fixed upper mask is incident with at most

  \[
  \left\lfloor\frac{3(m+1)}2\right\rfloor
  \tag{5.6}
  \]

  candidates.

For (5.6), charge a candidate at `U` to its two middle facets of `U`, each
tagged by the SCD colour producing that facet.  Injectivity of every `f_i`
allows each of the `3(m+1)` tagged facets to be charged at most once.

Theorem 4 is a material simplification, but it is still a matching problem
with covering clauses; ordinary Hall applied only to the upper candidates
does not enforce (5.4).  Moreover, three arbitrary edge-disjoint extension
matchings need not even have an upper perfect matching.  The deterministic
checker `scratch/check_three_extension_catalog.py` decomposes the full
rank-`(m-1)`/rank-`m` incidence graph into extension matchings.  At `m=5`,
several triples leave an upper vertex isolated.  This last computation is a
counterexample to a shortcut based only on the central injection axioms; it
is not asserted to extend to three globally orthogonal SCDs.

## 6. Relation to the published existence theorems

Shearer--Kleitman give two orthogonal minimum chain decompositions in every
dimension.  More strongly for the present application, Spink's Corollary
10.7 gives three orthogonal minimum chain decompositions of `Q_n` for every
`n>=4`, with only the possible odd exceptions `9,11,13,23`.  Apart from the
separately handled case `n=4`, it obtains the even cases from odd cases by
duplicating every chain.  Duplication preserves
the minimum chain count, which is exactly the structural hypothesis of
Theorem 4, although the resulting even-dimensional chains need not be
symmetric.  Changes involving the empty mask do not affect the three central
ranks.

Therefore three decompositions, and hence the exact three-choice system of
Theorem 4, are available for **every** even dimension `2m>=4`.  This is a
genuine all-`m` reduction of the depth-one problem.  It does not prove that
the three-choice system has a solution.

In fact, the particular even-dimensional triples used in that existence
proof are provably unsuitable here.

### Theorem 5 (sector Hall obstruction for duplicated triples)

Let three minimum chain decompositions of `Q_(2m-1)` be lifted to `Q_(2m)` by
replacing every chain `C` by the two chains

\[
 C,\qquad C+z,
\tag{6.1}
\]

where `z` is the new coordinate.  For `m>=2`, the three-choice upper graph of
Theorem 4 has no perfect matching.  More precisely, it has a Hall deficiency
of at least

\[
 \binom{2m-1}{m-1}-\binom{2m-1}{m+1}>0.
\tag{6.2}
\]

#### Proof

Let `A` be all rank-`m-1` lower masks avoiding `z`.  In every duplicated
decomposition, the chain containing such an `S` is an untagged chain `C`.
Its middle successor also avoids `z`.  Hence all three successors of `S`,
and therefore all three candidate unions in (5.1), avoid `z`.

There are

\[
 |A|=\binom{2m-1}{m-1}
\]

such lower masks, but only

\[
 \binom{2m-1}{m+1}=\binom{2m-1}{m-2}
\]

rank-`m+1` upper masks avoiding `z`.  Their ratio is

\[
 \frac{\binom{2m-1}{m-1}}{\binom{2m-1}{m-2}}
 =\frac{m+1}{m-1}>1.
\]

Hall's inequality fails by at least (6.2).  QED.

For Spink's displayed `Q_7` triple duplicated to `Q_8`, the witness consists
of all 35 rank-three masks avoiding coordinate 8; they have only the 21
rank-five masks avoiding coordinate 8 as candidates.  The full candidate
graph has maximum matching size 42 rather than 56.  The parser, all
orthogonality/partition checks, the candidate graph, and the Hall witness are
in `scratch/spink_q8_three_choice.py`.

Thus the published existence of three decompositions does not by itself
advance the upper matching: its canonical even-dimensional construction is
sector-separated in exactly the wrong way.  A useful triple must mix the new
coordinate across its central chains.

For comparison, Spink's Corollary 10.6 gives three almost-orthogonal SCDs for
`n>=5` except possibly `6,8,9,11,13,16,18,23`, and he notes that three
almost-orthogonal SCDs do not exist on `Q_4`.  The exhaustive `Q_4` checker is
consistent with this distinction: it finds no symmetric triple, while
Corollary 10.7 concerns general minimum chain decompositions.

The exact next lemma suggested by this audit is therefore one of the
following, neither presently proved:

* an augmentation theorem that mixes the colour-polarized cycles of Theorem
  3 while preserving both colour ledgers; or
* for a non-sector-preserving explicit triple, a perfect matching in the
  three-choice graph of Theorem 4 that simultaneously satisfies all
  triple-covered-middle clauses (5.4).

Either would solve the upper-colour obstruction at depth one.  Neither would
by itself prove longer shadows, consecutive ordering, or pin survival.

## References

* Hunter Spink, *Orthogonal Symmetric Chain Decompositions of Hypercubes*,
  arXiv:1706.08545.
* Karl Däubel, Sven Jäger, Torsten Mütze, and Manfred Scheucher,
  *On orthogonal symmetric chain decompositions*, arXiv:1810.09847.
