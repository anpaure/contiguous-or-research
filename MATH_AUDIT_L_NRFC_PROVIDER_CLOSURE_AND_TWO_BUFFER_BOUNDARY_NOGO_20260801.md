# Independent audit: NRFC provider closure and the two-buffer boundary no-go

Date: 2026-08-01  
Audited theorem:
`MATH_THEOREM_L_NRFC_PROVIDER_CLOSURE_CUT_AND_TWO_BUFFER_DEEP_FIBRE_NOGO_20260801.md`  
Audited theorem SHA-256:
`c91e5bfb5eeab002b07f975ba3cb584a75f2746ae67ea8b7d9c8b303755f15e0`  
Status: **PASS WITH THE STATED PROTECTED/PARTIAL SCOPE**.

## 1. Verdict

All four exact rows of the theorem independently check.

1. For integral nonnegative terminal loads, the maximum signed
   provider-closure cut is exactly the number of missing targets.  The
   signs in (1.2)--(1.7) are correct.
2. On the functional private-transfer face, the absorber is exactly one
   integral transshipment problem.  Re-deriving its source--sink cut gives
   (2.3)--(2.4), with the entering capacity
   `c(P-B,B)` and not the reverse orientation.
3. The aggregate vector (3.3) forces at least one core-free top package in
   every canonical package decomposition.  Its deep positive-composition
   words are marginal-tight and therefore raw-rotation closed.  The orbit
   count and the exponential zero-capacity cut family are correct.
4. The primitive-buffer Boolean bank has literal distinct rank-`r` owners
   and distinct old rank-`r-1` q1 colours.  In every relaxed cyclic source
   reassembly, at most `L-d+1` old colours per module can remain.  Hence
   the signed root boundary is at least
   `C(d-1)-B_out-||(sum epsilon)_-||_1`.

The conclusion is deliberately not a no-go for the full unguarded
canonical Ferrers inventory.  The deep-fibre theorem concerns the explicit
aggregate vector (3.3).  The Boolean theorem concerns a protected partial
NRFC bank and explicitly charges every provider imported from outside that
bank to `B_out`.  Those qualifications are mathematically necessary and
are present in the theorem.

## 2. Independent audit of the signed provider cuts

For one protected target `t`, put

```text
m(t)=m_0(t)+sum_e Delta_e(t).
```

Since `m(t)` is a nonnegative integer,

```text
(1-m(t))_+ = 1  iff m(t)=0,
               0  otherwise.
```

For arbitrary real numbers `a_t`, the maximum of `sum_(t in S) a_t` over
all subsets is the sum of their positive parts.  Applying this with
`a_t=1-m(t)` gives

```text
number of holes
 = max_(S subseteq P) [|S|-m_0(S)-sum_e Delta_e(S)].
```

Thus debt at most `H` is equivalent to every displayed expression being at
most `H`, which rearranges exactly to (1.3).  From an exact baseline,
`m_0(S)=|S|`, so the cut is `sum_e Delta_e(S)>=-H`.  If the cocycle sum is
the vector `B`, the exact debt is therefore `max_S(-B(S))`.  There is no
missing positive-part operator: the empty set already contributes zero.

This also audits Corollary 1.2.  A connector loss `-q` on a fixed set and
repair gain at most `g(S)` leaves the cut value at least `q-g(S)`.

## 3. Independent audit of the private-transfer min-cut

After the connector packet, a target `u` has transferable surplus

```text
s(u)=(m(u)-1)_+,
```

and each initial hole needs one unit.  In the network of Theorem 2.1, take
a source-side cut

```text
{sigma} union A,       B=P-A.
```

Its capacity is independently

```text
sum_(u in B) s(u) + c(A,B) + |D intersect A|.
```

Requiring this to be at least `|D|-H` is equivalent to

```text
|D intersect B|
 <= sum_(u in B)s(u) + c(P-B,B) + H.
```

Hence the maximum residual deficiency is

```text
max_(B subseteq P)
  (|D intersect B|-sum_(u in B)s(u)-c(P-B,B))_+,
```

exactly (2.3).  Integral capacities give integral flow.  A flow path can be
serialized from its surplus source toward its hole: each intermediate
target receives a provider before passing one onward, so it never becomes
a new hole.  This proves the converse under the theorem's explicit
serial-composability and private-capacity assumptions.

The scope warning is also correct.  If one choice independently consumes
one shared low socket and one shared high socket, it is a paired hyperedge;
projecting those two resources to unrelated network capacities is unsound.
The `2x2` paired-socket obstruction in the preceding theorem supplies the
minimal witness.

For Proposition 2.2, taking
`S={t_1,...,t_(C-1)}` gives total signed load `-(C-1)`.  Every private
socket and topology row passes, but the exact provider cut forces `C-1`
holes.  This is a valid signed-catalogue counterexample; the theorem does
not mislabel it as a Boolean incidence construction.

## 4. Independent audit of the decomposition-independent deep fibre

Use the theorem's notation

```text
s=r-1-d,
q_0=C(r-2,d),
p_0=C(r-2,d-1).
```

The binomial ratio gives

```text
q_0/p_0=(r-1-d)/d=s/d,
```

so `d q_0=s p_0`; the vector (3.3) is balanced.  It is visibly realized by
`T` copies of `g_(0,r-1)` and `N` copies of
`g_(d-1,d+1)`, and both buffer entries equal the required `Q^circ`.

Only low coordinates `0,d-1` and high coordinates `d+1,r-1` are nonzero.
If a canonical decomposition used no `g_(0,r-1)`, all `p_0 T` top
occurrences would have to come from `g_(d-1,r-1)`.  Directly from the
generator formula,

```text
q_(d-1,r-1)=C(r-d-1,1)=s,
p_(d-1,r-1)=1.
```

It would consume `s p_0 T>N` low-buffer occurrences by the definition of
`T`, a contradiction.  Lemma 3.1 is therefore correct for every canonical
decomposition of the same vector.

The only remaining nontrivial package types are exactly

```text
g_(0,d+1), g_(d-1,d+1), g_(d-1,r-1),
```

besides the forced core-free packages and canonical unit packages.  Each
has equal aggregate age marginals in coordinates `2,...,d`; for
`g_(0,d+1)` this is mobile-coordinate symmetry, and for the other listed
packages it is the singleton tail.  Therefore every selected perfect
assignment is termwise tight in rows `2,...,d-1`.

Fix a word `w=(c_2,...,c_(d-1))` with every entry at least two.  Since
`d>=4`, this word contains at least two entries.  No non-core package can
occur on either shore: `g_(0,d+1)` changes at most one internal one to a
two, and all other eligible packages have an all-one internal word.  The
block is therefore `z` copies of the same finite prefix downset `P_w` on
both shores.  Every matched pair obeys

```text
y_1<=x_0,   y_2<=x_1.
```

The source and target multisets have equal coordinate sums.  Summing each
nonnegative slack forces equality on every edge, even though equal copies
may permute.  The target type is exactly the raw rotation.  Repeating this
argument around a type whose every coordinate is at least two makes each
rotation orbit, with all `z` copies, a closed successor block.

At least one buffer occurrence lies outside those blocks because
`N=Q^circ_(r,d)>0` in the stated range.  Thus there are at least
`kappa_2+1` factor components and no one-cycle assignment.

Finally, subtracting two from each of `d+1` coordinates leaves total
`r-2(d+1)`.  Stars and bars gives

```text
|U_2|=C(r-d-2,d).
```

Every rotation orbit has size at most `d+1`, so the lower bound on
`kappa_2` follows.  At `r=3(d+1)` it becomes
`C(2d+1,d)/(d+1)`, exponential in `d`.  Any proper nonempty union of these
closed blocks is a zero-capacity subtour cut.  The stated
`2^kappa_2-2` is a conservative valid count; the union of the entire deep
bank is also proper because buffer occurrences remain outside it.

## 5. Independent audit of the Boolean run cut

Set `L=2 ceil((d+2)/2)`.  Then `L` is even and `L>d+1`.  In one module,
the alternating `P,H` common-core word has sources

```text
G+z_t       at P,
G+b+z_t     at H.
```

There are no adjacent `P` positions.  The literal common-core construction
therefore supplies the claimed `L`-cycle with `m=L/2` copies of
`g_(d-1,d+1)`.  Every owner is

```text
G+b+{d+1 consecutive tags},
```

and every old lower-q1 colour is

```text
G+b+{d consecutive tags}.
```

Distinct starts give distinct cyclic `d`-subsets because all tags are
distinct and `d<L-1`; different modules have disjoint tag sets.  Thus all
`CL` protected colours initially have load one.

Any literal successor cycle on the retained source occurrences induces a
cyclic order of their source letters.  Relaxing to every cyclic order can
only enlarge the feasible class.  For one module, let the maximal runs of
its tags have lengths `l_i`, summing to `L`.  An old protected colour can
be supplied internally only by a pure length-`d` window, and

```text
sum_i max(0,l_i-d+1) <= L-d+1.
```

If no run has length at least `d`, the left side is zero.  Otherwise, over
the long runs it is at most
`L-|I|(d-1)<=L-d+1`.  One pure window has only one tag set and therefore
can supply at most one old colour.  At least `d-1` old colours per module
are missing.

An outside provider incidence supplies at most one rank-`r-1` colour by
definition.  Charging every non-pure provider to `B_out` gives exactly

```text
h>=C(d-1)-B_out.
```

Since the initial loads are one, terminal holes equal the negative
`l_1` mass of the cumulative signed payload.  If that payload is
`Pi+E`, subadditivity of negative parts yields

```text
||Pi_-||_1
 >= C(d-1)-B_out-||E_-||_1.
```

The sign and the location of the exceptional-error term in (4.13) are
therefore correct.  The `C` modules contribute
`A_(d-1)=A_(d+1)=Cm`; choosing `Cm>=Q^circ` makes the scalar two-buffer
hypotheses hold while the protected boundary remains linear.

## 6. Exact implication boundary

The audit supports precisely the following statement:

> Two-buffer aggregate abundance and signed-payload bookkeeping do not
> imply an `O(1)`-boundary NRFC merge tree.  One additionally needs
> component-spanning off-fibre circuits and a jointly feasible
> provider-recycling expansion row.

It does not support any of the following stronger claims:

* that the actual full Ferrers inventory has the deep closed fibres of
  (3.3);
* that the protected Boolean modules already possess fixed-state
  cross-module connectors;
* that `B_out=O(1)` in an unguarded global Boolean atlas; or
* that the abstract private payloads of Proposition 2.2 are realized by
  incidence circuits.

Those are correctly left open in the audited theorem.
