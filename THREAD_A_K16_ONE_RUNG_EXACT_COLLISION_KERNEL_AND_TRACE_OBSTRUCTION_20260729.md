# Exact one-rung collision kernel and the minimal trace obstruction

Date: 2026-07-29

Status: theorem plus sharply scoped counterexample.  The note gives the
necessary-and-sufficient `k=15` collision criterion for a safe one-rung
corner.  It also constructs a literal cyclically bi-resident
\(C_{16}\subset J(15,8)\) in which both orientations of one colour-aware square
are collar-unsafe.  The cut upper colours of that `C_16` are unique; their
duplicate providers are only externally marked.  Thus the construction is
an abstract trace/square obstruction, not a q1-exact, upper-complete parent
Hamilton-factor counterexample.

## 1. Duplicate-safe catalogue and endpoint-age labels

Retain the notation of
`THREAD_A_K16_ONE_RUNG_SQUARE_COUNTING_AND_COLLAR_FORCING_20260729.md`.
Let \(\Gamma_F\) be the square graph, let \(\mathcal U\) be the parent edges whose upper
colour has load one, and let \(\mathcal D\) be the set of duplicate-safe oriented
one-rung corners.  Its exact size is

\[
 C_{\rm dup}=|{\cal D}|
 =C-2d_{\Gamma_F}({\cal U})+2e_{\Gamma_F}({\cal U}).
\tag{1.1}
\]

For a corner \(s\in{\cal D}\), the six-row normal form says that only
coordinates in \(L_s\setminus\{v_s\}\) can fail.  At each oriented
endpoint, at most one such coordinate has positive age one and at most one
has positive age two.  Denote these labels by

\[
 A_1(s),A_2(s),B_1(s),B_2(s),
\tag{1.2}
\]

using slot-specific null symbols when a label is absent.  Null symbols
never compare equal to each other or to a coordinate of `X`.

At `D=4`, the corner is unsafe exactly when at least one of

\[
 A_1=B_1,\qquad A_1=B_2,\qquad A_2=B_1
\tag{1.3}
\]

holds as an equality in `X`.

## 2. Exact inclusion--exclusion

For \((i,j)\in\{(1,1),(1,2),(2,1)\}\), put

\[
 E_{ij}=\{s\in{\cal D}:A_i(s)=B_j(s)\in X\},
 \qquad N_{ij}=|E_{ij}|,
\tag{2.1}
\]

and define the crossed-swap count

\[
 N_\times=|E_{12}\cap E_{21}|.
\tag{2.2}
\]

### Theorem 2.1 (exact collision kernel)

The number of safe oriented corners is exactly

\[
 \boxed{
 N_{\rm safe}
 =C_{\rm dup}-N_{11}-N_{12}-N_{21}+N_\times.}
\tag{2.3}
\]

Consequently a safe one-rung splice exists if and only if

\[
\boxed{
 C-2d_{\Gamma_F}({\cal U})+2e_{\Gamma_F}({\cal U})
 >N_{11}+N_{12}+N_{21}-N_\times.}
\tag{2.4}
\]

This is a radius-two necessary-and-sufficient criterion.

#### Proof

The two A-age labels are distinct whenever nonnull, as are the two B-age
labels.  Hence \(E_{11}\cap E_{12}=\varnothing\), since membership would
give \(B_1=B_2\), and \(E_{11}\cap E_{21}=\varnothing\), since membership
would give \(A_1=A_2\).  The only possible overlap is
\(E_{12}\cap E_{21}\); there the two collision labels are necessarily
distinct.  There is no triple overlap.  Inclusion--exclusion on (1.3)
therefore gives

\[
 |E_{11}\cup E_{12}\cup E_{21}|
 =N_{11}+N_{12}+N_{21}-N_\times.
\]

This union is exactly the unsafe catalogue.  Subtracting it from
\(C_{\rm dup}\), and then using (1.1), proves (2.3)--(2.4).  \(\square\)

Pointwise, if \(I_{ij}(s)\) is the indicator of \(E_{ij}\), then

\[
 {\bf1}_{\rm unsafe}(s)
 =I_{11}(s)+I_{12}(s)+I_{21}(s)-I_{12}(s)I_{21}(s).
\tag{2.5}
\]

This is the exact boundary-word/Hadamard collision kernel sought in the
one-rung lane.  For example,

\[
 N_{ij}=\sum_{s\in{\cal D}}\sum_{x\in X}
 {\bf1}_{A_i(s)=x}{\bf1}_{B_j(s)=x},
\tag{2.6}
\]

and

\[
 N_\times=
 \sum_{s\in{\cal D}}\sum_{\substack{x,y\in X\\x\ne y}}
 {\bf1}_{A_1(s)=x}{\bf1}_{B_2(s)=x}
 {\bf1}_{A_2(s)=y}{\bf1}_{B_1(s)=y}.
\tag{2.7}
\]

### Quantitative form

If, for some \(\eta>0\),

\[
 N_{11}+N_{12}+N_{21}-N_\times
 \le(1-\eta)C_{\rm dup},
\tag{2.8}
\]

then at least \(\eta C_{\rm dup}\) corners are safe.  The strict case
\(\eta>0\), with no prescribed value, is exactly (2.4).  Thus the weakest
additional condition needed beyond duplicate safety is the
**collision-noncover condition**

\[
 N_{11}+N_{12}+N_{21}-N_\times<C_{\rm dup}.
\tag{2.9}
\]

Any proposed universal parent-factor theorem must prove (2.9), or a
stronger structural condition implying it.

## 3. Relation to the Ferrers profile bound

For coordinate `x`, let `M_x` be the Ferrers bound from the preceding
note.  A fixed coordinate cannot witness two of the events in (1.3) at
one corner, because the A and B age labels are individually distinct.
Therefore

\[
 N_{11}+N_{12}+N_{21}\le\sum_xM_x.
\tag{3.1}
\]

Combining (2.3) with (3.1) gives the crossed-refund refinement

\[
 N_{\rm safe}
 \ge C_{\rm dup}+N_\times-\sum_xM_x.
\tag{3.2}
\]

Thus

\[
 \boxed{C_{\rm dup}+N_\times>\sum_xM_x}
\tag{3.3}
\]

is the sufficient statement obtained by substituting the coordinatewise
Ferrers bounds and retaining the one joint statistic \(N_\times\).  The simpler
condition

\[
 N_{11}+N_{12}+N_{21}<C_{\rm dup}
\tag{3.4}
\]

is sufficient but discards the crossed refund.

## 4. The smallest pure trace obstruction

Consider cyclic positions `0,...,7`, cuts

\[
 e=(0,1),\qquad f=(4,5),
\tag{4.1}
\]

and two coordinate traces

\[
 x=11110000,\qquad y=00001111.
\tag{4.2}
\]

For the first square orientation, retain position `0` as the A endpoint
and the complement of position `4` as the B endpoint.  Then

\[
 A_1=B_1=x.
\]

For the reciprocal orientation, retain position `4` as the A endpoint and
the complement of position `0` as the B endpoint.  Then

\[
 A_1=B_1=y.
\]

Both traces have every zero-run and one-run of length four, yet both
orientations of the sole square are unsafe.  Mark the two parent upper
colours as having external second providers; the square is then
duplicate-safe in the abstract palette ledger.

The length `8` is minimal for a nonconstant cyclic trace with one-runs and
zero-runs of length at least four.  Two witness coordinates are also
minimal for killing both reciprocal corners, because their dangerous
grounds \(L\setminus\{v\}\) and \(K\setminus\{u\}\) are disjoint.

This is the smallest trace relaxation.  It does not impose constant rank,
Johnson adjacency, or the other parent-factor palettes.

### Exact `k=15` marginal embedding

Q1 exactness would force, for each old coordinate, `429` positive and
`429` zero runs, `3432` present states, and `3003` absent states.  Reserve
the local four-one/four-zero block in (4.2).  The remaining `3428` present
states and `2999` absent states can respectively be divided among the
other `428` positive and zero runs, all with length at least four.  Hence
the exact one-coordinate `k=15` run counts and weights do not exclude the
bad cell.  This is still a coordinatewise trace embedding, not a
simultaneous fixed-rank Hamilton cycle.

## 5. A literal bi-resident Johnson obstruction in the `k=15` dimension

The preceding binary gadget can be made into a genuine simple Johnson
cycle on rank eight while retaining all-coordinate cyclic bi-residence.

Let positions be \(t\in{\mathbb Z}_{16}\).  Take the fifteen coordinates

\[
 x,y,a,u,v,p_0,q_0,\ldots,p_4,q_4.
\]

Put \((s_0,\ldots,s_4)=(0,1,4,5,6)\), and define the traces

\[
\begin{array}{c|l}
x&1\text{ on }3,4,\ldots,10,\\
y&1-x,\\
a&1\text{ on }\{0,1,2,3,8,9,10,11\},\\
u&1\text{ on }4,5,\ldots,15,\\
v&1\text{ on }\{0,\ldots,7,12,\ldots,15\},\\
p_i&1\text{ on the cyclic interval }\{s_i+1,\ldots,s_i+8\},\\
q_i&1-p_i.
\end{array}
\tag{5.1}
\]

Let \(V_t\) be the set of coordinates whose trace is one at time `t`.

### Proposition 5.1

The sequence \((V_0,\ldots,V_{15})\) is a simple `C_16` in `J(15,8)`.
Every cyclic zero-run and one-run of every coordinate has length at least
four.  The edges

\[
 e=V_3V_4,\qquad f=V_{11}V_{12}
\tag{5.2}
\]

form an exact colour-aware square, and both reciprocal one-rung corners
are collar-unsafe.

#### Proof: rank and Johnson adjacency

At every `t`, exactly one of `x,y`, exactly two of `a,u,v`, and exactly one
of each `p_i,q_i` pair is present.  Thus

\[
 |V_t|=1+2+5=8.
\]

The base coordinates toggle on precisely the following edges:

\[
\begin{array}{c|c}
2&y\longrightarrow x,\\
3&a\longrightarrow u,\\
7&v\longrightarrow a,\\
10&x\longrightarrow y,\\
11&a\longrightarrow v,\\
15&u\longrightarrow a.
\end{array}
\tag{5.3}
\]

Pair `i` toggles on edges \(s_i,s_i+8\).  These ten edges are

\[
 0,1,4,5,6,8,9,12,13,14,
\]

the complement of (5.3).  Hence every cyclic transition deletes exactly
one coordinate and inserts exactly one coordinate.

#### Proof: simplicity

The five-bit `p`-signatures of \(V_0,\ldots,V_{15}\) are

\[
\begin{array}{c|cccccccccccccccc}
t&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\ \hline
p&00000&10000&11000&11000&11000&11100&11110&11111&
11111&01111&00111&00111&00111&00011&00001&00000.
\end{array}
\tag{5.4}
\]

Only the clusters \(\{0,15\},\{2,3,4\},\{7,8\},\{10,11,12\}\) repeat a
signature.  Within them the base traces differ, respectively, through
`u/a`, through `y/x` and then `a/u`, through `v/a`, and through `x/y` and
then `a/v`.  Thus all sixteen states are distinct.

#### Proof: bi-residence

Coordinates `x,y` have one run of each bit of length eight.  Coordinate
`a` has two one-runs and two zero-runs, all of length four.  Coordinate `u`
has run lengths `12` and `4`, as does `v`.  Every `p_i,q_i` has run lengths
`8` and `8`.  Thus the cyclic bi-residence threshold is four.

#### Proof: square and two failures

From (5.1),

\[
\begin{aligned}
 L&=\{x,v,p_0,p_1,q_2,q_3,q_4\},\\
 K&=\{y,u,q_0,q_1,p_2,p_3,p_4\}.
\end{aligned}
\tag{5.5}
\]

These sets are disjoint and

\[
 X=L\mathbin{\dot\cup}K\mathbin{\dot\cup}\{a\},
\]

while

\[
 V_3=L+a,\quad V_4=L+u,\quad
 V_{11}=K+a,\quad V_{12}=K+v.
\tag{5.6}
\]

This is exactly the square normal form.  For the `L`-corner, the A path
toward \(V_3\) has predecessor \(V_2\), and

\[
 (x(V_2),x(V_3))=(0,1).
\]

The complementary B path away from the copy of \(V_{11}\) follows the
underlying states \(V_{11},V_{10},\ldots\), and

\[
 (x(V_{11}),x(V_{10}))=(0,1).
\]

Thus \(A_1=B_1=x\).  Reciprocally, the A path toward \(V_{11}\) has
predecessor \(V_{10}\), and the complementary B path away from the copy of
\(V_3\) follows \(V_3,V_2,\ldots\).  Since

\[
 (y(V_{10}),y(V_{11}))=(0,1)
 =(y(V_3),y(V_2)),
\]

the opposite corner has \(A_1=B_1=y\).  Both seam runs have length two,
below four.  \(\square\)

### Duplicate-provider caveat

Inside this actual `C_16`, the upper colours of `e` and `f` each have load
one: the only cycle vertices contained in their respective upper sets are
the displayed edge endpoints.  To obtain the abstract duplicate-safe
square system, attach one formal external provider for each colour.  No
embedding of those providers into one q1-exact, upper-complete Hamilton
factor is proved here.

## 6. Minimality of the literal trace length

### Proposition 6.1

Every cyclic constant-rank Johnson square system in which all coordinates
are `D`-bi-resident and which has an unsafe corner has length at least
\(4D\).  The cycle in Proposition 5.1 attains this bound at \(D=4\).

#### Proof

Use the normal form and orient the carrier cycle.  Both selected square
endpoints contain the distinguished coordinate `a`, while their other cut
endpoints omit it.  If the two `a`-transitions have the same sign, `a` has
at least two positive and two zero runs.  Their four lengths are at least
`D`, giving length at least \(4D\).

Suppose instead that the signs are opposite.  Unless `a` already has two
runs of each sign, `a` has one positive run.  After deleting `e,f`, let
`I` be the unique path component from the selected endpoint
\(S=K+a\) of `f` to the selected endpoint \(P=L+a\) of `e` on which `a`
is present.  Both noncut endpoint directions lie in `I`, and \(|I|\ge D\).
Let `x` witness the unsafe corner, with endpoint ages
\(\alpha,\beta\) and \(\alpha+\beta\le D-1\).  Complementing the B rail
changes the bit but not the underlying noncut adjacency.  Thus `alpha` is
the terminal underlying `x=1` block at `P` in `I`, while `beta` is the
terminal underlying `x=0` block at `S` in that same path.  Since these
blocks do not cover `I`, the trace on `I` contains

\[
 0\cdots1\cdots0\cdots1.
\]

Coordinate `x` is constant one across `e` and constant zero across `f`, so
the complementary arc supplies the further transition joining the final
one block to the initial zero block.  Cyclically, `x` therefore has at
least two positive and two zero runs, all of length at least `D`.  Again
the total length is at least \(4D\).  \(\square\)

This is trace-length minimality only.  It does not assert dimension
minimality, q1 exactness, upper completeness, or embedded duplicate
providers.

## 7. Exact proved boundary

The full universal statement

> every q1-exact, upper-complete, cyclically bi-resident parent Hamilton
> cycle having a duplicate-safe square has a safe square

is neither proved nor refuted here.  No such parent PASS was available,
and the external duplicate providers in Section 5 are not a physical
factor completion.

What is proved is sharper at the surviving interface:

1. local Johnson geometry, cyclic bi-residence, reciprocal-square symmetry,
   and duplicate-provider flags do not imply collar safety;
2. the exact missing global condition is the collision-noncover inequality
   (2.9); and
3. any sufficient global parent-factor theorem must create a strict deficit
   in that collision cover, for example the quantitative decorrelation
   (2.8).
