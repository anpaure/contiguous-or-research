# Component-catalogue width completeness for even equivariant factors

Date: 2026-07-29  
Status: solver-free exact theorem and scope audit.  No spanning-factor
existence claim beyond the stated universal implication; no computation.

## 0. Verdict

Assume `r>=3`; the exceptional case `r=2` has only proper depth one and
needs width two.  There are two different catalogues, and they must not be
conflated.

1. The successor permutation, dart phases, and owner transversal in
   `MATH_THEOREM_AD_EVEN_MULTICOMPONENT_CT_WAKSMAN_NORMAL_FORM_20260729.md`
   are an exact representation of every rotation-equivariant simple
   spanning two-factor.  This factor representation needs no window-width
   catalogue at all.
2. A finite list of contiguous-window widths is a separate *witness
   catalogue*.  For `K=2r`, exact detection of every proper lower and upper
   shadow witnessed anywhere in an arbitrary two-factor is guaranteed by

   \[
      \mathcal H_{\rm safe}(r)=
      \{2,3,\ldots,B_{r,r-1}\},
      \qquad
      B_{r,r-1}=\binom{2r-3}{r-3}+2.
      \tag{0.1}
   \]

   More sharply, depth `q` needs only the widths

   \[
      q+1\le w\le B_{r,q},\qquad
      B_{r,1}=2,qquad
      B_{r,q}=\binom{r+q-2}{q-2}+2\quad(q\ge2).
      \tag{0.2}
   \]

The upper endpoint in (0.2) is sharp among simple Johnson-cycle
components: for every `2<=q<=r-1` there is a simple cycle and a rank
`r+q` target whose only witnessing cyclic interval has width exactly
`B_(r,q)`.  The dual statement holds for rank `r-q` intersections.  Gauge,
cyclic rerooting, and reversal do not change that width.

Consequently no width bound independent of `r` is WLOG for an
*unrestricted component chronology*.  In fact

\[
 B_{r,r-1}
 =\frac{r-2}{4(2r-1)}\binom{2r}{r}+2
 =(1/8+o(1))\binom{2r}{r}.
 \tag{0.3}
\]

There is one important scope boundary.  The sharp examples below are
honest simple Johnson cycles, but this note does not prove that each can be
prescribed as a component of a *spanning rotation-equivariant* two-factor.
Thus (0.1) is an unconditional WLOG upper catalogue for all such factors,
whereas minimality of its endpoint for that narrower spanning-equivariant
class would require an additional equivariant extension theorem.  What is
already ruled out is deriving a bounded-width WLOG claim from the local
factor laws or from gauge alone.  The current fixed six-width `K=16`
catalogue remains only a sufficient subclass.

## 1. Literal intervals and minimal witnesses

Let

\[
 A_0,A_1,\ldots,A_{w-1}
 \tag{1.1}
\]

be a one-pass interval in a simple cycle of `J(2r,r)`.  Thus the `A_i` are
distinct rank-`r` sets and consecutive sets are Johnson neighbours.

It is an **upper depth-`q` witness** for `T`, `|T|=r+q`, when

\[
                  \bigcup_{i=0}^{w-1}A_i=T.
\tag{1.2}
\]

It is a **lower depth-`q` witness** for `L`, `|L|=r-q`, when

\[
                  \bigcap_{i=0}^{w-1}A_i=L.
\tag{1.3}

A witness is minimal when no proper contiguous subinterval is still a
witness for the same target.  Every finite witnessing interval contains a
minimal one, obtained by deleting endpoints while possible.

The one-pass convention matters only when a physical component is shorter
than a requested width.  No interval is allowed to traverse the same
physical state twice.  This agrees with the validity bit (5.6) in the
multi-component normal-form theorem.

## 2. Exact minimal-width theorem

### Theorem 2.1 (minimal shadow-witness bound)

Let (1.1) be a minimal upper or lower depth-`q` witness in a simple
component of a two-factor of `J(2r,r)`.  Then

\[
                    w\ge q+1.
\tag{2.1}
\]

For `q=1`, necessarily `w=2`.  For `q>=2`,

\[
                    w\le
                    \binom{r+q-2}{q-2}+2.
\tag{2.2}

If the physical component has length `P`, the effective upper bound is of
course `min(P,B_(r,q))`.

#### Proof: upper witnesses

Since the union is `T`, every `A_i` is contained in `T`.  Put

\[
                    D_i=T\setminus A_i.
\tag{2.3}
\]

The `D_i` are distinct `q`-subsets of the `(r+q)`-set `T`, and

\[
       \bigcup_i A_i=T\quad\Longleftrightarrow\quad
       \bigcap_i D_i=\varnothing.
\tag{2.4}
\]

Each Johnson step can introduce at most one new member of `T`, so starting
from rank `r` and reaching union-rank `r+q` needs at least `q` steps.  This
proves (2.1).

Minimality after deleting the last or first state gives

\[
 \bigcap_{i=0}^{w-2}D_i\ne\varnothing,
 \qquad
 \bigcap_{i=1}^{w-1}D_i\ne\varnothing.
\tag{2.5}
\]

Choose `x` in the first intersection and `y` in the second.  They are
different, since a common choice would belong to every `D_i`, contradicting
(2.4).  Every internal set `D_i`, `1<=i<=w-2`, contains both `x` and `y`.
There are only

\[
                    \binom{r+q-2}{q-2}
\tag{2.6}
\]

distinct `q`-subsets of `T` containing this pair.  The component is simple,
so its internal `D_i` are distinct.  Hence `w-2` is at most (2.6), proving
(2.2).  For `q=1`, two distinct rank-`r` subsets of an `(r+1)`-set already
have union `T`, so a minimal witness has width two.

#### Proof: lower witnesses

Every `A_i` contains `L`.  Put

\[
                    D_i=A_i\setminus L.
\tag{2.7}
\]

These are distinct `q`-subsets of the `(r+q)`-set `[2r]\setminus L`, and

\[
       \bigcap_i A_i=L\quad\Longleftrightarrow\quad
       \bigcap_i D_i=\varnothing.
\tag{2.8}
\]

The preceding argument now applies verbatim.  QED.

The proof uses only simplicity and literal chronology.  Rotation symmetry,
component voltage, and the choice of quotient section play no role.

### Corollary 2.2 (an unconditional WLOG witness catalogue)

For a fixed proper depth `q`, materializing every valid one-pass width in

\[
             \mathcal H_q(r)=\{q+1,\ldots,B_{r,q}\}
\tag{2.9}
\]

detects every depth-`q` lower intersection and upper union that occurs in
any simple two-factor.  This follows by replacing any witness with an
endpoint-minimal subinterval and applying Theorem 2.1.

The numbers `B_(r,q)` increase with `q`, and the intervals (2.9) overlap.
Therefore, for all nonempty proper lower and upper ranks, their union is
exactly (0.1).  This statement is WLOG for every two-factor, equivariant or
not; it is not an existence statement saying that any such factor has all
the required shadows.

The full upper target `[2r]` is deliberately excluded here.  After a factor
has been opened and spliced into a path containing every middle owner, the
union of that whole path is automatically `[2r]`; it need not consume a
cyclic component-window width.  If one insists on certifying the full target
inside a single pre-splice component, Theorem 2.1 also applies at `q=r` and
gives the safe bound `binom(2r-2,r-2)+2`, but no matching sharp
equivariant-component statement is claimed.

## 3. Sharp simple-component obstruction

The next construction proves that the endpoint in Theorem 2.1 is not an
artifact of its counting proof.

### Lemma 3.1 (fixed-weight Gray path)

For `0<=k<R`, the graph `J(R,k)` has a listing

\[
                 E_1,E_2,\ldots,E_{\binom Rk}
\tag{3.1}
\]

of all `k`-subsets in which consecutive sets differ by one deletion and one
insertion.

#### Proof

Use the reflected recursion

\[
 G(R,k)=G(R-1,k)\ ;\
       \bigl(\operatorname{rev}G(R-1,k-1)\bigr)+\{R\},
\tag{3.2}
\]

with the singleton boundary cases `k=0` and `k=R`.  Inductively the first
set is `{1,...,k}` and the last is `{1,...,k-1,R}`.  The last set of
`G(R-1,k-1)` is contained in the last set of `G(R-1,k)`, so the join in
(3.2) is also one Johnson step.  The two blocks partition the `k`-subsets
according to whether they contain `R`.  QED.

### Theorem 3.2 (sharp unique-width cycle)

For every `2<=q<=r-1`, there is a simple cycle in `J(2r,r)` and an upper
target `T` of rank `r+q` such that the only cyclic interval whose union is
`T` has width

\[
                    B_{r,q}=\binom{r+q-2}{q-2}+2.
\tag{3.3}
\]

There is also a simple cycle and a lower target `L` of rank `r-q` for which
the only interval with intersection `L` has this width.

#### Proof: the upper cycle

Put `R=r+q-2`, `k=q-2`, and write an `(r+q)`-set as

\[
                    T=\{x,y\}\mathbin{\dot\cup}\Omega,
                    \qquad |\Omega|=R.
\tag{3.4}
\]

Take the Gray path `E_1,...,E_s` of Lemma 3.1 on the `k`-subsets of
`Omega`, where `s=binom(R,k)`.  Choose

\[
                 a\in\Omega\setminus E_1,
                 \qquad b\in\Omega\setminus E_s,
\tag{3.5}
\]

which is possible because `k<R`.  Define `q`-subsets of `T` by

\[
 \begin{aligned}
  D_0&=\{x\}\cup E_1\cup\{a\},\\
  D_i&=\{x,y\}\cup E_i &&(1\le i\le s),\\
  D_{s+1}&=\{y\}\cup E_s\cup\{b\}.
 \end{aligned}
\tag{3.6}

Consecutive `D_i` share exactly `q-1` elements.  Hence

\[
                         A_i=T\setminus D_i
\tag{3.7}
\]

is a simple Johnson path of rank-`r` states.  All proper prefixes of the
`D` path have common element `x`, and all proper suffixes have common
element `y`.  The intersection of all internal `D_i` is `{x,y}`, because
the intersection of all `k`-subsets of `Omega` is empty; `D_0` removes `y`
and `D_(s+1)` removes `x`.  Thus the full intersection is empty, while
every proper contiguous subinterval has nonempty intersection.  Equivalently,
the full `A` path, of width `s+2=B_(r,q)`, is the unique interval in this
path with union `T`.

Because `q<=r-1`, choose `w` outside `T`.  Replace one element at each end
state by `w`, and connect the resulting two rank-`r` states by a shortest
Johnson path inside the states containing `w`.  This subgraph is a copy of
`J(2r-1,r-1)` and is connected by replacing unequal elements one at a time.
It closes the displayed path to a simple cycle.  Every closing-path state
contains `w`, so no interval using any closing state can have union `T`.
The asserted uniqueness on the cycle follows.

For the lower construction, start with `|L|=r-q` and put
`A_i=L\cup D_i`, using the same `D` path on `[2r]\setminus L`.  Choose
`ell in L`, choose `w_0 notin A_0` and `w_1 notin A_(s+1)`, and replace
`ell` by `w_0,w_1` at the respective endpoints.  Connect those two endpoint
neighbours through the connected Johnson graph of rank-`r` states omitting
`ell`.  Every closing state omits `ell`, so no interval using the closing
path has intersection exactly `L`.  QED.

For `q=1`, an adjacent Johnson pair gives the sharp width two.  For `q=3`,
the construction is especially transparent: the internal deletion sets
are `{x,y,u_i}` for all `r+1` choices of `u_i`, so the unique witness width
is `r+3`.

### Corollary 3.3 (every depth-three width is individually necessary locally)

Assume `r>=4`.  For every integer

\[
                         4\le h\le r+3,
\tag{3.8}
\]

there is a simple Johnson cycle with an upper depth-three target whose only
witness has width `h`; the same holds for a lower depth-three target.

#### Proof

Put `s=h-2` and choose distinct
`u_1,...,u_s` from an `(r+1)`-set `Omega`.  In (3.6) use

\[
 \begin{aligned}
 D_0&=\{x,u_1,u_2\},\\
 D_i&=\{x,y,u_i\}\quad(1\le i\le s),\\
 D_{s+1}&=\{y,u_s,u_{s-1}\}.
 \end{aligned}
\tag{3.9}
\]

Consecutive triples share two elements.  Every proper prefix has common
element `x`, every proper suffix has common element `y`, and the complete
intersection is empty because `s>=2`.  The closure argument of Theorem 3.2
then applies unchanged.  QED.

Thus a sparse width list cannot be made locally complete merely by choosing
its maximum at least `r+3`: at depth three every omitted integer in this
whole interval has an exact unique-width obstruction.

### Corollary 3.4 (what is and is not disproved)

Any component catalogue that claims to admit arbitrary simple Johnson-cycle
chronologies must admit widths growing with `r`; indeed its maximum width
must be at least `B_(r,q)` if it is to detect every depth-`q` witness in
that component class.  Coordinate relabelling, section gauge, cyclic
rerooting, and reversal preserve interval cardinality, so none turns this
witness into one of a different width.

The construction is not, by itself, an equivariant factor-extension
theorem.  It therefore does not establish that every width endpoint in
(0.1) occurs in some spanning `rho`-equivariant factor.  Claiming that
stronger lower bound would be an overstatement.  Conversely, no bounded
catalogue can be called WLOG merely because all dart voltages have been
normalized or because the local Johnson equations hold: those operations
do not address this exact component obstruction.

## 4. Exact `K=16` calibration

For `K=16`, `r=8`, the proper-depth bounds are

| depth `q` | complete minimal-width interval |
|---:|---:|
| 1 | `2` |
| 2 | `3` |
| 3 | `4,...,11` |
| 4 | `5,...,47` |
| 5 | `6,...,167` |
| 6 | `7,...,497` |
| 7 | `8,...,1289` |

Thus the single common safe catalogue is `2,...,1289`.  At `N=858`, merely
forming one quotient-start word for every width `2,...,1289` gives

\[
                    858\cdot1288=1,105,104
\tag{4.1}
\]

candidate start-width objects before target routing.  This is exact but no
longer the fixed-width near-linear regime.

The current compact upper catalogue is

\[
                         \{2,3,4,6,9,13\}.
\tag{4.2}
\]

It is not the WLOG catalogue furnished by Theorem 2.1.  Already at depth
three, Theorem 3.2 gives a simple component whose sole target witness has
width eleven; extending that interval to width thirteen crosses a state
containing an outside coordinate and contaminates the union.  This does not
make the existing SAT model unsound: its declared scope is exactly the
sufficient subclass in which all needed upper targets have witnesses among
(4.2).  It only forbids upgrading an UNSAT result from that model to an
all-factor theorem.

## 5. Encoding-size consequence

Let `B=B_(r,r-1)`.  The shared-successor construction can generate every
safe width without occurrence-by-target selectors, but it must propagate
`B-1` successor layers or represent the same number of start-width objects.
Using one quotient word per start and width gives `Theta(NB)` actual words.
Since

\[
             N=\frac{W}{2r-1},\qquad
             B=(1/8+o(1))W,
\tag{5.1}
\]

the all-proper-depth safe catalogue has `Theta(W^2/r)` start-width objects.
A grouped Waksman cover has size

\[
                    O\bigl(KNB\log(NB)\bigr),
\tag{5.2}
\]

and separate width networks have the comparable bound
`O(KNB log N)`.  This is still polynomial and selector-free, but it is not
the `O(N log N)` fixed-width catalogue of the current model.

This is not a lower bound against every conceivable SAT or flow encoding.
A different automaton or cut-separation formulation might avoid explicitly
materializing all start-width pairs.  What is proved is the completeness
boundary for a Waksman catalogue indexed by an explicit fixed list of
literal window widths.

## 6. Scope table

| claim | status |
|---|---|
| successor permutation + dart phases represent every equivariant factor | exact WLOG |
| widths `H_q(r)` detect every occurring depth-`q` literal shadow | exact WLOG |
| common widths `2,...,B_(r,r-1)` detect all proper depths | exact WLOG |
| endpoint `B_(r,q)` is sharp for simple Johnson-cycle components | proved |
| gauge can convert an omitted witness width to an admitted width | false |
| current six-width `K=16` catalogue is all-factor WLOG | not proved; only sufficient |
| sharp cycles extend to spanning equivariant factors | open in this note |
| every SAT encoding must explicitly use `Theta(NB)` window variables | not claimed |
