# Atomic reserve versus native C6 packets on the direct Catalan chain

Date: 2026-07-31  
Status: exact fixed-state Hall/packing/graphic census and minimal obstruction;
exact correlated-planting theorem in the declared native-packet class.  No
all-parameter recursion or `nu=B` conclusion is made.

## 0. Verdict

The literal reserve-to-packet rank is **not full** on any authenticated
direct-chain state.

The correct atomic reserve row is a literal atom

\[
                         e=(D,V;\xi_X,\xi_Y)\in M,              \tag{0.1}
\]

of one fixed-`Q` direct-side matching `M`.  Deleting `e` leaves its four
resources free.  A native suspended-C6 packet can repair this deletion only
when its complete three-atom OLD phase is already contained in `M` and `e`
is one of those three OLD atoms.

The authenticated stored states give the following exact ranks.

\[
\begin{array}{c|c|r|r|r|r|r|r}
n&\text{shore}&P&\#\mathcal P&\#\text{supported}&r_H&r_{\rm pack}&r_\Gamma\\\hline
3&U&6&0&0&0&0&0\\
3&L&6&0&0&0&0&0\\
4&U&28&2&6&2&2&2\\
4&L&28&1&3&1&1&1\\
5&U&120&11&31&11&10&9\\
5&L&120&9&24&9&6&6\\
6&U&495&55&139&55&40&40\\
6&L&495&66&177&66&52&52
\end{array}                                                     \tag{0.2}
\]

Here `r_H` is the ordinary target-to-packet matching rank, `r_pack` imposes
pairwise-disjoint OLD triples, and `r_Gamma` additionally requires the
simultaneous replacement to preserve the complete fixed-`Q` three-rail
forest.  Thus the all-target Hall/graphic deficiencies are

\[
\begin{array}{c|cc|cc}
n&\delta_H^U&\delta_H^L&\delta_\Gamma^U&\delta_\Gamma^L\\\hline
3&6&6&6&6\\
4&26&27&26&27\\
5&109&111&111&114\\
6&440&429&455&443.
\end{array}                                                     \tag{0.3}
\]

Every row has an isolated literal target.  Hence the minimal obstruction is
already the singleton Hall cut

\[
                              X=\{e\},\qquad N(X)=\varnothing.  \tag{0.4}
\]

For the stored `n=3` upper state one may take

\[
                         e=(0x07,0x1f;0x0f,0x17).               \tag{0.5}
\]

This is an actual four-resource leave, not an abstract closed-core deficit.

## 1. The canonical fixed-state system

Fix one fully serialized direct state

\[
                         \sigma=(F,Q,M^-,M^+,\Gamma_Q),         \tag{1.1}
\]

where `F` is the oriented parent Catalan forest, `Q` is the selected common
basis, `M^-` and `M^+` are the two strict direct representative matchings,
and `Gamma_Q` is their complete three-rail physical forest.  Complement the
lower side so that both shores have atom type

\[
                 \binom{[2n]}n\times\binom{[2n]}{n+2}
                    \times\binom{[2n]}{n+1}^{,2}.              \tag{1.2}
\]

At a physical owner of degree two, its two edge incidences are distinct
literal capacity slots.  The audit prints the owner mask for each incidence,
but does not conflate the two incidences.  Inside one suspended hex the six
owners are distinct.

For one shore `M`, let `P_sigma` contain every canonical suspended hex

\[
                             p=(O_p,N_p)                         \tag{1.3}
\]

whose full OLD phase `O_p` is a subset of `M`.  Canonical means the exact
`2n(n-2)` construction through a designated atom from the suspended-hex
theorem; deduplication is by the unordered pair `(O_p,N_p)`.  Literal replay
gives

\[
 |O_p|=|N_p|=3,qquad
 \operatorname{res}(O_p)=\operatorname{res}(N_p).               \tag{1.4}
\]

Each packet is recovered exactly three times by the generator, once for
each possible designation in `O_p`.

Make the bipartite incidence graph

\[
                     B_\sigma=(M,\mathcal P_\sigma;E),qquad
                     e\sim p\iff e\in O_p.                      \tag{1.5}
\]

For `A subseteq M`, define

\[
 r_H(A)=\nu(B_\sigma[A,\mathcal P_\sigma]).                    \tag{1.6}
\]

This is the ordinary Hall relaxation.  It forgets that two chosen packets
may use the same OLD atom.

Define the support-packing rank

\[
 r_{\rm pack}(A)=\max\{|S|:
  O_p\cap O_q=\varnothing\ (p\ne q),\quad O_p\cap A\ne\varnothing\}. \tag{1.7}
\]

Finally, `r_Gamma(A)` imposes in addition that

\[
          \left(M\setminus\bigcup_{p\in S}O_p\right)
             \cup\bigcup_{p\in S}N_p                           \tag{1.8}
\]

together with the untouched opposite shore and fixed central/seam bank is
again a maximum-degree-two forest.

The three ranks in (1.6)--(1.8) are distinct.  In particular, the word
“Rado” is legitimate for (1.6), or after a genuine packet matroid has been
proved.  It is not legitimate for the raw OLD-triple packing family.

## 2. Exact correlated-planting theorem

### Theorem 2.1 (fixed-body native-C6 completion)

Let `A subseteq M`.  In the resource-private native-C6 move class, the body
`M\A` has an exact C6 completion on the fixed-`Q` three-rail face if and only
if there are a packet family `S subseteq P_sigma` and a bijection

\[
                              \tau:S\longrightarrow A           \tag{2.1}
\]

such that

1. `tau(p) in O_p` for every `p`;
2. the OLD triples `O_p`, `p in S`, are pairwise disjoint; and
3. the simultaneous replacement (1.8) is `Gamma_Q`-legal.

#### Proof

If `tau(p)` is deleted, the other two members of `O_p` remain installed.
Replacing those two OFF atoms by `N_p` gains exactly the four resources of
`tau(p)` by (1.4).  Pairwise OLD disjointness makes these identities commute,
and item 3 is exactly the remaining physical guard.  This proves
sufficiency.

Conversely, every gain-one activation in the declared class starts with two
installed atoms from one OLD triple and repairs the deleted third atom.
Resource privacy forces the OLD triples to be pairwise disjoint, and exact
saturation forces every deleted atom to be designated exactly once.  The
resulting final state must satisfy item 3. `square`

The theorem suggests the correct quantifier order:

1. choose a `Gamma_Q`-legal resource-private packet packing `S`;
2. choose one designated OLD atom `tau(p)` per packet;
3. construct the exterior body with leave exactly `tau(S)`; and
4. activate the planted packets.

It does not route an arbitrary leave chosen before `S`.

## 3. The finite loose-tree invariant

Every nonempty target-packet incidence component in the stored `n=4,5,6`
states is a tree.  If it contains `p` packet nodes and `t` target nodes, then

\[
                         t=2p+1,qquad |E|=3p.                  \tag{3.1}
\]

Indeed two distinct packets meet in at most one complete OLD atom; the audit
checks connectedness and `|E|=|V|-1` componentwise.  Therefore for every
packet subset `S`, its induced incidence forest obeys

\[
                              |N(S)|\ge2|S|+c(S)>|S|.           \tag{3.2}
\]

Hall consequently saturates every packet node, explaining the equality

\[
                              r_H(M)=|\mathcal P_\sigma|.       \tag{3.3}
\]

This is the smallest positive invariant visible in the fixtures.  It says
that every available packet can receive a distinct target designation.  It
does **not** say that every target has a packet; the isolated vertices in
(0.4) are outside these loose trees.

The component packet-size histograms `(upper,lower)` are

\[
\begin{array}{c|c|c}
n&U&L\\\hline
4&1^2&1^1\\
5&1^8,3^1&1^3,2^3\\
6&1^{21}2^2 3^1 4^2 5^1 6^1 8^1&1^{35}2^7 3^2 11^1.
\end{array}                                                     \tag{3.4}
\]

Exact componentwise independent-set enumeration gives the packing ranks in
(0.2).

## 4. A literal nonmatroid and graphic obstruction

On the stored `n=5` upper shore, lexicographically numbered packets satisfy

\[
                       A=\{p_7\},\qquad B=\{p_1,p_8\}.          \tag{4.1}
\]

Both `A` and `B` are OLD-disjoint packet families.  Packets `p_1` and `p_8`
are disjoint, while `p_7` meets each of them in a different OLD atom.  Hence
neither member of `B` augments `A`, violating the matroid exchange axiom.
The exact three OLD triples are frozen in the audit JSON.

The same fixture separates packing from topology.  It has a unique
ten-packet OLD-disjoint packing, with packet ids

\[
                         0,1,2,3,4,5,6,8,9,10.                  \tag{4.2}
\]

After simultaneous replacement, the three-rail support has cycle rank one.
Dropping packet `9` leaves the nine-packet forest

\[
                         0,1,2,3,4,5,6,8,10,                    \tag{4.3}
\]

so `r_pack=10` but `r_Gamma=9` exactly.  Thus even the clean loose-tree
incidence structure does not make the graphic guard automatic.

## 5. Complete finite scope

The strict occurrence-labelled `n=3` audit has four common bases, indexed by
retained edges `0,1,5,11`.  Retained edges `0,1` have no compatible no-empty
rooted two-shore support.  Retained edges `5,11` each have exactly one such
physical-support pair.  The present audit reconstructs both pairs, and both
have empty native C6 catalogues on **both** shores.  The stored chain state is
the retained-`11` pair.  Hence the singleton obstruction is common to every
authoritative admissible strict `n=3` state.

For `n=4,5,6`, exactly one complete `Q`/upper/lower representative state is
serialized in the authenticated chain witness, and all are audited in
(0.2).  Existing endpoint-orientation and SBE files which store only masks or
fractional existence do not materialize new packet hosts and are not silently
counted as zero-rank states.

The chain does authenticate the produced parent forest `F_7`, with `429`
paths and `3003` edges, but no `n=7 -> 8` common basis or side representatives
are serialized.  Therefore the `n=7` atomic packet rank is

\[
          \boxed{\text{UNAVAILABLE, not zero and not UNSAT}.}                  \tag{5.1}
\]

## 6. Exact remaining theorem

The weakest repairable induction statement is not “closed-core reserve pays
C6 demand.”  It is:

> **Matching-indexed correlated planting.**  Jointly choose endpoint
> orientation, common basis `Q`, both direct representative matchings, and a
> resource-private native-C6 packing `S`, so that the intended body leave is
> one designated OLD atom per packet and the simultaneous replacement lies
> in the required rooted/graphic/common-cap face.

For a separately proved packet matroid `K`, the exact Rado condition would be

\[
                  r_K(N(X))\ge |X|\qquad(X\subseteq A),          \tag{6.1}
\]

or equivalently

\[
 r_{\rm Rado}(A)=\min_{X\subseteq A}igl(|A\setminus X|+r_K(N(X))\bigr). \tag{6.2}
\]

The actual native OLD-triple system is not such a matroid by Section 4.
A positive induction may instead prepack a past-directed/private bank, use a
compound packet class whose independence is matroidal, or retain the exact
packing-plus-graphic formulation of Theorem 2.1.

No generic closed-core or Joos--Mubayi--Smith argument is used.

## 7. Audit

The dependency-light exact replay is

```text
scratch/audit_threadD_catalan_direct_chain_reserve_c6_rado_20260731.py
scratch/threadD_catalan_direct_chain_reserve_c6_rado_20260731.audit.json
```

It authenticates the chain witness and its independent replay, reconstructs
the two authoritative strict `n=3` states, regenerates every canonical OLD
packet, checks the loose-tree incidence components, computes exact bipartite
matching and conflict-pack ranks, and replays simultaneous packet switches in
the complete three-rail graph.  Runtime is under three seconds on the local
audit machine; no SAT solver or remote search is used.

