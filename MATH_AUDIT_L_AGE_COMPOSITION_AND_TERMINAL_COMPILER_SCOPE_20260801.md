# Independent audit: age-composition circulation versus occurrence-labelled terminal compilation

Date: 2026-08-01  
Lane: L independent audit  
Status: PASS for the symmetric unrooted fractional quotient after two
explicit proof repairs; NOT a rooted, integral, occurrence-address, or
common-cap theorem

## 0. Audited artifacts and verdict

The supplied reduction is

* `/Users/amir.nuriyev/.codex/attachments/bba291cc-29ed-4220-b1a6-562410486402/pasted-text.txt`,
  SHA-256
  `fc612beef74434c4d901fd01f7a04c2b9fc2725d9194fcafe6d3753085412419`.

It is compared with

* `MATH_THEOREM_TRIANGULAR_MARKED_TRACE_CIRCULATION_AND_K6_BALANCED_CLOCK_20260801.md`,
  SHA-256
  `227295e9a985f8d7e86cec3153c5226013557f3af73b04e12ff3865514f898cd`;
* `MATH_THEOREM_L_PINNED_TRIANGULAR_ROOTED_TRACE_AND_PRIVATE_COMMONCAP_20260801.md`,
  SHA-256
  `bc15e1681dd31306a83640d6269109d6413d588535bd701c0782459c12e8ce7c`.

The main verdict is:

\[
 \boxed{
 \text{The age-composition theorem is exact for }
 \mathsf{ST}_{k,r,d},
 \text{ the unrooted }\operatorname{Sym}(k)\text{-invariant fractional
 projection.}}                                             \tag{0.1}
\]

Two short coupling steps are missing from its written proof and are supplied
below.  The quotient does **not** include a fixed boundary prefix, literal
support connectivity, one trace per owner, named target exact cover,
representative suffix addresses, or maximal common-cap feasibility.

In particular, the answer to the compiler question is:

* `R(c)` counted once is the correct **distinct target-colour capacity** of
  one trace type in `ST`;
* it is not the complete occurrence-labelled cell capacity, because equal
  suffix values at different widths remain different physical addresses;
* rank-only marking loses no extra fractional target-Hall constraint after
  full symmetry averaging, but it loses the integral coloured Hall,
  root/topology, and common-cap constraints.

## 1. Literal age transitions

For a literal trace ending at time `t`, let

\[
 T=C_0\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_d,
 \qquad c_i=|C_i|,                                    \tag{1.1}
\]

where `C_i` consists of the coordinates whose most recent occurrence is at
time `t-i`.  Then `c_0>0` and `sum_i c_i=r`.

### Proposition 1.1 (the type edge relation is exact)

Successive trace types satisfy

\[
                         c'_{i+1}\leq c_i
                         \qquad(0\leq i<d).           \tag{1.2}
\]

Conversely, every pair of types satisfying (1.2) has a literal same-owner
transition.

#### Check

Every coordinate of new age `i+1` had old age `i`, proving necessity.  For
sufficiency, choose disjoint survivor subsets

\[
                         C'_{i+1}\subseteq C_i,
                         \qquad |C'_{i+1}|=c'_{i+1},  \tag{1.3}
\]

and put

\[
 C'_0=C_d\cup\bigcup_{i=0}^{d-1}(C_i\setminus C'_{i+1}). \tag{1.4}
\]

The size of (1.4) is `c'_0`; it is nonempty; and appending it refreshes
exactly its members while the survivors age by one.  This proves the
claimed transition without changing `T`.

## 2. First proof repair: a literal circulation needs a stationary coupling

A balanced de Bruijn **edge measure** does not canonically specify which
outgoing edge follows which incoming edge.  Therefore the sentence
"project each literal edge to a type edge" is incomplete.

Let `x_e` be a balanced literal edge measure.  At every order-`d` state `v`,
the incoming and outgoing edge masses have equal total.  Choose any
transportation coupling

\[
 g_v(e^-,e^+)\geq0                                   \tag{2.1}
\]

with those incoming and outgoing marginals.  Equivalently, decompose the
rational measure into directed cycles.  Consecutive trace edges in (2.1)
have age types `c,c'` satisfying (1.2).  Project `g`, sum equal type pairs,
and normalize by the total owner mass `W`.  The resulting `f(c,c')` is a
type circulation and its stationary mass `pi(c)` sums to one.

This supplies the missing necessity step.

## 3. Second proof repair: lift through labelled age partitions, then push to literal words

Fix an owner `T`, and let `P_c(T)` be the set of labelled age partitions of
`T` having type `c`.  For an allowed type edge `c->c'`, join partitions by
the survivor rule (1.3).  The relation is invariant under `Sym(T)`, which is
transitive on each `P_c(T)`.  Hence the bipartite relation is biregular.

Distribute `f(c,c')` uniformly over these labelled transition edges.  Every
partition of type `c` then has total incoming and outgoing mass

\[
                         {\pi(c)\over |P_c(T)|}.       \tag{3.1}
\]

Decompose this labelled partition flow into directed cycles.  Along each
cycle append the next zero-age class `C'_0`.  It is nonempty, and the age
recurrence proves that the resulting periodic letter sequence induces the
declared labelled partitions.  Push its consecutive length-`d+1` windows
to the literal de Bruijn graph.  This gives a balanced literal trace
measure of owner `T`.  Repeat for every owner and average under `Sym(k)`.

This is the missing sufficiency step.  Merely calling the partition flow a
literal state flow would skip the pushforward argument.

## 4. Why `R(c)` is counted once

For type `c`, put

\[
 s_j(c)=c_0+\cdots+c_{j-1},
 \qquad
 J_s(c)=\{j\in[d]:s_j(c)=s<r\}.                       \tag{4.1}
\]

The suffix set at width `j` is literally

\[
                         S_j=C_0\cup\cdots\cup C_{j-1}. \tag{4.2}
\]

These suffixes are nested.  Therefore

\[
                 |S_j|=|S_{j'}|\quad\Longleftrightarrow\quad
                 S_j=S_{j'}.                          \tag{4.3}
\]

The marked atoms defining `ST` require their marked suffix **sets** to be
distinct.  Thus the rank-`s` target-colour capacity of one trace is exactly

\[
       \min(1,|J_s(c)|)=\mathbf1_{s\in R(c)},
       \qquad R(c)=\{s_j(c):s_j(c)<r\}.               \tag{4.4}
\]

Counting a repeated equal suffix once is therefore correct for target
coverage.  Counting it with multiplicity would falsely use the same target
twice.

However, the literal interval cells at the widths in `J_s(c)` are distinct.
They can have different starts, deadlines, overlap conflicts, and cap
guards.  Integral compilation must choose a representative

\[
                         j\in J_s(c).                  \tag{4.5}
\]

The set `R(c)` forgets this choice.  It is therefore a distinct-colour
capacity, not a complete occurrence-ticket catalogue.

## 5. No hidden fractional target Hall row inside invariant `ST`

Suppose a type circulation has stationary distribution `pi`.  For every
rank `s`, choose masses

\[
 0\leq m_{c,s}\leq\pi(c),
 \qquad m_{c,s}=0\text{ if }s\notin R(c),
 \qquad \sum_c m_{c,s}=q_s.                            \tag{5.1}
\]

The coordinatewise inequalities in the supplied theorem are exactly the
condition for (5.1).  Different ranks may be marked independently because
one atom may mark any subset of its distinct nested suffixes.

Uniform labelled age partitions make the rank-`s` suffix a uniform
`s`-subset of a fixed owner.  Hence a fixed global target `S` receives

\[
 \binom{k-s}{r-s}{q_s\over\binom rs}
   ={Wq_s\over\binom ks}
   =1-{b_s\over\binom ks}.                            \tag{5.2}
\]

This is the exact right side of the symmetric marked-trace LP.  Thus no
additional fractional palette-Hall inequality is lost by passing from
literal targets to rank marginals **inside the fully invariant polytope**.

The systematic residue decomposition in the supplied text is also correct
conditional on the stated monotonicity of
`n_t=binom(k,r-t)-b_(r-t)`: its residue counts, row-size bound, and unit-drop
inequality follow from interval counting and concavity.  Since `b_s<=d`
while every adjacent binomial gap in the relevant half grows faster than
`d`, that monotonicity holds for all sufficiently large `k`.

The subsequent exact Strassen reduction in
`MATH_THEOREM_AGE_COMPOSITION_STRASSEN_CIRCULATION_CUTS_20260801.md`
eliminates the variables `f`: a type law `pi` is circulable exactly when

\[
        Q_*\pi\preceq_{\rm st}P_*\pi,
        \qquad
        P(c)=(c_0,\ldots,c_{d-1}),\quad
        Q(c)=(c_1,\ldots,c_d).                        \tag{5.3}
\]

This independently confirms that a stationary coupling, not merely type
marginals, is the load-bearing step in Sections 2--3.  It also shows that
the one-row unit-drop law is insufficient: at `d=2,r>=4`, the fully marked
gap profile `(2,1)` fixes `c=(r-3,1,2)` and violates the upward-set cut
`{x:x_2>=2}`.  The systematic family may still admit a global monotone
coupling, but that remains open.

## 6. A fixed boundary prefix restores named, not averaged, targets

The `Sym(k)` average chooses the singleton boundary prefix fractionally.
Once one literal prefix `rho` is fixed, it covers a concrete target bank
`B(rho)`.  The residual right side is

\[
 \mathbf1_{S\notin B(\rho)},                           \tag{6.1}
\]

not the averaged number `1-b_s/binom(k,s)`.

The age type also omits the ordered root state.  A fixed-owner lift can be
disconnected and need not meet the ordered-singleton boundary states at all.
Even connected type support does not imply connected literal support.

Accordingly, the phrase "the fractional serialization gate collapses" must
be scoped as follows:

> the **unrooted invariant marked-trace projection** collapses to the
> age-composition circulation; boundary rooting, connectedness, and
> one-copy compilation do not.

## 7. Exact remaining integral object

Fix a literal boundary prefix `rho`.  For every owner `T`, let `A_T(rho)`
be its literal marked trace atoms, now enhanced by a representative-width
choice (4.5) for every marked target.

An exact one-copy rounding must choose binary variables `x_a` satisfying

\[
             \sum_{a\in A_T(\rho)}x_a=1
             \qquad(T\in\tbinom{[k]}r),               \tag{7.1}
\]

and

\[
             \sum_{a:S\text{ is marked by }a}x_a
                =\mathbf1_{S\notin B(\rho)}
             \qquad(\varnothing\ne S,\ |S|<r).       \tag{7.2}
\]

If `z_e` is the selected literal edge multiplicity, there must also be at
most `C` bridge edges `b` such that

\[
 \operatorname{out}_{z+b}-\operatorname{in}_{z+b}
       =\mathbf1_\rho-\mathbf1_\tau                  \tag{7.3}
\]

for some terminal state `tau`, and the positive support must be weakly
connected.  Equations (7.1)--(7.3) are a coloured hypergraph exact cover
coupled to de Bruijn incidence and topology.  Clearing a denominator of the
fractional age flow repeats owners and does not solve them.

Finally, let `C(a,S)` be the physical suffix cell chosen by atom `a` for
target `S`, and let `Ebar_p` be the fixed carrier envelope.  For the selected
target-cell family `M`, its maximal common cap is

\[
 A_p(M)=\overline E_p\cap
       \bigcap_{(S,C)\in M:\ p\in C}S.                \tag{7.4}
\]

The rounding is physical only if every `A_p(M)` is nonempty and these caps
reproduce every protected owner/upper row and every selected lower cell.
Neither cardinalities `c_i`, ranks `s_j`, nor `R(c)` contain the membership
or overlap information in (7.4).

The authenticated guarded-common-cap `K_(2,2)` example already shows that
marginal Hall and chain alignment may pass while every integral assignment
kills a protected bit.  Thus a trace-guarded / laminar certificate or a
literal maximal-cap replay is an independent load-bearing theorem.

## 8. Independent audit of the Lane-L terminal theorem

The companion Lane-L theorem was checked separately at each interface.

1. Its ideal-pin extension follows from the uniform containment flow and
   the minimum owner degree `k-r+1`; it makes no chainization claim.
2. Its fixed-clock formula is exactly residual Hall after contracting the
   forced partial matching.
3. Its rooted trace-Euler formula counts all `W+C` full windows of a word
   and is exact for the declared flat trace subclass because the definition
   explicitly requires the prescribed root to lie in the connected support.
   The explicit `Init(D)` condition is necessary.
4. Its Ferrers term counts exactly the used basis cells removed by retiming;
   the first-used-index bound follows from rowwise cell injectivity.
5. Its antitone loss is Lipschitz in the number of unavailable private rail
   cells.  The canonical rays have zero baseline defect.
6. The common-cap conclusion correctly requires one complete guard system
   or exact private full-block transport.  Without that hypothesis, one
   spanning `{a}` pin erases arbitrarily many private bits, so bounded pin
   count alone is insufficient.

No symmetric-chain-decomposition assumption enters any of these arguments.

## 9. Final scope

The age quotient is genuine progress on the fractional clock question.  It
does not yet reduce the terminal compiler to a polynomial or rank-only
rounding.  The exact missing object is:

\[
\boxed{
\begin{array}{c}
\text{one literal prefix and its named boundary targets}\; +\\
\text{one marked trace per owner and exact named lower cover}\; +\\
\text{one rooted connected Euler trail with }O(1)\text{ bridges}\; +\\
\text{one occurrence-level maximal common cap preserving the protected
carrier.}
\end{array}}                                           \tag{9.1}
\]

This is precisely the pin-compatible guarded clocked Euler basis isolated
in the Lane-L theorem.  Proving it with bounded defect would give the stated
SCD-independent `B(k)+O(1)` route.
