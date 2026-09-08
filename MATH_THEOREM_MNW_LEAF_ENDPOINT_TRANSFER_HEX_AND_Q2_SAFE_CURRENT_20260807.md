# The missing MNW leaf endpoint transfer is one q2-safe transport hex

**Date:** 2026-08-07  
**Method:** explicit incidence hexagon and exact inverse multiplicities; no
computation or search  
**Status:** unconditional literal local switch in the factor obtained from
the canonical factor by applying the gamma-alpha relay bank.  It installs
the missing positive-context incidence and is q2-support-safe in that
partial rethreading.  A completion to one MNW spanning hypertree must be
chosen to preserve its six edge phases and the named q2 backup occurrence;
that completion is not proved here.

## 1. The missing edge

At the defective positive-context owner put

\[
 X=1010001101,
 \qquad
 R=1110001101=X+2,
 \qquad
 Q=1010001111=X+9.                                  \tag{1.1}

After mirror gamma, `(X,R)` is selected and `(X,Q)` is unselected.  The
prepared `H0` boundary needs the reverse status.

Choose the active core label `c=1` and put

\[
                         K=X-1=0010001101.            \tag{1.2}

The three active labels are `1,2,9`.  The corresponding incidence hexagon
has owners

\[
\begin{aligned}
X   &=K+1=1010001101,\\
X_2 &=K+2=0110001101,\\
X_9 &=K+9=0010001111,
\end{aligned}                                        \tag{1.3}

and colours

\[
\begin{aligned}
R&=K+12=1110001101,\\
M&=K+29=0110001111,\\
Q&=K+19=1010001111.
\end{aligned}                                        \tag{1.4}

## 2. The hexagon is alternating in the current factor

At `X`, the gamma-alpha factor selects `R` and not `Q`.

The other two owners begin with zero, so the **two gamma-alpha relay
tuples** do not change their canonical incidences.  (An arbitrary later
MNW-tree completion could do so and is outside this local theorem.)  The
exact MSW touching-step rule gives:

* at `X_2`, the selected additions are `5,9`; hence `(X_2,M)` is selected
  and `(X_2,R)` is unselected;
* at `X_9`, the unique endpoint addition is `1`; hence `(X_9,Q)` is
  selected and `(X_9,M)` is unselected.

Thus the six cyclic edge statuses are

\[
\begin{array}{c|cccccc}
\text{edge}&XR&X_2R&X_2M&X_9M&X_9Q&XQ\\ \hline
\text{status}&1&0&1&0&1&0.
\end{array}                                                   \tag{2.1}

The incidence hexagon is literally alternating.  Toggling it performs

\[
 XR\mapsto XQ                                      \tag{2.2}

and compensates both colour degrees through the other four edges.  No
additional q1 matching is needed.

## 3. Exact q2 current

At `X`, the untouched mate is `X+5`.  The turn changes as

\[
 X+\{2,5\}=1110101101
 \longmapsto
 X+\{5,9\}=1010101111.                              \tag{3.1}

At `X_2`, the untouched mate is `X_2+5`.  Its turn changes as

\[
 X_2+\{5,9\}=0110101111
 \longmapsto
 X_2+\{1,5\}=1110101101.                            \tag{3.2}

The intermediate target `1110101101` cancels.  Owner `X_9` is a path
endpoint before and after the switch and carries no q2 turn.  Therefore

\[
 \boxed{
 \partial_2 H_{\rm leaf}
 =[1010101111]-[0110101111].}                        \tag{3.3}

Both targets in (3.3) have canonical multiplicity exactly two.  For
`1010101111`, the inverse witnesses are `(3,9)` and `(1,10)`.  For
`0110101111`, they are `(5,9)` and `(3,10)`.  The two possible `q`
positions are nine and ten, so these lists are exhaustive.

The gamma-alpha relay pair does not have either target in its signed q2
current.  Consequently their loads in the canonical-plus-relay factor are
still two before the leaf switch.  After (3.3) they are three and one.  No
q2 target becomes uncovered in this partial rethreading.

### Theorem 3.1 (q2-safe endpoint transfer)

In the canonical-plus-gamma-alpha factor, the missing positive-context
incidence (5.2) of the boundary-defect theorem can be installed by one
literal alternating incidence hexagon while preserving the complete q1
palette and every q2 target.

## 4. Dyck-suffix tensoring

Append any Dyck suffix `v` to every owner and colour above.  All selected
incidence tests persist by MSW concatenation.  Every q2 prefix in (3.1)--
(3.3) ends at height four, so the exact inverse multiplicities remain two
after suffixing.

Every vertex of the tensor copy has suffix restriction `U(v)`.  Distinct
suffixes therefore give disjoint hexagons.  The complete bank

\[
                         \{H_{\rm leaf}v:v\in D_{m-5}\} \tag{4.1}

can be toggled simultaneously without incidence collisions.

## 5. Relation to the annulus sweep

This switch is not an unrelated patch.  The owner `X_2` is exactly the
natural source-context copy

\[
                         01\,10001101,

and `M=01\,10001111` is its selected `Q^-` edge in `H0`.  Thus
`H_leaf` is precisely the transport face associated with that base
incidence under the context move `01->10`.

Toggling it installs the missing destination edge `XQ`, but at the same
time toggles the corresponding source edge `X_2M`.  Therefore it cannot be
blindly prepended to the standard sequence "toggle the whole source relay,
then sweep the annulus": that ordering would reverse its required source
phase.

The remaining literal statement is narrower but includes a completion row:

> **Interleaved one-prefix sweep lemma.**  Order the four source relay
> hexagons and the transport faces so that `H_leaf` is used in its available
> phase, every other face becomes alternating when reached, all source and
> rail incidences are restored, and the desired `10` relay remains.
> Complete the selected packet bank to one MNW spanning hypertree without
> changing those prepared phases or consuming the last provider of the
> negative target in (3.3).

The endpoint incidence and its q2 halo are now solved exactly.  Only this
finite face-order/topology condition remains for the second relay.

## 6. Topological scope

As a local degree-preserving switch, `H_leaf` preserves the owner and q1
rows.  Its effect on the number and pairing of path components depends on
the cyclic order of its three selected edges in the current Hamiltonized
factor.  No component claim is made here.  The interleaved sweep must either
show that its component action cancels with the other prism faces or include
it in the final connector ledger.
