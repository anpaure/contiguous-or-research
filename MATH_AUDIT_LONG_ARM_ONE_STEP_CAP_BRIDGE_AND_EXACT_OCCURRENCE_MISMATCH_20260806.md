# Long tagged arms have raw one-step suffix rank, but not yet typed cap rank

**Date:** 2026-08-06  
**Method:** Boolean containment and occurrence audit; no computation or
search  
**Verdict:** the far-arm ports admit an explicit raw rank-`(R+1)` suffix
matching.  The Aug-4 bounded-turn-star theorem independently confirms that
there is no Boolean Hall obstruction.  The remaining mismatch is literal:
an owner Johnson path is not a proved claim-to-port path in the cap network,
and an adjacent-union occurrence is not automatically a legal typed sink
edge after compensation deletion.

## 1. Explicit raw suffixes from the arms

Let `A_i`, `1<=i<=p`, be distinct far-port owners from the long-arm
construction.  Give `A_i` its unique missing tag `g_i`, and let `B_i` be
the owner adjacent to `A_i` on its one-tag arm.  Then

\[
 A_i\cap\mathcal T=B_i\cap\mathcal T
   =\mathcal T\setminus\{g_i\}.
\tag{1.1}
\]

Put

\[
 U_i=A_i\cup B_i.
\tag{1.2}

Because `A_i B_i` is a Johnson edge,

\[
 |U_i|=R+1,
 \qquad A_i\subset U_i.
\tag{1.3}

Moreover

\[
 U_i\cap\mathcal T=\mathcal T\setminus\{g_i\}.
\tag{1.4}

Distinct port tags therefore make all `U_i` distinct.  The incidences

\[
                         A_i\longrightarrow U_i
\tag{1.5}

form a matching from the complete far-port bank to distinct rank-`(R+1)`
values.  This proves raw full-port rank at the Boolean-value level without
any all-cut argument.

Once a depth-`delta` antecedent spelling the arm is fixed, (1.2) is also a
literal interval occurrence: two adjacent owner windows overlap in
`delta` source positions, and their union is the union of the corresponding
`delta+2` consecutive source letters.  Thus the terminal value is not a
formal set absent from the word.

## 2. Comparison with the bounded-turn-star theorem

Set `m=R`.  For each `A_i`, choose a lower facet

\[
                         L_i\subset A_i,qquad |L_i|=R-1.
\tag{2.1}

The facets may be chosen distinct when `p<=R/4`: two distinct rank-`R`
owners share at most one rank-`(R-1)` facet, so at stage `i` fewer than
`i<=R/4` of the `R` facets of `A_i` are forbidden.  Hence

\[
                         A_i\in P_i={L_i+a:a\notin L_i\}.
\tag{2.2}

Theorem 2.1 of
`MATH_THEOREM_BOUNDED_TURN_STARS_ONE_STEP_FULL_PORT_LINKAGE_20260804.md`
links the entire union of the stars `P_i` injectively into rank `R+1`.
Restricting that linkage to `{A_i}` again proves raw full-port rank.  Thus
even without the missing-tag terminals (1.2), arbitrary adjacency among
the lower turns creates no Boolean Hall cut at the present
`p=O(sqrt R)` scale.

For the tagged arms, (1.2) is the stronger and more physical certificate:
the chosen terminal already occurs on the protected factor edge.

### 2.1 The maximal antecedent supplies a lower source-port path

There is an even closer compiler-level object.  Write one length-`L` arm as

\[
 V_i=V_{i-1}-\{D_i\}+\{I_i\}
       \qquad(1\le i\le L),
\tag{2.3}
\]

with all event labels fresh.  On the internal maximal depth-`delta`
antecedent, put

\[
 C_j=\bigcap_{h=0}^{\delta}V_{j+h}
     =V_j\setminus\{D_{j+1},\ldots,D_{j+\delta}\}
       \qquad(0\le j\le L-\delta).
\tag{2.4}
\]

Then every `C_j` has rank `R-delta`, and

\[
 C_{j+1}=C_j-\{D_{j+\delta+1}\}+\{I_{j+1}\}.
\tag{2.5}
\]

Hence the actual source letters on the arm form a fresh Johnson path of
length `L-delta`.  Their adjacent unions

\[
                         W_j=C_j\cup C_{j+1}
\tag{2.6}

have rank `R-delta+1`, are pairwise distinct, and are literal two-letter
source intervals.  All `C_j,W_j` on this arm omit exactly its unique tag;
different arms are separated by tag signature.

Thus every arm contains `Theta(R)` mutually private **raw lower-source
ports** with distinct one-step upper occurrences.  This is closer to the
strict-lower compiler than the owner ports `A_i`.  If a target claim is
assigned to its equal occurrence `C_j` and the residual cap network accepts
the literal edge `C_j -> W_j` with the required terminal type, the
claim-prefix may be taken to end at that already materialized source cell.
The equality assignment and typed edge are still cap-state data; (2.4)--
(2.6) do not assert them for an arbitrary target bank.

## 3. Exact occurrence/type mismatch

The raw matching (1.5) becomes a typed cap suffix linkage only under the
following materialization statement.

### Literal one-step bridge premise

In one fixed cap/phase/guard state, after deleting the compensation and
background capacities:

1. every `A_i` is retained as the declared physical active-port occurrence;
2. every protected adjacent-union interval `U_i` is retained as a distinct
   unused terminal occurrence;
3. the physical directed edge `A_i -> U_i` exists in the residual cap
   network and uses a private capacity;
4. its terminal type is legal for every gain incident with port `A_i`.

Under these four statements the displayed edges themselves prove

\[
 r_{\Gamma_{\rm suf}^{\rm type}}(\{A_i})=p.
\tag{3.1}
\]

No Haxell, Rado, or additional cut theorem is then needed for this port
bank.

The current long-arm theorem proves neither item 1 nor item 3.  Its path is
in the Johnson owner graph: vertices are rank-`R` owner values and its
intermediate incidence vertices are rank-`(R-1)` lower colours.  A cap
prefix, by contrast, is a directed path from an occurrence-labelled claim
state through source-cell/guard capacities to one physical port.  There is
no established network homomorphism sending a Johnson arm to such a
claim-to-port prefix.  Equal set values under two cap states can also have
different structural zeros and terminal types.

Likewise, the fact that `U_i` is a literal upper interval does not by itself
install the directed residual edge in item 3 or keep it disjoint from the
fixed compensation linkage.  These are precisely the occurrence/type rows
left explicit in Corollary 3.1 of the bounded-turn-star theorem.

## 4. Sharpened cap frontier

The Aug-5 common-scan receiver theorem does not remove this occurrence
premise.  Its ports are root-coded capacity-two states `v_(00),v_(01)` and
its suffix is the contextual local move `12 -> 21` in one fixed coordinate
pair.  A far owner `A_i` and the Boolean containment `A_i subset U_i` live
in different state spaces.  No current theorem embeds every far-owner
occurrence into a root-coded receiver square while preserving its phase,
guard, compensation avoidance, and gain type.  Such an embedding would be
a valid alternative proof of the literal one-step bridge, but the common
scan cannot be cited without it.

The far-arm construction has therefore closed the **raw suffix Hall** row.
The cap problem is no longer an abstract search for enough rank-`(R+1)`
sets.  It is the following co-design statement:

> Plant each forced gain prefix so that it ends at its far owner occurrence
> `A_i`, reserve the already present adjacent-union occurrence `U_i`, and
> certify the local owner-to-union containment edge as a private legal typed
> cap edge after compensation deletion.

If this literal one-step bridge is proved, the connector-specific active
ports have full suffix rank exactly.  It would not by itself route the
transported background or the remaining ordinary lower compiler ports;
those retain their existing common-cap semantics.
