# Independent audit of the rotor-circulation multicover theorem

Date: 2026-07-24

## Verdict

The abstract rotor graph is strongly connected for

\[
 1\le d\le m-2.
\]

The submitted group calculation is correct, including directed
reachability.  The endpoint `d=m-1` is genuinely disconnected, while `d=0`
is a separate Johnson-graph case not covered by the displayed rotor formula.

The submitted prefix-state MTF lemma is correct.  The symbol `gamma` records
the useful chain prefix and only the union of the older remainder; it does
not assert that the remainder is one physical MTF block.  The remaining
physical blocks form an arbitrary ordered partition of the abstract residual
set, and this invariant survives every rotor edge.

Consequently an abstract Euler circulation gives one genuine finite MTF word
after one initialization, but generally not a periodic orbit of complete
MTF states.  Any theorem statement claiming physical state closure must be
weakened accordingly.

## 1. The abstract graph

Put

\[
 r=m-d,
\]

and let an abstract state be

\[
 \gamma=(L;z_1,\ldots,z_{2d};R),
 \qquad |L|=|R|=r,
 \tag{1.1}
\]

where the displayed sets and singletons partition `[2m]`.  For `x in L`
and `y in R`, the submitted rotor successor is

\[
 \gamma'=
 (L-x+y;x,z_1,\ldots,z_{2d-1};R-y+z_{2d}).
 \tag{1.2}
\]

The graph has `r^2` outgoing arcs at every vertex.  The incoming count is
also `r^2`, either by direct inversion or by the slot action below.

## 2. Exact audit of the group argument

Temporarily order the two end blocks and use slots

\[
 a_1,\ldots,a_r,q_1,\ldots,q_{2d},b_1,\ldots,b_r.
\]

Internal permutations of the `a` and `b` slots form

\[
 H=\operatorname{Sym}(A)\times\operatorname{Sym}(B)
\]

and do not change the abstract state.  Choosing the contents of slots
`a_i,b_j` as `x,y` acts on ordered slot fillings by the cycle

\[
 c_{ij}=(a_i,q_1,\ldots,q_{2d},b_j),
 \tag{2.1}
\]

up to the harmless global choice of left-versus-right action.

Assume `d>=1` and `r>=2`.  With the usual right-to-left permutation
composition,

\[
 \boxed{c_{21}c_{11}^{-1}=(a_1,a_2,q_1).}
 \tag{2.2}
\]

Multiplying on the right by the internal transposition `(a_1,a_2)` gives

\[
 (a_1,a_2,q_1)(a_1,a_2)=(a_1,q_1).
 \tag{2.3}

Conjugating this transposition by powers of

\[
 c_{11}=(a_1,q_1,\ldots,q_{2d},b_1)
\]

gives every adjacent transposition around that slot cycle:

\[
 (a_1,q_1),(q_1,q_2),\ldots,(q_{2d},b_1),(b_1,a_1).
 \tag{2.4}

These generate the symmetric group on
`{a_1,q_1,...,q_(2d),b_1}`.  Together with `H`, they generate the full
`Sym(2m)`.  Hence the corresponding Schreier graph on abstract states is
connected.

This also proves **directed** strong connectivity.  Every rotor generator
has finite order `2d+2`, so

\[
 c_{ij}^{-1}=c_{ij}^{2d+1}
\]

is a positive word in directed rotor moves.  Internal elements of `H` are
free changes of ordered representative of the same quotient state.  Thus
the semigroup of directed moves has the same quotient orbit as the generated
group.

### Endpoint corrections

* If `d=m-1`, then `r=1`.  There is only one outgoing move, the rigid
  rotation `(a_1,q_1,...,q_(2d),b_1)`, and the graph splits into cyclic-order
  orbits.  The hypothesis `d<=m-2` is sharp.
* If `d=0`, the symbols `q_1` and `z_(2d)` in the submitted formula do not
  exist.  The natural corrected graph swaps `x in L` with `y in R`; it is
  the bidirected Johnson graph and is connected.  It needs a separate
  one-line proof, not (2.2).

## 3. Why the prefix-state convention is necessary

Let

\[
 \Pi=(L,\{z_1\},\ldots,\{z_{2d}\},R)
\]

be the canonical complete last-occurrence partition.  The only possible
update set whose new leading block is `L-x+y` is

\[
 X=L-x+y.
\]

Exact block subtraction gives

\[
 \boxed{
 M_X(\Pi)=
 (L-x+y,\{x\},\{z_1\},\ldots,\{z_{2d}\},R-y).
 }
 \tag{3.1}

The canonical abstract successor records the tail only through its union,
and would be displayed as ending

\[
 \ldots,\{z_{2d-1}\},R-y+z_{2d}.
 \tag{3.2}

Equations (3.1) and (3.2) are not equal as complete ordered partitions: MTF
subtraction preserves `{z_(2d)}` as its own older block and never merges it
with `R-y`.  The submission explicitly avoids this false equality by saying
that the complete state merely **begins** with the displayed prefix and that
the later blocks partition `R-y+z_(2d)`.

The smallest explicit counterexample is `m=3,d=1`.  With

\[
 L=\{a_1,a_2\},\quad R=\{b_1,b_2\},
\]

choosing `x=a_1,y=b_1` gives the actual partition

\[
 (\{a_2,b_1\},\{a_1\},\{z_1\},\{z_2\},\{b_2\}),
\]

not

\[
 (\{a_2,b_1\},\{a_1\},\{z_1\},\{b_2,z_2\}).
\]

Thus this example is a regression test for the submitted wording, not a
counterexample to it.  The prefix-state statement passes the test.

## 4. Exact refined-state composition

The following is the exact invariant used by the submitted Lemma 1.

### Lemma 4.1 (refined rotor lift)

Let the current abstract state be (1.1).  Suppose the actual complete
last-occurrence partition has the form

\[
 \widehat\Pi=
 (L,\{z_1\},\ldots,\{z_{2d}\},B_1,\ldots,B_s),
 \tag{4.1}
\]

where `(B_1,...,B_s)` is any ordered partition of `R` into nonempty blocks.
For any abstract rotor edge determined by `x in L,y in R`, append the one
set

\[
 X=L-x+y.
\]

Then the actual new partition is

\[
 \begin{split}
 M_X(\widehat\Pi)=(&X,\{x\},\{z_1\},\ldots,\{z_{2d}\},\\
                  &B_1-\{y\},\ldots,B_s-\{y\}),
 \end{split}
 \tag{4.2}
\]

with empty blocks deleted.  Its first `1+2d` blocks are exactly the abstract
successor prefix

\[
 (L-x+y; x,z_1,\ldots,z_{2d-1}),
\]

and the remaining blocks

\[
 \{z_{2d}\},B_1-\{y\},\ldots,B_s-\{y\}
\]

form an ordered partition of `R-y+z_(2d)`.  Hence the invariant (4.1)
holds at the successor.

### Proof

The update set contains all of `L` except `x`, contains exactly the tail
coordinate `y`, and contains none of the displayed `z` coordinates.  Direct
MTF block subtraction is therefore (4.2).  Grouping only for purposes of the
abstract annotation gives the claimed successor sets; no physical blocks
are merged.  QED

Initializing one canonical state makes (4.1) true with `s=1`.  Induction
therefore lifts **every finite abstract rotor path** to a genuine one-entry-
per-edge MTF word.  At every endpoint, the first `1+2d` blocks expose the
entire advertised saturated chain as literal suffix ORs.

This is stronger than repairing individual edges independently: stale
tail blocks can accumulate arbitrarily, and later choices `y in R` may come
from any one of them.  The proof still works because all stale blocks occur
after the useful prefix.

## 5. Consequences for circulation and multicover claims

The abstract rotor graph is `r^2`-regular in and out and strongly connected.
Therefore its complete directed edge set is Eulerian, and it has an Euler
tour visiting every abstract outgoing arc once.  More general rational
circulations can be cleared to integral closed walks in the usual way,
provided their support is connected after zero-flow arcs are removed or
connector circulations are explicitly added.

Lemma 4.1 turns any such finite abstract tour into a genuine OR word after
one initialization.  However, when the abstract tour returns to its initial
state, the actual tail refinement in (4.1) need not return to the initial
single block `R`.  Thus the valid conclusion is

\[
 \boxed{\text{abstract closed circulation }\Longrightarrow
 \text{ one-pass literal MTF multicover},}
\]

not

\[
 \text{abstract closed circulation }\Longrightarrow
 \text{ periodic complete-state MTF orbit}.
\]

If the submitted theorem uses the circulation only to linearly order chain
exposures, its mathematical conclusion survives after this wording change.
If it needs physical state closure in order to concatenate independently
initialized copies without another reset, that step is unsupported.

## Exact wording/caveats

1. The submitted “begins with ...; the remaining blocks partition `R`”
   convention is exactly the correct refined-prefix formulation and needs no
   mathematical repair.
2. Strong connectivity should be stated for `1<=d<=m-2`; handle `d=0`
   separately if it is required.
3. An abstract directed cycle should not be called a closed complete-state
   MTF orbit unless physical closure is separately proved.
4. For a non-full circulation, ensure connected support (or add
   connecting circulation) before invoking one Euler tour.

Subject to these endpoint and terminology caveats, the submitted
strong-connectivity/group-action portion is valid and every abstract rotor
path has a genuine literal MTF realization.
