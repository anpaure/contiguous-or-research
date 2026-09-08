# Strict-occurrence isoperimetry, exact codegrees, and the `eta>=3` counterexample

Date: 2026-07-31  
Status: all-parameter local structure and exact robust-Hall reformulation;
dependency-free replay on the authenticated recursive chain `n=3,...,7`;
literal counterexample showing that Catalan linearity, recursive supply, and
`eta^pm>=3` do not imply robust SBE.  Robust SBE on the `n>=5` members is
not claimed.

## 0. Result

Fix either strict direct occurrence graph

\[
                         G_F^s=(O_s,X),                 \tag{0.1}
\]

of a Catalan linear forest `F` on the `n`-sets of a `2n`-set.  Thus

\[
 |X|=M={2n\choose n},\quad |O_s|=P={2n\choose n-2},
 \quad N={2n\choose n-1},\quad C=M-P,\quad R=N-C.      \tag{0.2}
\]

The following statements hold for every Catalan linear forest, without a
recursive or `eta` hypothesis.

1. Every outer row has exactly `n+2` occurrence edges and at least **three
   distinct** middle neighbours.  The family of simple outer
   neighbourhoods is an antichain.
2. Simple pair codegrees are supported only at Johnson distance one or two.
   For middle pairs the sharp containment bounds are `n-1` and `1`; for
   outer pairs they are `n+1` and `1`.
3. Robust SBE has an exact edge-isoperimetric form.  If `J subseteq X`, let
   `ell_s(J)` be the number of occurrence edges from `J` to outer rows not
   wholly supported in `J`, let `p_F(J)` count path components whose two
   endpoints are in `J` (an isolate counts once), and let `chi_F(J)` count
   nontrivial paths with exactly one endpoint in `J`.  Then robust SBE is
   equivalent to

   \[
   \boxed{\quad
   n\ell_s(J)+2(n+1)p_F(J)-n\chi_F(J)-2|J|\ge0
   \quad(J\subseteq X).\quad}                         \tag{0.3}
   \]

   Equivalently,

   \[
   \ell_s(J)-\chi_F(J)\ge
   \left\lceil {2\bigl(|J|-(n+1)p_F(J)\bigr)\over n}\right\rceil .
                                                               \tag{0.4}
   \]

Equation (0.4) is the exact endpoint-corrected occurrence isoperimetry
needed for an orientation-forgetting theorem.  It is stronger and more
structural than a maximum-degree estimate: `ell` is a literal occurrence
edge boundary, while the right side is the excess of the chosen path mass
over the Catalan mean path order `n+1`.

There is a sharp positive threshold for atomic Hall cores.  A single outer
row can never violate robust SBE once `n>=5`, because

\[
                         3R\ge N\qquad(n\ge5).         \tag{0.5}
\]

This explains the observed regeneration scale, but it does not prove the
global inequality: multirow cores remain.

Most importantly, the authenticated recursively supplied parameter-four
forest has `eta^-=eta^+=3` and nevertheless violates (0.3) on **both**
shores.  On each shore two outer rows have a seven-element union `J`, no
complete endpoint pair, four split endpoint pairs, and occurrence boundary
six.  Hence

\[
       4\cdot6-4\cdot4-2\cdot7=-6<0,                 \tag{0.6}
\]

or, in the original units, robust Hall defect `14`.  Thus

\[
 \boxed{\text{Catalan linear forest + recursive supply + }\eta^\pm\ge3
        \not\Longrightarrow\text{ robust SBE}.}       \tag{0.7}
\]

Any preservation theorem needs one additional multirow occurrence-cut
state.  The most economical exact candidate is (0.4) itself, or a
recursively checkable sufficient lower bound for its left side.

## 1. The local turn model

Consider the upper shore; the lower shore follows by complementation.  Fix
an outer colour `V`, an `(n+2)`-set.  Its `n+2` occurrences are indexed by
`x in V`.  The child edge of upper colour `V-x` has endpoints

\[
                  V-\{x,a_x\},\qquad V-\{x,b_x\},     \tag{1.1}
\]

for a unique unordered pair `{a_x,b_x} subseteq V-x`.  The corresponding
middle neighbour is

\[
                         D_x=V-\{a_x,b_x\}.            \tag{1.2}
\]

In the complement-pair model for the `n`-sets inside `V`, (1.1) is a turn
in the line graph of `K_V`, centred at `x`, and (1.2) is its opposite edge.
The `n+2` turns are distinct child edges and therefore form a subforest of
`F`.

### Lemma 1.1 (three-neighbour lemma)

Every outer row has at least three distinct middle neighbours.

#### Proof

One neighbour is impossible because `D_x` contains `x`; one `n`-set cannot
contain all `n+2` possible centres.

Suppose there are exactly two neighbours, whose omitted pairs are `e_1`
and `e_2`.  A centre lying in `e_i` cannot use neighbour `V-e_i`.
Therefore `e_1 cap e_2` is empty.  Write

\[
                         e_1=\{a,b\},\qquad e_2=\{c,d\}.
\]

The centres `a,b` must use `e_2`, while `c,d` must use `e_1`.  The four
child turns are

\[
 ac-ad,\quad bc-bd,\quad ac-bc,\quad ad-bd,           \tag{1.3}
\]

in complement-pair notation.  They form the four-cycle
`ac-ad-bd-bc-ac`, contradicting that `F` is a forest.  Hence at least three
neighbours occur. `square`

The bound is exact: the authenticated chain contains degree-three rows at
every audited scale except on one of the two smallest individual shores.

### Lemma 1.2 (neighbourhood antichain)

For distinct outer colours `V,V'`, neither simple neighbourhood is
contained in the other.

#### Proof

Every common middle neighbour is an `n`-subset of `V cap V'`.  If the
outer Johnson distance is at least two, the intersection has order at most
`n`, so Lemma 1.1 rules out containment.  At distance one, choose the unique
element `x in V-V'`.  The occurrence of row `V` centred at `x` has a
middle neighbour containing `x`, and hence not contained in `V'`.  Thus it
is not a neighbour of `V'`.  The reverse argument is symmetric. `square`

For a fixed incident pair `D subset V`, `V-D={a,b}`, its occurrence
multiplicity is exactly

\[
 \#\{x\in D:\ F\text{ contains the edge }
       (D-x+a)(D-x+b)\}.                               \tag{1.4}
\]

It is at most `n-d_F(D)` and hence at most `n`.  Equality can occur only
when `D` is an isolated child vertex.  The authenticated chain attains
maximum multiplicity `n-1` at every `n=3,...,7`; this empirical value is
not promoted to a universal bound.

## 2. Exact pair codegrees

Let `gamma_X(D,E)` be the number of simple outer rows adjacent to both
middle vertices.  A common upper row must contain `D union E`; a common
lower row must be contained in `D cap E`.  Consequently, on either shore,

\[
 \gamma_X(D,E)=0\quad\text{if }d_J(D,E)>2,            \tag{2.1}
\]

and

\[
 \gamma_X(D,E)\le
 \begin{cases}
 n-1,&d_J(D,E)=1,\\
 1,&d_J(D,E)=2.
 \end{cases}                                         \tag{2.2}
\]

Indeed, at distance one the union above, or the intersection below, leaves
`n-1` choices for the final coordinate; at distance two the outer set is
unique.

Likewise, let `gamma_O(V,V')` be the number of common middle neighbours of
two outer rows.  The same containment count gives

\[
 \gamma_O(V,V')=0\quad(d_J(V,V')>2),                 \tag{2.3}
\]

and

\[
 \gamma_O(V,V')\le
 \begin{cases}
 n+1,&d_J(V,V')=1,\\
 1,&d_J(V,V')=2.
 \end{cases}                                         \tag{2.4}
\]

These are exact ambient containment bounds; the strict graph retains only
the pairs selected by the child turns (1.1).  Lemma 1.2 adds

\[
 \gamma_O(V,V')\le
 \min\{|N(V)|-1,|N(V')|-1\}.                         \tag{2.5}
\]

The audit computes the complete positive-codegree histograms, separated by
Johnson distance, on all ten strict shores of the authenticated chain.  It
finds no support or magnitude violation.

## 3. Exact characterization of Hall-deficient sets

For `H subseteq X`, robust SBE means

\[
 N|\partial_sH|\ge R|H|+Cq_F(H),                     \tag{3.1}
\]

where `partial_sH` is the family of outer rows meeting `H`, and `q_F(H)`
counts path components having an endpoint in `H`.

Put `J=X-H`, and define

\[
 A_s(J)=\{o:N_G(o)\subseteq J\}.                     \tag{3.2}
\]

Let `p_F(J)` count components all of whose endpoints lie in `J`; for an
isolate this means its unique vertex lies in `J`.  Then

\[
 |\partial_sH|=P-|A_s(J)|,\qquad
 q_F(H)=K-p_F(J).                                    \tag{3.3}
\]

The total-capacity identity

\[
                             NP=RM+CK                \tag{3.4}
\]

turns (3.1) into the closed-row inequality

\[
              N|A_s(J)|\le R|J|+Cp_F(J).             \tag{3.5}

Thus every Hall-deficient set is exactly a set `J` supporting too many
complete strict outer rows.

To expose the missing expansion, let `ell_s(J)` count occurrence edges from
`J` to `O_s-A_s(J)`.  The exact middle occurrence-degree law gives

\[
 (n+2)|A_s(J)|
   =\sum_{D\in J}(n-d_F(D))-\ell_s(J).                \tag{3.6}
\]

Put

\[
 \delta_F(J)=\sum_{D\in J}(2-d_F(D)).                \tag{3.7}
\]

The endpoint decomposition is

\[
                   \delta_F(J)=2p_F(J)+\chi_F(J).    \tag{3.8}
\]

Substituting (3.6)--(3.8) and

\[
 {C\over N}={4n+2\over n(n+2)},\qquad
 {R\over N}={n^2-2n-2\over n(n+2)}                 \tag{3.9}
\]

into (3.5) gives exactly (0.3).  In particular the signed failure identity
is

\[
 n(n+2)\bigl(N|A|-R|J|-Cp\bigr)
 =-N\bigl(n\ell+2(n+1)p-n\chi-2|J|\bigr).           \tag{3.10}
\]

This proves both necessity and sufficiency of (0.3)--(0.4).  It also shows
why raw degree counting almost closes the gate: all that remains after the
degree law is the small occurrence boundary `ell`, corrected by component
length excess and split endpoints.

### Corollary 3.1 (one-row threshold)

For `J=N_G(o)`, Lemma 1.2 gives `A_s(J)={o}`, while Lemma 1.1 gives
`|J|>=3`.  Therefore

\[
 R|J|+Cp_F(J)-N\ge3R-N.                              \tag{3.11}
\]

Now

\[
 3R-N={2N(n^2-4n-3)\over n(n+2)}\ge0                \tag{3.12}
\]

exactly for integral `n>=5`.  Thus no one-row robust-Hall obstruction
exists from parameter five onward. `square`

The analogous two-row statement is not proved universally.  It is checked
exactly on the authenticated chain and has positive margin at `n=5,6,7`.

## 4. The minimal recursive `eta` counterexample

The parameter-four forest is the literal output of the authenticated
parameter-three direct lift.  It has

\[
                         \eta^-=\eta^+=3.             \tag{4.1}
\]

On the upper shore take outer masks

\[
                            183,\quad237.             \tag{4.2}
\]

Their simple neighbourhoods are

\[
 \{23,53,165,177\},\qquad
 \{165,108,172,232\}.                                \tag{4.3}
\]

On the lower shore take outer masks

\[
                            129,\quad160,             \tag{4.4}
\]

with neighbourhoods

\[
 \{147,195,197,225\},\qquad
 \{165,225,226,232\}.                                \tag{4.5}
\]

On either shore their union `J` has

\[
 |J|=7,\quad |A_s(J)|=2,\quad p_F(J)=0,
 \quad\chi_F(J)=4,\quad\ell_s(J)=6.                 \tag{4.6}
\]

Since `(N,R,C)=(56,14,42)`, (3.5) fails by

\[
                 56\cdot2-14\cdot7=14.              \tag{4.7}
\]

This is a two-row, seven-middle-set obstruction.  No one-row core is
deficient at `n=4`; hence it is minimal in number of generating outer rows.
It proves (0.7).  The complete orientation census gives larger maximum
robust defects `(42,56)` on the upper and lower shores, respectively, but
the small core (4.2)--(4.7) is the structural obstruction.

At `n=3`, the still smaller obstruction is one outer row with four middle
neighbours, no complete endpoint pair, two split paths and occurrence
boundary one.  Its robust defect is eleven on either shore.

## 5. Authenticated chain audit

The dependency-free audit is

```text
scratch/audit_catalan_strict_occurrence_isoperimetry_n3_n7_20260731.py
scratch/catalan_strict_occurrence_isoperimetry_n3_n7_20260731.audit.json
```

with SHA-256 hashes

```text
7fc509803f4ce0a2d5ee0a8148c2a803960d4812048ec796c7a941b1942ef5c5
e07be8f88fac0264d9a6c5d187e164dbc47db58373993e0156daaa294fb18b55
```

and canonical payload hash

```text
c42f0ff5d6a1ddbcabc3cc237a09f69753743d5fa5f431d9623b1b3c34178eef
```

It reconstructs both strict occurrence graphs rather than trusting stored
claims.  For each shore at `n=3,...,7` it verifies:

* the exact occurrence-degree laws;
* the facet slacks
  `(3,3),(3,3),(4,3),(5,4),(4,5)`;
* outer simple degree at least three;
* every codegree support and bound in Section 2, with complete positive
  histograms;
* (3.10) on every one-row and every intersecting two-row generated core;
  and
* exact maximum robust defects `(11,11)` and `(42,56)` by exhausting all
  coherent orientations at `n=3,4`.

At `n=5,6,7`, all one-row and intersecting-two-row cores have nonpositive
defect.  The maximum pair-core defects `(upper,lower)` are respectively

\[
                    (-126,-126),\quad(-957,-957),
                    \quad(-5005,-5005).               \tag{5.1}
\]

The stored, fully reversed, and two alternating orientations also pass
ordinary SBE on both shores at all three parameters.  These are exact finite
checks, **not** an exhaustive robust-SBE proof at `n=5,6,7`.

## 6. Consequence

The hoped-for implication from the currently retained structural state is
false at the first recursively supplied child.  `eta>=3` is a physical
continuation condition; it does not control dense multirow cores in the
strict occurrence graph.  Codegree bounds alone also cannot replace the
missing state: the parameter-four obstruction uses only one shared middle
neighbour between its two rows.

The narrow corrected target is therefore:

> **Endpoint-corrected occurrence-isoperimetry preservation.**  Choose the
> direct lift so that the output forest satisfies (0.4) on both strict
> shores, or at least admits one endpoint orientation plus common basis and
> physical representatives.  Carry enough four-sector reserve information
> to prove (0.4) after the next lift.

The first clause is robust and stronger than necessary; the second is the
actual DERF target.  This note proves neither preservation statement.  It
does remove the possibility that the already observed `eta` and recursive
supply properties make robust SBE automatic.
