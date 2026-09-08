# Catalan-scale pivot bridges glue a protected trace factor at zero extra length

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact gluing theorem, owner-disjoint pivot-bank
packing theorem, and exact scalar ledger.  A
collection of already literal, owner-disjoint trace components can be joined
into one source word without increasing the target length, provided actual
unused middle owners form explicit pivot geodesics between the prescribed
component endpoint states.  At depth `h=d(k)+1`, the lower-slot slack is
large enough to leave all bridge owners unmarked for the standard Catalan
component counts in both parities.  The complete middle layer contains an
owner-disjoint pivot bank of the required Catalan size.  The theorem does
**not** construct a protected trace factor on its complement or make that
factor expose the bank's endpoint states.

## 1. Trace components and exact owner accounting

Fix a ground set `[k]`, an owner rank `r`, and a trace depth `h<r`, and
assume `k>=r+h`.  Put

\[
                         W={k\choose r}.
\tag{1.1}
\]

An order-`h` trace component is a nonempty source word

\[
                   A=(A_0,\ldots,A_{n+h-1})
\tag{1.2}
\]

whose `n` consecutive length-`h+1` unions are distinct rank-`r` owners.
Its initial and terminal de Bruijn states are

\[
       \operatorname{in}(A)=(A_0,\ldots,A_{h-1}),\qquad
       \operatorname{out}(A)=(A_n,\ldots,A_{n+h-1}).
\tag{1.3}
\]

The component may carry occurrence-labelled strict flags on its owner
windows.  A flag is **literal** when all its members are proper suffix unions
of that exact window.  Different flagged occurrences are required to have
different target values.

We use a deliberately strong upper-protection convention.  A family of
components is **internally upper-complete** if every target `Z` of rank
strictly above `r` is the union of a consecutive interval of owner windows
lying wholly inside one component.  Thus no upper witness relies on a future
component join.

The owners of the components below and the owners of every bridge are
occurrence-labelled subsets of the one rank-`r` layer.  The partition
condition in Theorem 3.1 will require them to be pairwise distinct and to
cover that layer exactly.  Bridge owners therefore replace owners omitted
from the components; they are not additional or repeated owners.

## 2. The explicit pivot bridge

Choose pairwise disjoint objects

\[
 Q,\quad \lambda_1,\ldots,\lambda_h,\quad
       \rho_1,\ldots,\rho_h,
 \qquad |Q|=r-h,
\tag{2.1}
\]

where the displayed Greek symbols are singleton coordinates.  Since
`h<r`, the set `Q` is nonempty.  Define the two order-`h` singleton rail
states

\[
 U=(\{\lambda_1\},\ldots,\{\lambda_h\}),
\tag{2.2}
\]

and

\[
 V=(\{\rho_1\},\ldots,\{\rho_h\}).
\tag{2.3}
\]

Starting from state `U`, append the `h+1` letters

\[
                       Q,V_1,V_2,\ldots,V_h.
\tag{2.4}
\]

### Lemma 2.1 (rank-flat pivot reset with a complete strict suffix deck)

The `h+1` owner windows traversed in (2.4) are

\[
 M_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
          \cup\{\rho_1,\ldots,\rho_j\},
             \qquad 0\le j\le h,                  
\tag{2.5}
\]

with empty index ranges omitted.  They are distinct rank-`r` sets and form
the Johnson geodesic

\[
                    M_j-M_{j+1}=\{\lambda_{j+1}\},
 \qquad M_{j+1}-M_j=\{\rho_{j+1}\}.
\tag{2.6}
\]

The final de Bruijn state is exactly `V`.  Every source letter in the bridge
is nonempty.  Moreover, all `h(h+1)` proper suffix unions of these `h+1`
owner windows are strict subsets of rank below `r`, and they are pairwise
distinct.

#### Proof

For `j=0`, the window is `U_1,...,U_h,Q`.  Its union is `M_0`.
After `j` further shifts, the surviving old letters are
`U_(j+1),...,U_h`, while the appended letters are
`Q,V_1,...,V_j`.  Their union is (2.5): the old tail contributes the
displayed lambda labels and the new prefix contributes `Q` and the rho
labels.  Equation (2.1) gives

\[
                         |M_j|=(r-h)+(h-j)+j=r.
\]

Equation (2.6) proves distinctness and Johnson adjacency.  After all `h+1`
appends, the initial state and `Q` have shifted out, leaving precisely
`V_1,...,V_h`.  Nonemptiness is immediate from (2.1)--(2.4).

It remains to inspect the proper suffixes.  The literal owner window for
`M_j` is

\[
 (\{\lambda_{j+1}\},\ldots,\{\lambda_h\},Q,
                   \{\rho_1\},\ldots,\{\rho_j\}).
\tag{2.7}
\]

Its suffixes of lengths `1,...,j` are the nonempty consecutive rho
intervals

\[
             \{\rho_{j-\ell+1},\ldots,\rho_j\},
                       \qquad 1\le \ell\le j,
\tag{2.8}
\]

and its suffixes of lengths `j+1,...,h` are

\[
 Q\cup\{\rho_1,\ldots,\rho_j\}
   \cup\{\lambda_{h-\ell+j+2},\ldots,\lambda_h\},
                       \qquad j+1\le \ell\le h,
\tag{2.9}
\]

with the last lambda range empty when `ell=j+1`.  Values in (2.8) do not
contain `Q`, whereas every value in (2.9) does.  Within (2.8), the terminal
rho index and the interval length recover `(j,ell)`.  Within (2.9), the rho
prefix recovers `j` and the lambda-tail length recovers `ell`.  Hence all
the values are pairwise distinct.  Their ranks are respectively `ell` and
`r-h+ell-1`, at most `h` and `r-1`; because `Q` is nonempty, no value has
rank `r`.  Thus every one is strict. `square`

We call the owner set

\[
                         \mathcal M(Q,\lambda,\rho)
                            =\{M_0,\ldots,M_h\}
\tag{2.10}
\]

a pivot bridge bank.  Notice that one bridge consumes exactly `h+1` actual
owner colours.  The bridge is not a collection of free, uncounted reset
letters.

### Theorem 2.2 (unconditional owner-disjoint pivot-bank packing)

Let `s=h+1`.  The rank-`r` layer contains a family of at least

\[
                         {W\over s^2}               
\tag{2.11}
\]

pairwise owner-disjoint pivot bridge banks (2.10), with the integer meaning
that the family size is at least the ceiling of the displayed real lower
bound.

#### Proof

Make a simple `s`-uniform hypergraph whose vertices are the rank-`r` sets
and whose hyperedges are all distinct owner sets (2.10) obtained from all
choices in (2.1).  The symmetric group on `[k]` acts transitively on the
vertex set and preserves this hypergraph.  Hence it is regular; write its
common vertex degree as `Delta`.  Double-counting vertex--edge incidences
gives

\[
                         s|E|=W\Delta.              
\tag{2.12}
\]

Take a maximal hypergraph matching of size `m`.  Every hyperedge meets a
selected hyperedge.  The union of the stars of the `s` vertices in one
selected edge contains at most `s Delta` hyperedges.  Therefore

\[
                 |E|\le m s\Delta,
 \qquad
                 m\ge {|E|\over s\Delta}={W\over s^2},
\tag{2.13}
\]

as claimed. `square`

Theorem 2.2 is deliberately prospective.  It permits reserving a disjoint
bridge bank before the trace components are built.  It does not say that a
separately constructed factor avoids that bank or has its literal endpoint
states.

## 3. Exact zero-length factor gluing

### Theorem 3.1 (protected trace-factor gluing)

Let `A^(1),...,A^(c)` be order-`h` trace components, in the order in which
they are to be joined.  For every `1<=j<c`, let `B^(j)` be a pivot bridge of
Section 2 with initial state `U^(j)` and terminal state `V^(j)`.  Assume:

1. **endpoint fit**

   \[
      \operatorname{out}(A^{(j)})=U^{(j)},\qquad
      \operatorname{in}(A^{(j+1)})=V^{(j)};
   \tag{3.1}
   \]

2. **owner partition:** every component owner and every owner in every
   bridge bank is distinct, and together they are exactly

   \[
                              {[k]\choose r};
   \tag{3.2}
   \]

3. **lower protection:** the literal flags carried by component and bridge
   windows are target-disjoint and together contain every nonempty target
   of rank below `r`; bridge windows are allowed to carry no flag;

4. **upper protection:** the components are internally upper-complete.

Then there is one universal source word of length

\[
                              W+h.                  
\tag{3.3}
\]

Its consecutive length-`h+1` owner windows list every rank-`r` set exactly
once, and it retains every declared lower and upper witness.

#### Proof

Write the initial `h` letters of `A^(1)`.  Append the remaining letters of
`A^(1)`.  Its terminal state is `U^(1)`, so append the bridge extension
`Q^(1),V_1^(1),...,V_h^(1)` from (2.4).  Lemma 2.1 ends at state `V^(1)`,
which is the initial state of `A^(2)` by (3.1); append only the letters of
`A^(2)` after that initial state.  Continue in this way.

Every appended letter is nonempty.  The consecutive owner windows are, in
order, the component owners and the bridge owners.  By (3.2) their number is
`W` and they list the rank-`r` layer exactly once.  A word with `W` order-`h`
arcs has `W+h` letters, proving (3.3).

No component letter or component window is changed.  Hence every literal
component suffix flag in item 3 survives at the same relative occurrence.
Every bridge suffix flag is literal in the appended bridge itself, so it
also survives.  This covers the strict lower ideal.  For an upper target
`Z`, item 4 gives a consecutive owner interval `[a,b]` inside one component
with

\[
                              Z=\bigcup_{i=a}^{b}T_i.
\]

The component remains a contiguous block in the joined owner order.  If its
source-window start is `p`, associativity gives

\[
    \bigcup_{i=a}^{b}T_i
      =\bigcup_{q=p+a}^{p+b+h}A_q,
\tag{3.4}
\]

so the same upper witness survives.  The middle layer is covered by the
owner windows themselves.  Thus the joined word is universal. `square`

### Corollary 3.2 (the joint quantifier can be weakened to a factor)

The single-path target

\[
 \exists P,\mathcal C:\quad L(P,\mathcal C)
                       \text{ has one source--sink path}
\tag{3.5}
\]

may be replaced by the following sufficient target:

* construct an internally upper-complete, literal named trace factor;
* protect rail endpoints on its components;
* select pairwise owner-disjoint pivot bridge banks from the owners omitted
  by the factor; and
* require the factor owners and bridge owners to partition the middle layer.

Theorem 3.1 then supplies the single layered path.  No extra source position
is appended.  What remains is a correlated protected-factor/bridge matching
problem, rather than a demand that the unglued object already be connected.

## 4. Exact lower-slot charge

Put

\[
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},\qquad
 d=d(k)=\min\left\{q:qW+{q+1\choose2}\ge\Lambda\right\},
 \qquad h=d+1.                                      
\tag{4.1}
\]

There are `h` proper suffix addresses on every owner window.  In this
section we deliberately use only those owner-ending suffix addresses and
discard the additional triangular bank at the initial boundary of the
source word.  If every bridge owner is left completely unflagged, then
`c-1` bridges remove

\[
                         h(h+1)(c-1)                
\tag{4.2}

potential lower marks from this owner-suffix bank.  The exact raw-capacity
condition for all `Lambda` lower targets to fit in the *remaining
owner-suffix addresses* is

\[
                  h(h+1)(c-1)\le hW-\Lambda.
\tag{4.3}

For the full word this is a deliberately stronger sufficient condition,
not a necessary condition, because the discarded initial triangular cells
could also carry lower targets.  In either interpretation it is only a
scalar statement; it is not a named chainization or trace existence
theorem.

The definition of `d` gives the uniform lower bound

\[
 hW-\Lambda
   =W+dW-\Lambda
   \ge W-{h\choose2}.                               
\tag{4.4}

Hence the simple sufficient component bound is

\[
 c\le 1+\left\lfloor
       {W-{h\choose2}\over h(h+1)}\right\rfloor.
\tag{4.5}

Since

\[
                         d(k)=\sqrt{\pi k/8}+O(1),
\tag{4.6}

for either parity, with `k=2r+O(1)`, the right side of (4.5) is

\[
                 \left({4\over\pi}+o(1)\right){W\over r}.
\tag{4.7}

Thus the zero-length bridge mechanism has precisely Catalan-scale component
capacity.

## 5. The standard Catalan counts fit in both parities

### Corollary 5.1 (even central Catalan scale)

For `k=2r`, the standard central Catalan component count is

\[
                         C_{\rm ev}={W\over r+1}.
\tag{5.1}

For all sufficiently large `r`, leaving every owner of `C_ev-1` pivot
bridges unflagged satisfies (4.3).

#### Proof

The left side of (4.3), divided by `W`, is at most

\[
                  {h(h+1)\over r+1}
                    ={\pi\over4}+o(1),             
\tag{5.2}

by (4.6).  Equation (4.4), divided by `W`, is `1-o(1)`, because
`h=O(sqrt(r))` while `W` is exponential in `r`.  Since `pi/4<1`, (4.3)
holds for all sufficiently large `r`. `square`

### Corollary 5.2 (odd middle-levels Catalan scale)

For `k=2r-1`, the standard plane-tree cycle-factor count is

\[
 C_{\rm odd}=\operatorname{Cat}_{r-1}
      ={1\over r}{2r-2\choose r-1}
      ={W\over 2r-1}.                               
\tag{5.3}

For all sufficiently large `r`, leaving every owner of `C_odd-1` pivot
bridges unflagged satisfies (4.3).

#### Proof

Now the normalized bridge charge is at most

\[
                 {h(h+1)\over2r-1}
                    ={\pi\over8}+o(1)<1,            
\tag{5.4}

while (4.4) again supplies normalized slack `1-o(1)`. `square`

The two corollaries are scalar statements only.  In particular, a standard
Catalan factor does not automatically expose the rail endpoint states, carry
the completed MLD flags, preserve all-width upper witnesses internally, or
leave an owner set which decomposes into the required pivot geodesics.

### Corollary 5.3 (the isolated Catalan bridge bank exists)

For all sufficiently large `r`, Theorem 2.2 supplies at least `C_ev-1`
pairwise owner-disjoint pivot banks when `k=2r`, and at least `C_odd-1`
when `k=2r-1`.

#### Proof

Here `s=h+1=d(k)+2` and

\[
                         {s^2\over r}\longrightarrow{\pi\over4}.
\]

Thus eventually `s^2<=r+1`, so `W/s^2>=W/(r+1)=C_ev` in the even case.
In the odd case eventually `s^2<=2r-1`, so
`W/s^2>=W/(2r-1)=C_odd`.  Apply Theorem 2.2. `square`

This closes owner-disjoint bridge supply **before conditioning**.  The
unproved correlation is that the complementary owner set must carry the
protected trace factor with exactly the rail endpoints exported by the
selected banks.

## 6. The sharpened existence theorem

The remaining protected-serialization theorem can now be weakened from a
single connected trace object to the following.

> **Protected Catalan trace-factor and pivot-bank theorem.**  At depth
> `h=d(k)+1`, construct at most the parity-appropriate Catalan number of
> literal trace components such that:
>
> 1. their flagged windows realize the completed residual MLD forest and
>    the separately priced boundary bank;
> 2. every upper target has an internal component witness;
> 3. their ordered endpoints are the rail states (2.2)--(2.3); and
> 4. the omitted rank-`r` owners are exactly pairwise owner-disjoint pivot
>    banks (2.7).

Theorem 3.1 then gives a word of length `W+h=B(k)+1`.  Corollaries 5.1--5.2
show that leaving the bridge owners completely unflagged has enough raw
lower capacity in both parities.  Therefore neither component count nor
reset distance creates an additional asymptotic scalar charge at `B+1`.

The unresolved content is joint incidence: the component flags, upper
witnesses, endpoint states, and the prospectively reservable bridge owners
must coexist.  Theorem 2.2 proves that many owner-disjoint pivot geodesics
exist in isolation.  Separate existence of that bank, a Catalan factor, and
an MLD collar forest does not prove their intersection.

## 7. Scope

This note proves:

1. an explicit `h+1`-owner rank-flat bridge between two protected rail
   states;
2. an unconditional owner-disjoint packing of at least `W/(h+1)^2` such
   bridge banks;
3. exact no-extra-length gluing of any owner-partitioning protected trace
   factor carrying those endpoints;
4. preservation of all lower flags and every internally protected upper
   witness; and
5. an exact lower-slot ledger showing that the standard Catalan component
   counts are affordable at `B+1` in both parities.

It proves no protected factor on the complement of the reserved bank, no
endpoint-compatible correlation between factor and bank, no
carrier-conditioned MLD theorem, no all-price configuration inequality, and
no `B(k)+1`, `B(k)+O(1)`, or exact all-`k` theorem.
