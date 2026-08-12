# Boundary occurrence transposition repairs residence but needs two remote complementary-sector paths

Date: 2026-08-01  
Lane: AD, shared-bank residence refresh  
Status: exact local actuator, exact owner/q1 exchange ledger, exact local
complementary-sector no-go, and a superlinear lower bound for bounded outer
permutations.  A remote two-path sector exchange remains conditional.

**Quantifier correction.**  The remote-mate requirement below is for
preserving the old named chronology in situ.  If the global factor may be
selected around the refreshed paths, no inverse mate is required: the new
paths form a valid protected diamond bank.  The positive theorem and its
exact counts are in
`MATH_THEOREM_AD_REFRESHED_A_SECTOR_PROTECTED_DIAMOND_BANK_AND_ACCUMULATION_GATE_20260801.md`.

## 0. Verdict

At the first shared-bank residence expiry, the boundary occurrence should
not be overwritten one-way.  The rank-safe local operation is to transpose
the oldest and newest jump labels in each outer bank.  This operation:

1. removes every packet-internal signed-residence defect;
2. preserves source length, every owner rank, Johnson chronology, packet
   endpoints, and native lower/upper `q1` legality;
3. changes exactly `2b` owners, `2b` lower-`q1` colours, and `2b`
   upper-`q1` colours when the disjoint-base depth is `b`; and
4. turns one `b`-owner `X`-sector path and one `b`-owner `Y`-sector path
   into two `A=11`-sector paths.

The complete four-sector owner deck contains both `A`-sector mate paths
setwise.  The split packet does not contain them: it has only its two fixed
`A`-sector endpoint owners.  Therefore four-sector set coverage is not a
physical closure theorem.  Exact owner preservation requires two remote
contiguous mate paths.  If all four exchanged blocks are internal and
pairwise nonadjacent, chronology has eight boundary incidences; endpoint or
adjacent blocks have the corresponding smaller boundary ledger.

Moreover, repeated bounded outer-bank transpositions cannot maintain
residence forever.  The required number of moved labels through horizon `T`
is superlinear for fixed base depth.  Thus the suggested one-pair/every-two-
jumps schedule is false.

## 1. Repeated-bank notation and the rank-safe refresh

Start from pairwise-disjoint banks at depth `b>=2`.  After `t` deadline
jumps the current depth is

\[
                              h=b+t.                    \tag{1.1}
\]

The first expiry is `t=b+1`, hence `h=2b+1`.  Write

\[
                         a=\alpha_{b+1},\qquad
                         g=\gamma_{b+1}                \tag{1.2}
\]

for the newest jump pair.  The relevant outer-bank orders are

\[
\begin{aligned}
 D^+&=(\bar D^+,\alpha_1,\alpha_2,\ldots,\alpha_b,a),\\
 D^-&=(g,\gamma_b,\ldots,\gamma_2,\gamma_1,\bar D^-).
\end{aligned}                                          \tag{1.3}
\]

The boundary refresh is the pair of transpositions

\[
\begin{aligned}
 \widetilde D^+
   &=(\bar D^+,a,\alpha_2,\ldots,\alpha_b,\alpha_1),\\
 \widetilde D^-
   &=(\gamma_1,\gamma_b,\ldots,\gamma_2,g,\bar D^-).
\end{aligned}                                          \tag{1.4}
\]

A one-way replacement by `a` or `g` is not rank-safe: the donor label
already has its other outer occurrence, and the last/first depth window
would lose one distinct coordinate.  The transpositions (1.4) preserve the
set of bank labels in every window containing both endpoints and preserve
rank in the intermediate windows by an exact old/new exchange.

More generally, for an `alpha` label with central `Lambda` index `ell` and
outer `D^+` index `p`, its complete packet trace is

\[
 \operatorname{tr}(\alpha)
   =0^{\ell-1}1^{h+1}0^{h+1+p-\ell}1^{h-p}.           \tag{1.5}
\]

It is resident exactly when `p>=ell`.  This scalar inequality will also
drive the rolling no-go.

## 2. Exact residence repair and lifetime

Immediately after (1.4), the four affected traces are

\[
\begin{aligned}
 \operatorname{tr}(\alpha_1)&=0^b1^{h+1}0^{3b+1}1,\\
 \operatorname{tr}(a)&=1^{h+1}0^{3b+1}1^{b+1},\\
 \operatorname{tr}(\gamma_1)&=10^{3b+1}1^{h+1}0^b,\\
 \operatorname{tr}(g)&=1^{b+1}0^{3b+1}1^{h+1}.
\end{aligned}                                          \tag{2.1}
\]

Since `3b+1>=2b+2=h+1`, every internal zero-run is legal.  The short
positive runs meet a packet endpoint.  The left one is the global prefix;
the right one is a clipped packet run and must be continued by the already
exported exterior boundary state.

After `q` further jumps without another outer-bank move, put

\[
                            h_q=2b+1+q.                 \tag{2.2}
\]

The complete traces become

\[
\begin{aligned}
 \operatorname{tr}(\alpha_1)
   &=0^{b+q}1^{h_q+1}0^{3b+1}1^{q+1},\\
 \operatorname{tr}(a)
   &=0^q1^{h_q+1}0^{3b+1}1^{b+q+1},\\
 \operatorname{tr}(\gamma_1)
   &=1^{q+1}0^{3b+1}1^{h_q+1}0^{b+q},\\
 \operatorname{tr}(g)
   &=1^{b+q+1}0^{3b+1}1^{h_q+1}0^q.
\end{aligned}                                          \tag{2.3}
\]

Hence these four refreshed old/donor labels remain resident exactly for

\[
                              0\le q\le b-1.            \tag{2.4}
\]

They all expire simultaneously at `q=b`.  This is not the lifetime of the
whole packet: unrefreshed older pairs can expire earlier (for example the
second pair already reaches its next deadline at `q=2`).

## 3. Exact owner and `q1` delta

Use the standard packet owners

\[
\begin{aligned}
 L_u&=B^-\cup\Lambda[1,u+1]\cup D^-[u+1,h-1],\\
 R_u&=B^+\cup P[u+1,h]\cup D^+[1,u].                 \tag{3.1}
\end{aligned}

Let

\[
              \tau_L=(\gamma_1\ g),\qquad
              \tau_R=(\alpha_1\ a).                 \tag{3.2}
\]

Then (1.4) changes precisely

\[
 \mathcal B_L=(L_1,\ldots,L_b),\qquad
 \mathcal B_R=(R_b,\ldots,R_{h-2}),                  \tag{3.3}
\]

by applying `tau_L` and `tau_R`, respectively.  The four neighbouring
owners `L_0,L_(b+1),R_(b-1),R_(h-1)` are unchanged.  Consequently the new
row is still a simple Johnson path with the same two packet endpoints.

In the free abelian group on owner values, the exact signed delta is

\[
 \Delta\mathcal O=
   \sum_{u=1}^{b}([\tau_L L_u]-[L_u])
  +\sum_{u=b}^{h-2}([\tau_R R_u]-[R_u]).              \tag{3.4}
\]

All `2b` negative and all `2b` positive atoms are distinct.

For adjacent owners put

\[
 I^L_u=L_u\cap L_{u+1},\quad J^L_u=L_u\cup L_{u+1},
 \qquad
 I^R_u=R_u\cap R_{u+1},\quad J^R_u=R_u\cup R_{u+1}.
\]

The exact internal lower- and upper-`q1` deltas are

\[
\begin{aligned}
 \Delta\mathcal I={}&
   \sum_{u=0}^{b-1}([\tau_L I^L_u]-[I^L_u])
  +\sum_{u=b}^{h-2}([\tau_R I^R_u]-[I^R_u]),\\
 \Delta\mathcal J={}&
   \sum_{u=1}^{b}([\tau_L J^L_u]-[J^L_u])
  +\sum_{u=b-1}^{h-3}([\tau_R J^R_u]-[J^R_u]).       \tag{3.5}
\end{aligned}
\]

Again every row has exactly `2b` distinct negative and `2b` distinct
positive atoms.  These are literal native cells: (1.4) is a source-letter
permutation, so all shared intersection cells and spanning union cells
change exactly with the displayed owner path.  The one outgoing edge from
the packet into the exterior is not included in (3.5); it remains one
exported socket row.

## 4. Why the local four-sector packet does not close

With respect to the newest tags `(a,g)`, every owner of `\mathcal B_L` is in
sector `X=10`, and every owner of `\mathcal B_R` is in sector `Y=01`.
After (1.4), both blocks lie in sector `A=11`.

Define their old-coordinate cores by

\[
 C^-_u=L_u-\{a,\gamma_1\}\quad(1\le u\le b),
 \qquad
 C^+_u=R_u-\{g,\alpha_1\}\quad(b\le u\le h-2).       \tag{4.1}
\]

The added owners are precisely

\[
 C^-_u+\{a,g\},\qquad C^+_u+\{a,g\}.                 \tag{4.2}
\]

Each family is a simple `b`-vertex Johnson path.  Because the child owner
deck contains the complete `A` sector, all owners in (4.2) exist elsewhere
setwise.  But none occurs in the original split packet.  Indeed every
`C^-_u+{a,g}` contains `q^-`, so any packet occurrence would have to be an
`L` owner; the strict `Lambda/D^-` cutoff signature forces the same index,
where the owner is still in sector `X`.  The `q^+` argument is identical for
the second path.  The packet's only `A`-sector owners are its two fixed
sector endpoints.

Thus the local move produces `2b` duplicates and omits the `2b` owners in
(3.3) when viewed inside the complete child chronology.  A whole-sector
owner permutation must also locate the two mate paths (4.2) as remote,
contiguous chronology blocks and apply the inverse transpositions there.
This touches at least `4b` owner occurrences.

If those remote blocks exist, all internal owner and `q1` deltas cancel
under the two involutions.  If the four blocks are internal and pairwise
nonadjacent, their ends create eight external boundary edges.  Exact
owner/q1 closure is then equivalent to the first three conditions below;
endpoint or adjacent blocks use the same statement on their distinct
boundary incidences:

1. Johnson legality at every distinct new boundary incidence;
2. equality of the boundary lower-intersection multisets before and after;
3. equality of the boundary upper-union multisets before and after; and
4. for full compiler closure, additionally, literal source fragments and
   one common cap for both remote paths.

The raw four-sector owner partition proves only the setwise part (4.2).
The direct factor contains the remote internal `A` edges only when its
cap-two `K` factor contains every prescribed consecutive incidence pair;
it does not force that condition, contiguity, or the required sockets.

This is the minimal local no-go: the residence actuator is valid, but the
needed complementary-sector permutation is not contained in the protected
packet.

## 5. No bounded outer-permutation refresh schedule

At jump `t`, let `p_i(t)` be the `D^+` position assigned to `alpha_i`.
The available positions are

\[
                         b,b+1,\ldots,b+t-1,           \tag{5.1}
\]

while the central index is

\[
                         \ell_i(t)=t-i+1.              \tag{5.2}
\]

Equation (1.5) gives the exact residence criterion

\[
                              p_i(t)\ge\ell_i(t).       \tag{5.3}
\]

If label `i` is moved at time `s`, even the largest position gives slack

\[
 (b+s-1)-(s-i+1)=b+i-2.                               \tag{5.4}
\]

Every subsequent jump consumes one slack unit.  Thus label `i` must move at
least once in every `b+i-1` later jumps.  By horizon `T`, the number `M(T)`
of moved-label events satisfies

\[
 M(T)\ge
 \sum_{i=1}^{\lfloor T/2\rfloor}
 \left(\frac{T}{2(b+i-1)}-1\right)_+.                 \tag{5.5}
\]

For fixed `b` and `T/b->infinity`, this is

\[
                         M(T)=\Omega(T\log(T/b)).       \tag{5.6}
\]

A bounded number of pair transpositions per jump moves only `O(T)` labels,
contradicting (5.6).  The gamma bank is symmetric.  Hence no periodic
bounded-support outer-bank permutation maintains the shared-bank state
indefinitely.

The smallest failure already occurs at `b=2`.  Refresh at `t=3`; at `t=5`
the three alpha traces are

\[
 0^4 1^8 0^7 1^3,qquad
 0^3 1^8 0^7 1^4,qquad
 0^2 1^8 0^7 1^5.                                    \tag{5.7}
\]

All three have the illegal internal gap `0^7` against threshold `8`, while
one pair transposition can move at most two labels.

The lower bound applies to refreshes which retain both occurrences of every
jump label and only permute outer-bank positions.  A remote `A`-sector
exchange can instead retire an occurrence and is outside this no-go; it
must satisfy the socket/source conditions of Section 4.

## 6. Audit and exact boundary

The dependency-free symbolic replay

```text
scratch/audit_ad_shared_bank_boundary_sector_refresh_20260801.py
```

checks the first-expiry refresh for every `2<=b<=12`.  It verifies complete
signed traces, zero post-refresh residence defects, final/pre-row source
factorization, owner rank and Johnson legality, native lower cells, both
injective local `q1` palettes, unchanged packet endpoints, absence of local
mate owners, and the exact `2b` owner/lower/upper signed deltas.

Its expected status is

```text
PASS_LOCAL_REFRESH_WITH_EXACT_OWNER_Q1_EXCHANGE_NOGO
```

The proved boundary is therefore:

- **proved:** one boundary pair transposition repairs the first local
  residence expiry exactly;
- **proved:** it cannot close owner/q1 inside the split packet and has
  growing support `4b` even with ideal remote mates;
- **proved:** bounded-rate outer-bank permutations cannot give an unbounded
  recurrence;
- **open:** a nonlocal two-path `A`-sector socket exchange preserving all
  distinct boundary palettes (eight in the generic internal/nonadjacent
  case), literal source chronology, deeper shadows, and one common cap.
