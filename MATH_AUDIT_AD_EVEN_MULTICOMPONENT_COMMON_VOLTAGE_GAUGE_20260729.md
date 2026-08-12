# Common voltage gauges for even equivariant multi-component factors

Date: 2026-07-29  
Status: solver-free exact audit.  No existence or nonexistence claim for a
new carrier is made.

## 1. Scope and verdict

Let `k=2r`, put `n=k-1=2r-1`, let the old coordinates be
`X=Z_n`, and write `rho(x)=x+1`.  The cyclic action on both old middle
layers, of ranks `r` and `r-1`, is free because

\[
 \gcd(n,r)=\gcd(n,r-1)=1.
\tag{1.1}
\]

For **one** quotient circuit of unit voltage, multiplication of every old
coordinate label by the inverse voltage reduces the voltage to one.  This is
a valid without-loss reduction whenever the construction class is closed
under that global coordinate permutation.

For several quotient components, the corresponding assertion is false.
There is only one global multiplier.  It scales all component voltages by
the same unit and cannot erase their relative voltages.  Changing quotient
representatives does not help: that is a coboundary gauge and leaves every
circuit voltage unchanged.

Thus a multi-component model that requires voltage one on every component
is a sufficient subclass.  It is without loss only under the additional
relative-voltage hypothesis proved in Theorem 4.1 below.

## 2. The three operations that must not be conflated

Fix a section choosing one physical representative over each quotient
vertex.  Give a directed quotient edge `e:u->w` its voltage
`nu(e) in Z_n`.  For an oriented quotient circuit `C`, put

\[
                         v(C)=\sum_{e\in C}\nu(e)\pmod n.
\tag{2.1}
\]

There are three distinct transformations.

1. **Section gauge.**  Replacing the representative at `u` by its translate
   through `a(u)` changes

   \[
       \nu(u,w)\longmapsto \nu(u,w)+a(u)-a(w).
   \tag{2.2}
   \]

   The added terms telescope, so every `v(C)` is unchanged.

2. **One global normalizer automorphism.**  For `q in U(n)`, relabel every
   old coordinate by

   \[
                           \phi_q(x)=qx.
   \tag{2.3}
   \]

   Since `phi_q rho^p phi_q^{-1}=rho^{qp}`, every component voltage changes
   simultaneously by

   \[
                           v(C)\longmapsto qv(C).
   \tag{2.4}
   \]

   A further affine translation `x->qx+b` has the same multiplier `q`; the
   translation part does not create an independent component gauge.

3. **Circuit reversal.**  If the carrier is undirected and the chronology
   of a component may be reversed, then reversing `C` changes `v(C)` to
   `-v(C)`.  This sign may be chosen independently for different undirected
   components.  A directed catalogue does not receive this freedom unless
   the reversed arcs are also admitted.

Only operation 2 can turn a non-one unit voltage into one, and operation 2
is global, not componentwise.

## 3. Exact common-gauge criterion for arbitrary voltages

The following theorem also covers nonunits and zero voltage.

### Theorem 3.1 (common cyclic gauge)

Let

\[
                    v=(v_1,\ldots,v_c),\qquad
                    w=(w_1,\ldots,w_c)\in(\mathbb Z_n)^c
\]

be oriented component-voltage vectors.  A single global coordinate
automorphism sends `v` to `w` if and only if there is one
`q in U(n)` such that

\[
                              w_i=qv_i\pmod n
                    \qquad(1\le i\le c).
\tag{3.1}
\]

This admits the following explicit prime-power test.  For each
`p^a || n`, put

\[
 b_i=\min\{v_p(v_i),a\},\qquad
 b'_i=\min\{v_p(w_i),a\},
\tag{3.2}
\]

where `b_i=a` means `v_i=0 mod p^a`.  It is necessary and sufficient that:

1. `b_i=b'_i` for every `i`; and
2. whenever `b_i<a`, the unit residues

   \[
    R_i=\frac{w_i/p^{b_i}}{v_i/p^{b_i}}
          \pmod {p^{a-b_i}}
   \tag{3.3}
   \]

   obey

   \[
       R_i\equiv R_j
       \pmod {p^{\min(a-b_i,a-b_j)}}
   \tag{3.4}
   \]

   for every pair with `b_i,b_j<a`.

For undirected independently reversible components, the criterion is that
there exist signs `epsilon_i in {+1,-1}` for which Theorem 3.1 holds after
replacing `v_i` by `epsilon_i v_i`.

#### Proof

Equation (3.1) is exactly (2.4), so it remains only to prove the explicit
test.  Work modulo one `p^a`.  Multiplication by a unit preserves every
truncated valuation, proving condition 1.  After division by `p^{b_i}`,
the equation `w_i=qv_i mod p^a` is equivalent to

\[
                         q\equiv R_i\pmod {p^{a-b_i}}.
\tag{3.5}
\]

Congruences whose moduli are powers of the same prime have a simultaneous
solution precisely when each pair agrees modulo the smaller modulus; this
is (3.4).  Every `R_i` is a unit, so the common residue lifts to a unit
modulo `p^a`.  The Chinese remainder theorem then joins the choices over
the distinct prime powers dividing `n`.  The signed assertion follows by
applying the oriented result after the reversals.  \(\square\)

### Corollary 3.2 (single-component canonical forms)

The orbit of `v in Z_n` under global unit multiplication consists exactly
of the residues `w` satisfying

\[
                              \gcd(n,w)=\gcd(n,v).
\tag{3.6}
\]

In particular, a voltage is individually reducible to one if and only if it
is a unit.  Zero voltage is fixed by every multiplier.

This is a one-component statement.  Applying it independently to several
components is not a global coordinate relabelling.

## 4. Exact unit-voltage specialization

### Theorem 4.1 (simultaneous unit-one criterion)

Suppose all `v_i` are units modulo `n`.

* With fixed circuit orientations, one global relabelling makes every
  component voltage one if and only if

  \[
                             v_1=v_2=\cdots=v_c.
  \tag{4.1}
  \]

* If the components may be reversed independently, one global relabelling
  and those reversals make every component voltage one if and only if there
  is one `v in U(n)` such that

  \[
                             v_i\in\{v,-v\}
                       \qquad(1\le i\le c).
  \tag{4.2}
  \]

#### Proof

In the directed case, `qv_i=1` for all `i` holds precisely when all `v_i`
equal `q^{-1}`.  With reversals it becomes
`q epsilon_i v_i=1`, which is equivalent to (4.2).  \(\square\)

Consequently one may normalize a distinguished oriented component to
voltage one, after which the exact surviving invariants are

\[
                         v_i v_1^{-1}\in U(n),
                         \qquad 2\le i\le c.
\tag{4.3}

With independent reversals, these are retained modulo sign.  For labelled
components, the number of directed common-gauge classes of all-unit voltage
vectors is exactly

\[
                              \varphi(n)^{c-1}.
\tag{4.4}

For odd `n>1`, quotienting also by independent component reversals leaves

\[
                         \left(\frac{\varphi(n)}2\right)^{c-1}
\tag{4.5}

classes.  These counts show exactly what an all-components-voltage-one
ansatz discards.

## 5. Smallest even-dimensional counterexample

The failure is already realized by an exact rotation-equivariant middle
factor at `k=6`.  Here `n=5`, `X=Z_5`, and the middle rank is three.  There
are two old rank-two owner orbits and two old rank-three owner orbits.

On the `z` shore select the two quotient loops represented by

\[
 \{0,1\}\longrightarrow\rho\{0,1\}=\{1,2\},
 \qquad
 \{0,2\}\longrightarrow\rho^2\{0,2\}=\{2,4\}.
\tag{5.1}
\]

On the no-`z` shore select their old-coordinate complements.  Every displayed
transition is a Johnson edge.  The four quotient loops cover all four owner
orbits, so their lifts form a rotation-equivariant 2-factor of all twenty
middle vertices.  Their voltages are

\[
                                (1,2,1,2)\pmod5.
\tag{5.2}

Each voltage is a unit, and each quotient loop lifts to one physical
five-cycle.  Nevertheless no common multiplier, even with independent
reversal, makes all four voltages one: the two sign classes are

\[
                       \{1,-1\}=\{1,4\},\qquad
                       \{2,-2\}=\{2,3\}.
\tag{5.3}

They are disjoint.  This is the smallest possible even dimension for this
obstruction: for `k=4`, `n=3` and `U(3)={+1,-1}`, so there is only one unit
class modulo reversal.

The example is a factor, not a Hamilton cycle.  That is exactly the relevant
distinction: a physical Hamilton lift already forces one quotient component,
whereas a multi-component normal form must retain the relative-voltage data.

## 6. Physical lift census, including zero voltage

### Theorem 6.1 (multi-component lift formula)

Let the quotient factor have disjoint directed circuits `C_i` of lengths
`ell_i` and voltages `v_i`.  Because the even middle action is free, its
physical lift has

\[
                      \boxed{\sum_{i=1}^c\gcd(n,v_i)}
\tag{6.1}

components.  Component `C_i` contributes exactly `g_i=gcd(n,v_i)` physical
cycles, each of length

\[
                              \frac{n\ell_i}{g_i}.
\tag{6.2}

Here `gcd(n,0)=n`: a zero-voltage quotient circuit produces `n` physical
cycles, each of the original quotient length `ell_i`.

#### Proof

After one traversal of `C_i`, the phase changes by `v_i`.  Translation by
`v_i` on `Z_n` has `g_i` orbits, each of size `n/g_i`.  Following one phase
orbit traverses `C_i` exactly `n/g_i` times, giving (6.2).  Different
quotient circuits have disjoint vertex supports and therefore their lifted
cycles cannot join.  Summing `g_i` gives (6.1).  \(\square\)

Thus:

* a unit voltage gives one lift of that quotient component;
* a nonunit voltage gives more than one lift;
* zero voltage gives the maximum `n` lifts; and
* one physical Hamilton middle cycle is equivalent to one quotient circuit
  through every quotient owner and unit total voltage.

The last equivalence uses freeness of the two even middle shores.  It should
not be exported without adjustment to quotient layers with nontrivial
stabilizers.

As an exact retained-data check, the symmetrized `k=16` factor recorded in
`MATH_AUDIT_K16_CT_RECONCILIATION_AND_QUOTIENT_FACTOR_20260729.md` has

\[
 (\ell_i,v_i)=(415,2),(7,12),(4,9),(3,13)\pmod {15}.
\]

Formula (6.1) gives `1+3+3+1=8` physical components, and (6.2) gives

\[
                  6225,\quad 35^3,\quad20^3,\quad45,
\]

exactly its independently reported physical length multiset.  In particular,
the two nonunit voltages `12` and `9` cannot be repaired by any gauge.

## 7. Consequences for compact and Waksman encodings

There are two separate scope issues.

### 7.1 What is genuinely without loss

For a single quotient circuit, fixing its unit voltage to one is without
loss at the Boolean-cube theorem level.  Inside a restricted catalogue it
is without loss only if that catalogue is closed under every required
global multiplier `x->qx`.  A fixed skeleton, pinned token labelling, or
truncated catalogue needs an explicit closure proof or a shared frame
variable.

For `c>1`, global closure permits normalization of one distinguished unit
component only.  Requiring all component voltages to one remains a
sufficient subclass unless (4.1), or (4.2) when reversal is legal, is proved
from other constraints.

### 7.2 Exact size needed to retain arbitrary component voltages

Assume the component decomposition is already represented and each selected
directed edge has a known residue `p_e`.  For component `i`, retain an
integer voltage `V_i in {0,...,n-1}` and impose

\[
               \sum_{e\in C_i}p_e=V_i+nH_i.
\tag{7.1}

Allowed-residue tables then enforce `gcd(n,V_i)=g_i`; the table has
`phi(n/g_i)` residues when `g_i|n`, with the singleton `V_i=0` when
`g_i=n`.  In particular, arbitrary unit voltage needs `phi(n)` allowed
residues per component.  This uses

\[
             O(c\log n)\text{ Boolean information and }
             O(c\varphi(n))\text{ explicit table entries},
\tag{7.2}

not a Cartesian enumeration of `phi(n)^c` voltage vectors and not a
position-by-voltage selector family.  Equivalently, normalize `V_1=1` and
retain the `c-1` relative residues (4.3).

Conversely, (4.4) is an information lower bound: an exact directed
all-unit encoding modulo common gauge must distinguish
`phi(n)^(c-1)` cases and hence retain at least

\[
                         (c-1)\log_2\varphi(n)
\tag{7.3}
\]

bits of relative-voltage information.  With independently reversible
components and odd `n>1`, the corresponding lower bound is
`(c-1) log_2(phi(n)/2)`.  Thus no valid normalization can collapse the
multi-component voltage state to one constant-size global selector, while
an exponential one-hot enumeration is also unnecessary.

This does **not** solve the separate task of discovering the circuit
decomposition.  If component membership is unknown, connectivity labels,
subtour machinery, or a component-routing network is still required.  Nor
does it justify independently normalizing components: component-local
multipliers alter owner-orbit identities and must be accompanied by the
global all-different/coverage constraints.  A Waksman network can carry
those frame residues compactly if its token action is symbolic; a catalogue
that pre-expands every framed permutation may still suffer selector blowup.

## 8. Correct replacement wording

The safe statements are:

> Any **single** unit-voltage equivariant quotient circuit can be put in
> voltage-one form by one global multiplication of old coordinate labels,
> provided the admitted construction class is closed under that relabelling.

and

> For several quotient components, one may normalize one distinguished unit
> voltage.  All remaining relative voltages must be retained.  Simultaneous
> voltage one is without loss only when the oriented voltages are equal, or
> equal up to independently legal component reversals.

Anything stronger conflates a global coordinate automorphism with an
inadmissible componentwise relabelling.
