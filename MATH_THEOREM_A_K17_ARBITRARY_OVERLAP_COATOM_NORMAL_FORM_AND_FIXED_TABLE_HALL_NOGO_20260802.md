# K17 fixed-table overlap states: the coatom normal form and a one-transition Hall no-go

**Date:** 2026-08-02  
**Lane:** A, integral rotor fusion  
**Status:** exact literal-state normal form and independently replayable finite
K17 obstruction.  The conclusion is confined to one transition per frozen
owner/payload row at native depths `1,2,3`.  It does not obstruct payload
redistribution, a genuinely multi-transition row macro, or a different static
chain table.  No upper-shadow or common-cap/compiler assertion is made.

## 0. Outcome

The canonical disjoint-increment signature is not the real obstruction on the
frozen K17 table.  Even if repeated coordinates are allowed arbitrarily among
the three state letters, every transition from one length-three row to another
has one exact **coatom-split normal form**.

On the authenticated table this complete long-to-long overlap catalogue has
only `4,739` edges.  Its maximum matching into the `18,646` length-three heads
whose bottom has rank greater than one is `2,167`.  There are only `5,647`
short rows.  Therefore, even under the deliberately optimistic assumption
that every short row can precede every hard head, at most

\[
                         2,167+5,647=7,814
\]

hard heads can receive distinct predecessors.  The arbitrary-overlap,
one-transition-per-row face consequently has Hall deficiency at least

\[
                         18,646-7,814=10,832.       \tag{0.1}
\]

Thus overlap enrichment does reduce the canonical certificate `12,999`, but
it cannot close it.  A factor-critical escape must change more than the
three-letter state of an otherwise fixed row: it must redistribute payload
addresses across rows, realize a row by a genuinely larger macro, or change
the chain/owner table.  A bounded exceptional sidecar cannot repair (0.1).

## 1. Frozen rows and the maximal overlap family

The explicit table has one row for every rank-eight root.  A length-three row
`i` is

\[
 L_i\subset M_i\subset U_i\subset T_i,qquad
 (|M_i|,|U_i|,|T_i|)=(7,8,9),                         \tag{1.1}
\]

where `T_i` is its assigned owner and

\[
                         z_i=T_i\setminus U_i          \tag{1.2}
\]

is a singleton.

An arbitrary-overlap state for row `i` is a triple of nonempty letters

\[
                         h_i=(A_i,B_i,C_i)             \tag{1.3}
\]

whose native suffix unions are exactly its frozen payload:

\[
 C_i=L_i,qquad B_i\cup C_i=M_i,qquad
 A_i\cup B_i\cup C_i=U_i.                            \tag{1.4}
\]

No disjointness is imposed.  Hence (1.3)--(1.4) are the largest possible
three-letter state family preserving that row's three named targets at their
native depths.

A literal predecessor transition `j -> i` means that the de Bruijn shift is

\[
 h_j=(D,A_i,B_i),qquad h_i=(A_i,B_i,C_i),            \tag{1.5}
\]

and that the transition into `h_i` has owner `T_i`:

\[
                         D\cup U_i=T_i.                \tag{1.6}
\]

The state `h_j` must simultaneously satisfy (1.4) for row `j`.

## 2. Exact coatom-split normal form

### Theorem 2.1 (complete long-to-long overlap criterion)

Let `i,j` be length-three rows.  An arbitrary-overlap literal transition
`j -> i` exists if and only if there are

\[
                         x\in L_i,qquad
                         Y\subseteq L_i\setminus\{x\} \tag{2.1}
\]

such that

\[
 \boxed{
 \begin{aligned}
 L_j&=(M_i\setminus L_i)\cup Y,\\
 M_j&=U_i\setminus\{x\},\\
 U_j&=(U_i\setminus\{x\})\cup\{z_i\}.
 \end{aligned}}                                      \tag{2.2}
\]

Whenever (2.2) holds, a reduced literal witness is

\[
 \begin{aligned}
 B&=(M_i\setminus L_i)\cup Y,\\
 A&=(U_i\setminus M_i)\cup
          \bigl(L_i\setminus(Y\cup\{x\})\bigr),\\
 h_i&=(A,B,L_i),\\
 h_j&=(\{z_i\},A,B).
 \end{aligned}                                       \tag{2.3}
\]

All four displayed letters are nonempty.  Both frozen payload chains and
both rank-eight roots are reproduced exactly, and the transition owner is
exactly `T_i`.

#### Proof

Assume first that (1.5) is a transition.  The payload equations for `j`
and `i` give

\[
 B_i=L_j,qquad A_i\cup B_i=M_j,qquad
 B_i\cup L_i=M_i,qquad M_j\cup L_i=U_i.             \tag{2.4}
\]

Since `M_j` is a subset of `U_i` of ranks seven and eight, respectively,

\[
                         M_j=U_i\setminus\{x\}        \tag{2.5}
\]

for a unique `x in U_i`.  The last equation in (2.4) forces
`x in L_i`.  Since `B_i union L_i=M_i` and
`B_i` is a subset of `M_j=U_i-{x}`,

\[
 B_i=(M_i\setminus L_i)\cup Y
 \quad\hbox{for some }Y\subseteq L_i\setminus\{x\}. \tag{2.6}
\]

This proves the first two rows of (2.2).

The first letter `D` of `h_j` satisfies

\[
                         D\cup M_j=U_j,qquad
                         D\cup U_i=T_i.               \tag{2.7}
\]

Thus `D` contains `z_i`.  It cannot contain `x`, because then
`D union M_j` would contain the nine-set
`M_j union {x,z_i}`, whereas `U_j` has rank eight.  All other possible
members of `D` already lie in `M_j`.  Hence (2.7) forces the third row of
(2.2).  This proves necessity.

Conversely assume (2.2) and define (2.3).  Direct union gives

\[
 B\cup L_i=M_i,qquad A\cup B=U_i\setminus\{x\},qquad
 A\cup B\cup L_i=U_i.                                \tag{2.8}
\]

Therefore `h_i` realizes the payload of `i`, while

\[
 B=L_j,qquad A\cup B=M_j,qquad
 \{z_i\}\cup A\cup B=U_j                            \tag{2.9}
\]

shows that `h_j` realizes the payload of `j`.  Equation (1.5) is literal,
and `{z_i} union U_i=T_i`, so the transition has the prescribed owner.
Finally `M_i-L_i`, `U_i-M_i`, `L_i`, and `{z_i}` are nonempty,
which proves literal legality.  \(\square\)

### Corollary 2.2 (minimality of the split)

At the owner/root/payload projection, every long-to-long arbitrary-overlap
transition reduces to (2.3) by deleting redundant elements of
`A_i cap B_i` and `D cap M_j`.  Hence the only essential enrichment is
the distribution of `L_i-{x}` between the first two head letters.  For a
fixed `x`, its menu is the Boolean cube

\[
                         Y\subseteq L_i\setminus\{x\}. \tag{2.10}
\]

This reduction is semantic: deleting redundant occurrences may change a
residence history or another occurrence-labelled guard.  Therefore (2.3)
is complete for existence at the fixed owner/payload projection, but it is
not a license to simplify a previously certified history-bearing witness.

## 3. Exact K17 catalogue and Hall certificate

Let `H` be the `18,646` length-three rows with `|L_i|>1`, the same hard
head bank used in the canonical obstruction.  Form the bipartite graph
`G_33` whose left and right vertices are the `18,663` length-three rows
and whose edge `j -> i` is exactly (2.2).

The authenticated table gives:

\[
\begin{array}{lr}
|E(G_{33})|&4,739,\\
\text{left rows of positive degree}&3,658,\\
\text{hard heads of positive degree}&2,239,\\
\nu(G_{33})&2,168,\\
\nu(G_{33}[\text{left},H])&2,167.
\end{array}                                           \tag{3.1}
\]

The last matching value has a Kőnig minimum-vertex-cover certificate of the
same size; the deterministic serialization used by the verifier has SHA256

```text
9596de583f6fa461894e450313a1b0b4741c583804b828440425117b0563a029
```

There are `5,647` rows of chain length at most two.

### Theorem 3.1 (arbitrary-overlap fixed-table no-go)

No balanced literal rotor exists on the frozen table if every owner/payload
row is realized by one depth-three transition and every length-three payload
uses its three native suffix addresses, even when arbitrary repeated
coordinates are allowed in every state letter.

More precisely, the predecessor Hall deficiency on `H` is at least
`10,832`.

#### Proof

In a balanced one-copy rotor the `18,646` heads in `H` require distinct
predecessor rows.  By Theorem 2.1, the number that can be assigned distinct
length-three predecessors is at most the matching number `2,167` in (3.1).
Even granting every one of the `5,647` shorter rows as a universally legal
additional predecessor supplies at most

\[
                         2,167+5,647=7,814           \tag{3.2}
\]

heads.  Hence at least

\[
                         18,646-7,814=10,832         \tag{3.3}
\]

heads remain unmatched.  This optimistic treatment of shorter rows can only
weaken the obstruction, so (3.3) is unconditional on the stated face.
\(\square\)

The theorem is stronger than a failure of one chosen bounded menu: the
long-row part already includes every arbitrary-overlap three-letter state
which preserves the frozen payload at the native addresses.  Residence,
fixed owner phase, source guards, and topology can only delete edges.

## 4. Consequence for factor-critical bridges

The abstract factor-critical conveyor remains correct, but it cannot be
instantiated on this table by merely grouping rows and adding more overlap
states of the form (1.3).  Every internal module path and every bridge built
from one ordinary transition per frozen row is still a predecessor matching
on the same graph, and therefore inherits Theorem 3.1.

A successful factor-critical bridge for this fixed K17 seed must violate at
least one of the following face conditions:

1. one physical transition realizes one frozen owner/payload row;
2. the three targets of a long row occupy suffix depths `1,2,3` in that
   transition; or
3. the chain-to-owner attachment is frozen.

Examples of genuine escape mechanisms are a matching-closed macro which
redistributes two or more payload chains among the same owner rows, a larger
address block whose contraction is not a single state edge, or a new static
chain/owner assignment.  Such a macro must still expose the exact
factor-critical root/socket boundary and must be checked against the full
occurrence-labelled state; Theorem 3.1 does not supply it.

The deficit `10,832` also shows that an `O(1)` exceptional sidecar cannot
repair this frozen one-transition table.  Cross-depth fusion can telescope
many *available* factor-critical modules, but it cannot manufacture the
missing direct row incidences.

### Theorem 4.1 (minimum row support of a rowwise escape)

Start with the optimistic graph used in Theorem 3.1: every short row is
adjacent to every hard head, and long-to-long edges are the complete coatom
catalogue.  Suppose a new one-transition construction changes transition
incidences only at a set `R` of `q` row identities.  Thus every new edge with
both endpoint row identities outside `R` was already present in the
optimistic graph.  If the new graph has a matching covering every hard head,
then

\[
                              q\ge 5,416.             \tag{4.1}
\]

If only the predecessor-side copies of rows in `R` acquire new incidences,
while every head state remains on the old face, then

\[
                              q\ge 10,832.            \tag{4.2}
\]

#### Proof

The old optimistic graph has matching number at most `7,814` into the hard
head bank.  Changing one row identity can alter edges incident with at most
its one left copy and one right copy.  Deleting those two copies from any new
matching leaves an old matching, so the matching number increases by at most
two per changed identity.  Hence

\[
                         18,646\le7,814+2q,
\]

which gives (4.1).  Under the one-sided hypothesis only the `q` changed left
copies can support genuinely new matching edges, so the increase is at most
`q`, giving (4.2).  \(\square\)

Thus the first admissible escape may use a bounded **state type**, but not a
bounded total row support.  A proposed multirow factor-critical absorber must
either rethread thousands of K17 rows or introduce auxiliary transitions
outside the one-transition-per-row model.  This is compatible with the
factor-critical conveyor, whose path support may be linear even when its live
endpoint defect is constant.

## 5. Scope: finite K17 versus all `k`

The normal form in Theorem 2.1 is dimension-free for a three-target native
flag with consecutive top ranks `7,8,9`, after replacing those ranks by
`r-2,r-1,r`.  The numerical obstruction (3.1)--(3.3) is not.  It uses the
particular authenticated K17 chain table and its fixed owner attachment.
No all-`k` density or impossibility claim follows.

Nothing here checks arbitrary-width upper witnesses, a common source cap,
or compiler matching.  Those gates are separate; they cannot rescue a
lower/state Hall failure, but their absence is not being counted as damage.

## 6. Audit artifact

The lightweight exact verifier

```text
scratch/a_k17_coatom_split_bridge_20260802/
  audit_a_k17_coatom_split_bridge_20260802.py
```

replays table SHA
`029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1`,
enumerates (2.1)--(2.3), checks every literal union/shift/owner identity,
computes both Hopcroft--Karp matchings, and independently verifies the
Kőnig cover.  The script SHA is
`24fbd650bae6d6e42eb517132e14791df82ca1b9a2943087f194935fc7320c77`.
