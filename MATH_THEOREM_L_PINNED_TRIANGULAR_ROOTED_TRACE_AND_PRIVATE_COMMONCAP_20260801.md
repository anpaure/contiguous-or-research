# Pinned triangular chains serialize by a rooted trace Euler trail, and private Ferrers--birail packets have bounded common-cap defect

Date: 2026-08-01  
Lane: L, terminal lower compiler / chainization  
Status: exact ideal-pin, fixed-clock, rooted-serialization, and private
common-cap theorems; a conditional SCD-independent `B(k)+O(1)` route; no
unconditional integral Boolean chain factor or universal word is claimed

## 0. Outcome

Put

\[
 r=\left\lceil {k\over2}\right\rceil,
 \qquad W=\binom kr,
 \qquad
 \Lambda=\sum_{s=1}^{r-1}\binom ks,
\]

and let `d` be least with

\[
                 dW+\binom{d+1}{2}\geq\Lambda .       \tag{0.1}
\]

Thus the lower-bound length is `B(k)=W+d`.  The ideal owner-slot SDR,
endpoint-chain necessity, the attached antitone two-ray bank, and the
pivot-cycle pins live at four different levels.  They do not compose merely
by comparing their scalar capacities.

This note proves the following exact statements.

1. In the stronger `(d+1)`-slot ideal owner graph, every legal set of
   `O(d)` prescribed pivot/ray pins extends for all sufficiently large `k`.
   Thus fixed-packet robustness is not an ideal-Hall obstruction.
2. For a fixed clock, the effect of prescribed pins is one ordinary Hall
   deficiency, with an exact min--max formula.  Generic robustness loses
   `Theta(d)`; zero loss means that the clock and pins were selected jointly.
3. For the true triangular geometry, a static integral chain factor is not
   yet a physical object.  Its boundary chains must come from one common
   prefix.  Conditional on that prefix, the exact serialization overhead is
   a **rooted coloured trace-Euler** minimum.
4. Relative to one trace-guarded physical occurrence basis, Ferrers retiming,
   private pins, and the two antitone rays have an additive exact defect
   ledger.  In particular, insertion-born pivot/ray cells create zero
   common-cap matching loss.
5. These statements give an exact SCD-independent implication to
   `B(k)+O(1)`.  Its one compound missing input is a prefix-realizable,
   one-owner-per-trace, rooted Euler selection carrying a trace-guarded
   physical lower basis with bounded Ferrers loss.

The new age-composition quotient is compatible with this picture, but only
at the symmetric fractional level.  Its exact compiler scope is audited in
the companion note.

## 1. Robustness of the ideal `(d+1)`-slot SDR

Let

\[
       {\cal P}=\{S\subseteq[k]:1\leq |S|<r\},
       \qquad \rho={\Lambda\over W},
       \qquad q=d+1.                                  \tag{1.1}
\]

Give every rank-`r` owner `T` the labelled slots `(T,1),...,(T,q)`, and join
`S` to every slot of every owner containing `S`.

### Theorem 1.1 (arbitrary ideal pins extend)

Let `P` be any legal partial target-to-slot matching of size `p`.  It extends
to a matching saturating all of `\mathcal P` whenever

\[
        \boxed{
        p\leq(q-\rho)(k-r+1).}                         \tag{1.2}
\]

Moreover,

\[
 q-\rho=d+1-{\Lambda\over W}
       \geq 1-{\binom{d+1}{2}\over W}.                \tag{1.3}
\]

Consequently every fixed number of pivot/two-ray packets, using `O(d)`
ideal slots, is harmless in this graph for all sufficiently large `k`.

#### Proof

For every target `S`, distribute one unit uniformly over its containing
owners.  By owner symmetry, the total load at every owner is exactly
`rho`.  Hence every target family `F` obeys

\[
                         |F|\leq\rho|N_O(F)|.          \tag{1.4}
\]

Every nonempty `F` has at least `k-r+1` owner neighbours: this is the
minimum containment degree, attained at rank `r-1`.  The prescribed matching
removes at most `p` slots from the neighbour slots of `F`.  Therefore

\[
 \begin{aligned}
 |N_{\rm free}(F)|
   &\geq q|N_O(F)|-p\\
   &\geq \rho|N_O(F)|\\
   &\geq |F|,
 \end{aligned}                                        \tag{1.5}
\]

where the middle inequality follows from (1.2).  Hall extends `P`.
Finally, (0.1) gives
`Lambda/W<=d+binom(d+1,2)/W`, proving (1.3). \(\square\)

### Scope

The theorem is deliberately ideal.  It assigns targets to owner labels and
slot numbers.  It does not make the targets assigned to one owner nested,
does not satisfy the sliding endpoint cocycle, and does not produce a common
cap.  Thus it removes fixed-packet robustness from the ideal-SDR gate but
does not prove physical chainization.

## 2. Exact fixed-clock pin contraction

Fix a clock `tau:\mathcal P->[d]` and the exact triangular clock graph
`B_tau^triangle=(L,R;E)` of
`MATH_THEOREM_A_TRIANGULAR_CHAIN_EXCHANGE_CONTRACTION_AND_GLOBAL_RESERVOIR_20260801.md`.
Its right shore consists of later-time successor resources, owner resources,
and the `d` boundary terminals.  Suppose first that this graph has a
matching saturating `L`.

Let `P` now denote a legal partial matching of forced pivot/ray
successor/owner/terminal arcs.  Write `L(P),R(P)` for its used vertices and

\[
                 \sigma_\tau(X)=|N_\tau(X)|-|X|.      \tag{2.1}
\]

### Theorem 2.1 (pinned fixed-clock Hall formula)

The minimum number of new universal terminal resources needed to saturate
the residual left shore after forcing `P` is

\[
 \boxed{
 \begin{aligned}
 \delta_{\tau,P}
   &=\max_{X\subseteq L\setminus L(P)}
       \bigl(|X|-|N_\tau(X)\setminus R(P)|\bigr)_+\\
   &=\max_{X\subseteq L\setminus L(P)}
       \bigl(|N_\tau(X)\cap R(P)|-\sigma_\tau(X)\bigr)_+ .
 \end{aligned}}                                       \tag{2.2}
\]

In particular,

\[
                         \delta_{\tau,P}\leq |P|,     \tag{2.3}
\]

and `delta_(tau,P)=0` if and only if `P` is contained in a saturating
matching of `B_tau^triangle`.

#### Proof

The first line is the usual Hall deficiency of the residual graph.  Adding
`c` universal right vertices repairs precisely all cuts of deficiency at
most `c`, so its maximum is also the minimum required number.  Expanding
the deleted right shore gives the second line.  Since
`|N_tau(X) cap R(P)|<=|P|` and `sigma_tau(X)>=0` in the unpinned saturable
graph, (2.3) follows.  Zero deficiency is exactly residual saturability,
which is equivalent to extendibility of `P`. \(\square\)

Thus a packet with `Theta(d)` forced ideal arcs has only a `Theta(d)` generic
guarantee.  The prospective zero-defect rule is stronger and exact:
**choose the clock, its saturating matching, and the pivot/ray pins jointly.**

## 3. Prefix-realizable triangular factors

An integral triangular factor consists of

* one chain `C_T` of strict-lower targets below every rank-`r` owner `T`,
  with `|C_T|<=d`; and
* boundary chains `D_i`, `1<=i<=d`, with `|D_i|<=i`,

which together partition `\mathcal P`.

This static definition still omits one physical condition.

### Definition 3.1 (common-prefix fibre)

Let `Init(D)` be the set of `d`-letter states

\[
             u=(A_1,\ldots,A_d),\qquad A_i\ne\varnothing, \tag{3.1}
\]

such that, for every `i` and every `S in D_i`, there is a `j<=i` with

\[
                         S=A_j\cup A_{j+1}\cup\cdots\cup A_i. \tag{3.2}
\]

Call the triangular factor **prefix-realizable** when `Init(D)` is nonempty.

Separate nestedness of the `D_i` does not imply this.  At depth two, take

\[
 D_1=(\{3\}),\qquad D_2=(\{1\}\subset\{1,2\}).       \tag{3.3}
\]

The first chain forces `A_1={3}` and the singleton in the second forces
`A_2={1}`; their two-letter union is `{1,3}`, not `{1,2}`.  Thus
`Init(D)=emptyset`.

The common singleton-prefix construction in the exact fractional triangular
theorem proves this condition fractionally.  It is not inherited by an
arbitrary integral rounding of the triangular atoms.

## 4. Exact rooted trace-Euler serialization

For a chain `C_T` below owner `T`, let `Tr_d(T,C_T)` be the admissible
length-`d+1` trace fibre from
`MATH_THEOREM_BOUNDED_CHAIN_TRACE_EULER_SERIALIZATION_AND_SIDECAR_DISTANCE_20260801.md`.
Every element

\[
                         e=(B_0,\ldots,B_d)            \tag{4.1}
\]

is an edge of the order-`d` de Bruijn graph, has full union `T`, and has
every member of `C_T` among its proper suffix unions.

For an integral edge multiset `z` and a prescribed start state `u`, define
`chi_u(z)` to be the minimum size of a nonnegative integral bridge multiset
`b` such that

1. the positive support of `z+b` together with the prescribed vertex `u`
   is weakly connected (equivalently, `u` lies on the resulting nonempty
   Euler trail); and
2. for some terminal state `t`,

   \[
       \operatorname{out}_{z+b}-\operatorname{in}_{z+b}
                  =\mathbf1_u-\mathbf1_t.             \tag{4.2}
   \]

Set `chi_u(z)=infinity` if this is impossible.

### Theorem 4.1 (triangular rooted trace-Euler equivalence)

Fix an integral triangular factor `(C_T;D_1,...,D_d)`.  Within the flat
depth-`d` owner-trace subclass, its exact minimum physical serialization
overhead is

\[
 \boxed{
 \min_{u\in\operatorname{Init}(D)}
 \min_{e_T\in\operatorname{Tr}_d(T,C_T)\ (T\in\binom{[k]}r)}
       \chi_u\!\left(\sum_T e_T\right).}              \tag{4.3}
\]

Equivalently, the value in (4.3) is at most `C` if and only if there is a
word of length `W+d+C` whose first `d` letters realize all boundary chains
and whose later full windows contain one distinct trace for every owner
chain.

#### Proof

Suppose the word exists.  Its first `d` letters give a state
`u in Init(D)`.  It has exactly `W+C` length-`d+1` windows.  The `W`
owner-labelled windows give the selected traces `e_T`; the remaining `C`
windows are bridges.  Consecutive windows form one de Bruijn trail starting
at `u`, proving (4.2), connectedness, and `chi_u<=C`.

Conversely, take the rooted Euler trail of `sum_T e_T+b`.  Spell its initial
state `u`, then append the last letter of every traversed edge.  The prefix
realizes every `D_i`; each selected coloured edge occurs as a literal full
window and realizes `C_T`; and the total length is `d+W+|b|`. \(\square\)

This is the one-copy integral counterpart of the symmetric rational marked-
trace circulation.  Clearing a fractional denominator repeats every owner
colour and does not prove (4.3).

### Corollary 4.2 (sharp rooted distance to one Eulerian component)

If `z` is already Eulerian and its positive support is weakly connected,
then

\[
 \boxed{
 \chi_u(z)=\min_{v\in V(z)}\operatorname{dist}(u,v)
           =\min_{v\in V(z)}\bigl(d-\operatorname{ov}(u,v)\bigr).} \tag{4.4}
\]

Indeed, any rooted trail must first reach the support of `z`.  Conversely,
take a shortest path from `u` to a support state `v` and then traverse the
Euler circuit of `z` rooted at `v`.

Thus even unrooted serialization defect zero may cost exactly `d` after a
pivot prefix fixes the root.  A fixed pivot source should be contracted
first; its terminal `d`-state is the `u` in (4.3).

### Scope

Theorem 4.1 is exact for the declared flat owner-trace subclass.  It is not
a characterization of every near-optimal word: variable-length or nonflat
owner witnesses from the endpoint-chain theorem may fall outside this
model.

## 5. Fixed packets cannot replace global endpoint chains

Let `x_b` be the proper-suffix depth of the selected rank-`r` endpoint `b`
in a word of length `W+d+C`.  The architecture-independent endpoint theorem
gives, for fixed `C` and `eta>0`,

\[
 {1\over W}|\{b:x_b\leq(1-\eta)d\}|
 \leq {C+1\over\eta}\sqrt{8\over\pi}\,{1+o(1)\over\sqrt k}. \tag{5.1}
\]

### Corollary 5.1 (finite-packet rigidity)

Suppose `H` disjoint resident pivot packets occupy a set `J` of endpoint
windows.  Then

\[
 |\{b\notin J:x_b>(1-\eta)d\}|
 \geq W-O_{C,\eta}(W/\sqrt k)-|J|.                    \tag{5.2}
\]

For the shared-bank pivot cycles, `|J|<=H(3h+2)` at depth `h`; for fixed
`H` and `h=Theta(sqrt(k))`, the last term is negligible compared with `W`.

This is immediate from (5.1), but it has an important interpretation: a
constant packet bank may provide roots, rays, and pins; it cannot substitute
for the global physical chainization of almost all owner endpoints.

## 6. A private pinned Ferrers--birail common-cap theorem

Now fix one final carrier chronology, its protected rows, and one common-cap
state.  Let `M_0` be a trace-guarded physical target-to-cell matching which
covers all but `gamma` lower targets.

Index the lower cell bank by rows `ell` and time indices `i`.  For a vector
of tail starts `a=(a_ell)`, let

\[
                  D(a)=\{(i,\ell):i<a_\ell\}          \tag{6.1}
\]

be the deleted Ferrers ideal, and put

\[
        \kappa_{M_0}(a)=|\operatorname{cells}(M_0)\cap D(a)|. \tag{6.2}
\]

If `u_ell` is the first index used by `M_0` in row `ell`, then cell
injectivity gives

\[
           \kappa_{M_0}(a)
             \leq\sum_\ell(a_\ell-u_\ell)_+.          \tag{6.3}
\]

Let `Pi` be a forced matching of pin targets to cells.  Define the exact
background collision count

\[
 q_\Pi=
 |\{T\in\operatorname{dom}M_0\setminus T(\Pi):
                 M_0(T)\in\operatorname{cells}(\Pi)\}|. \tag{6.4}
\]

Then `q_Pi<=|Pi|`, and `q_Pi=0` when the pin cells are private from the
transported image of `M_0`.

Finally attach two ordered ray shores.  Let `q_L,q_R` be the numbers of
unavailable private cells on the two shores, and let `delta_0` be the
unrestricted birail deficiency before these deletions.

### Theorem 6.1 (private Ferrers--birail defect ledger)

Assume that

1. `M_0` lies in a trace-guarded candidate bank;
2. the forced pins and ray incidences are either members of the same
   complete guard system or arise by an exact full-block/monotone address
   refinement preserving literal OR and every guard; and
3. the background edges whose targets are reassigned to the packet are
   removed, after which all selected target labels and occurrence-labelled
   physical cells are pairwise distinct, and every packet cell is disjoint
   from every retained background cell.

Then one final common cap covers all but at most

\[
 \boxed{
 \Delta_{\rm terminal}
   \leq
   \gamma+\kappa_{M_0}(a)+q_\Pi+\delta_0+q_L+q_R}     \tag{6.5}
\]

lower targets.

For the canonical two-ray marginal

\[
                    \{0^{d-1},1,\ldots,d-1\}          \tag{6.6}
\]

on each shore, `delta_0=0`.  If the literal attached two-host packet is
private, its explicit diagonal is already a zero-defect ray matching, so
`q_L=q_R=0` as well.

#### Proof

Delete from `M_0` the `kappa_(M_0)(a)` edges whose cells lie in the Ferrers
ideal and the `q_Pi` remaining edges whose cells are consumed by pins.  The
unaffected edges are still an injective background matching.

Deleting `q_L` left rail cells lowers every left threshold-prefix count by
at most `q_L`.  Therefore the left overload parameter in the antitone
birail theorem increases by at most `q_L`; similarly the right overload
increases by at most `q_R`.  Its exact deficiency formula gives

\[
              \delta_{\rm ray}\leq\delta_0+q_L+q_R.   \tag{6.7}
\]

Take the union of the retained background, forced pins, and ray matching.
The occurrence hypotheses make it an ordinary matching.  The common guard
hypothesis makes every such matching maximal-cap exact.  Counting the
discarded or initially uncovered targets proves (6.5). \(\square\)

For residence starts `a=rho`, the checkable fixed-basis sufficient row is

\[
             \sum_\ell(\rho_\ell-u_\ell)_+=O(1).      \tag{6.8}
\]

The stronger `rho_ell<=u_ell` condition gives zero Ferrers loss.  The
shared-bank pivot and both rays are insertion-born outside the transported
old-cell image, so their `O(d)` named cells contribute `q_Pi=q_L=q_R=0`;
only the actual number of inserted source letters is charged to length.

### Why privacy / trace guards are necessary

One nonprivate pin can cause unbounded common-cap loss.  Take positions
`p_1,...,p_n` with envelopes and singleton-cell targets

\[
                         E_{p_i}=S_i=\{a,b_i\}.        \tag{6.9}
\]

The singleton matching is exact.  Force the one target `{a}` on the cell
spanning all positions.  The maximal cap at every `p_i` becomes `{a}`, so
all `n` targets `S_i` lose `b_i`.  Thus no `O(|Pi|)` common-cap theorem is
possible from pin count or marginal Hall alone.

## 7. Exact SCD-independent additive implication

The preceding pieces combine without any symmetric-chain-decomposition
basin.

### Theorem 7.1 (guarded rooted triangular implication)

Suppose that for a given `k` there exist:

1. a prefix-realizable integral triangular factor;
2. a root `u in Init(D)` and one trace `e_T in Tr_d(T,C_T)` per owner with
   rooted overhead `chi_u(sum_T e_T)<=c`;
3. a protected carrier on the spelled chronology whose nonlower masks have
   only `u_up` uncovered targets;
4. a trace-guarded lower occurrence basis and private packet transport,
   with the selected owner traces, boundary chains, and nonlower carrier
   rows included among the protected rows, satisfying Theorem 6.1 with
   defect `Delta_terminal`; and
5. a forced packet source/refinement with literal length charge `lambda_pin`
   (zero if already included in the prefix/traces).

Then

\[
 \boxed{
 \nu(k)\leq
 B(k)+c+\lambda_{\rm pin}+u_{\rm up}+\Delta_{\rm terminal}.} \tag{7.1}
\]

#### Proof

Theorem 4.1 gives the lower chronology in `W+d+c` letters.  The protected
carrier and Theorem 6.1 give all but the stated target defects in one common
cap, with the packet source charged exactly once.  Append each remaining
mask as one source letter.  Existing interval witnesses survive appending,
and every appended mask witnesses itself. \(\square\)

Hence uniform `O(1)` bounds on the four excess terms prove
`nu(k)<=B(k)+O(1)` independently of the SCD basin.

The one compound missing all-`k` theorem can now be stated without scalar
ambiguity.

> **Pin-compatible guarded clocked Euler basis.**  Construct, in the complete
> Boolean ideal, a prefix-realizable integral triangular factor and one
> owner-coloured rooted Euler trace selection whose physical target-cell
> matching is trace guarded and satisfies
> `gamma+sum_ell(rho_ell-u_ell)_+=O(1)`, while preserving the protected
> nonlower carrier with `O(1)` defect.

Ideal owner-slot Hall, fractional age marginals, abstract antitone pairing,
and a bounded number of pivot pins do not imply this theorem separately.

## 8. Exact relation to the age-composition quotient

The age-composition digraph gives an exact quotient of the
`Sym(k)`-invariant **fractional unrooted marked-trace circulation**.  Its
edge variables can be eliminated by the exact Strassen condition
`Q_*pi <=_st P_*pi`.  It
does not choose the root in `Init(D)`, one trace per owner, named residual
targets, a connected Euler trail, representative suffix widths, or a common
cap.  Therefore it attacks a genuine fractional subgate of Theorem 7.1 but
does not replace any of hypotheses 1--4.

The companion audit proves the precise statement and records the two small
proof repairs needed in the supplied reduction.

## 9. Frontier

The terminal lane is now separated into exact layers:

\[
\boxed{
\begin{array}{c}
\text{ideal owner slots + fixed pins}\quad\text{(robust)}\\
\Downarrow\\
\text{prefix-realizable integral triangular chains}\quad\text{(open)}\\
\Downarrow\\
\text{one-owner rooted trace-Euler selection with }O(1)\text{ bridges}
   \quad\text{(open)}\\
\Downarrow\\
\text{trace-guarded Ferrers/common-cap basis}\quad\text{(open in bulk)}\\
\Downarrow\\
\text{private antitone rays and pivot pins}\quad\text{(bounded defect)}.
\end{array}}
\]

The first genuinely global unresolved row is the correlated integral
chain/trace/guard selection.  The attached ray bank and pivot pins do not
add a new asymptotic compiler loss once that row is present.
