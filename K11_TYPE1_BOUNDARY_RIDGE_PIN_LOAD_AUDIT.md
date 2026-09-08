# Independent audit: Type-I boundary-ridge pin load

## Verdict

**PASS as a theorem and as an incremental circuit design.**  In every exact
Type-I `k=11,n=465` word, every four-set `Q` has at least ten positions in
the rank-at-most-four core whose entries are proper subsets of `Q`.
Consequently all fifteen ridges `63\{b,c}` satisfy the proposed rows.

Assuming reuse of the already constructed facet literals, the fifteen exact
counts require exactly

```text
20,760 variables / 124,470 clauses.
```

There are two scope qualifications, neither of which changes the theorem or
inventory.

1. The production facet plan currently constructs its `y[b,i]` variables
   locally.  A ridge implementation must retain/expose those variable
   references.  This is a zero-CNF bookkeeping change, not a new support
   bank.
2. The checker's separating multiset proves separation from the listed
   projected rank/support/facet/onion/lex summaries, with a separately
   feasible width profile.  It is not one assignment satisfying the full
   interval-witness CNF and therefore is not a proof of logical independence
   from the base CNF.  The theorem note correctly says that the base CNF
   already implies the ridge rows.

No solver source was edited in this audit.

## 1. Exact Type-I dependency

The independently audited Type-I filtration gives

```text
A = 63 || P_5 || C_4 || Q_5.
```

Let `z=|P_5|+|Q_5|`.  The suffix has length 464, so

```text
|C_4| = 464-z,
q = 462-z = |C_4|-2
```

rank-five masks are nonliteral.  Their witnesses cannot contain a different
literal rank-five boundary entry: containment between two rank-five masks
would force equality.  Hence one may choose all `q` witnesses wholly inside
`C_4`.

Locally index the core by `1,...,q+2` and order those incomparable witnesses
by left endpoint.  Their right endpoints have the same strict order and the
standard endpoint-slack normal form gives

```text
I_i subseteq [i,i+2].
```

Thus every core interval `[a,b]` of length at least three contains the
selected witness `I_a`; more generally it contains the distinct selected
witnesses `I_a,...,I_(b-2)`.  The endpoint case is safe because
`b<=q+2` implies `b-2<=q`.

The same Type-I deletion argument says that `C_4` itself covers every
nonempty mask of rank at most four.  These are exactly the two structural
facts needed by the ridge theorem.  Residual lex, named-cell Hall, the
rank-seven moment, and the prefix-chain cut are not mathematical
prerequisites.

## 2. Strict support versus total support

Fix a four-set `Q` and mark a core position exactly when its entry is a
proper subset of `Q`.

A marked run cannot have length three.  Such a triple would have OR
contained in `Q`, but Section 1 places a selected rank-five witness inside
it.  A rank-five value cannot be contained in a four-set.  Therefore every
marked run has length one or two.

Every one of the fourteen nonempty proper subsets `S` of `Q` has a witness
inside `C_4`.  Every entry of that witness is contained in `S`, so every
position of the witness is marked.  Hence the witness lies in one marked
run and has length at most two.

If there are `p` marked positions in `rho` runs, the number of available
singleton and adjacent-pair cells is exactly

```text
2p-rho.
```

Since every run has length at most two,

```text
rho >= ceil(p/2),
2p-rho <= p+floor(p/2).
```

For `p<=9` the latter quantity is at most thirteen.  Fourteen different OR
targets require fourteen different physical intervals, so `p>=10`.
Runs touching either endpoint of `C_4`, repeated literal values, and a
literal occurrence of `Q` create no exception to this argument.

If

```text
p_Q^C = #{i in C_4:A[i] subseteq Q},
m_Q^C = #{i in C_4:A[i]=Q},
s_Q^C = #{i in C_4:A[i] proper-subset Q},
```

then a contained core entry is either proper or equal to `Q`.  Consequently

```text
p_Q^C=s_Q^C+m_Q^C
```

and the strict theorem is exactly

```text
p_Q^C >= 10+m_Q^C.
```

This confirms that copies of the literal ridge cannot pay its proper-support
load.  Omitting `!rank4[i]` from the proposed circuit would be unsound.

The two ten-position gadgets in the checker are also valid.  Five separated
two-position runs provide fifteen singleton/pair cells.  The first gadget
covers all fourteen proper masks (with one repeated value); the second
covers all fifteen nonempty masks.  Thus neither the elementary capacity
argument nor the additional assumption that `Q` is nonliteral raises the
threshold above ten.

## 3. Endpoint ridges and aggregate identity

For `T=63`, the sets

```text
Q_bc=T\{b,c},  0<=b<c<6,
```

are fifteen ordinary four-sets, so the pointwise theorem applies to every
one of them.

An entry `A subseteq T` of rank `s<=3` is a proper subset of exactly

```text
C(6-s,2)
```

of these ridges: choose the two deleted coordinates from `T\A`.  Rank-four
entries are equal to the unique ridge containing them and are deliberately
not counted.  Summing the fifteen rows therefore gives exactly

```text
sum_(i in C_4, A[i] subseteq T, |A[i]|<=3)
    C(6-|A[i]|,2) >= 150.
```

The pointwise rows are stronger than this aggregate moment.

## 4. Exact gate semantics

The deployed facet module defines

```text
y[b,i] <-> [i in C_4 and A[i] subseteq T\{b}].
```

For `b<c`, the proposed gate is

```text
z[b,c,i] <-> y[b,i] AND !A[i,c] AND !rank4[i].
```

The first two conditions put `A[i]` inside `T\{b,c}`.  Type I caps suffix
rank at five, `y` excludes rank five and identifies the low core, and the
exact local-density one-hot flag makes `!rank4` equivalent here to rank at
most three.  Thus `z` is true exactly for a proper-subset ridge support.
Conversely every strict ridge support satisfies all three literals.  Using
`y[b]` rather than `y[c]` is asymmetric syntactically but not semantically.

The four clauses checked in the finite script are the exact bidirectional
CNF for this three-input conjunction.

The natural production dependency is ridge guard implies facet guard.  The
facet guard already requires Type I and the retained subcube row; Type I in
turn requires the exact local-density rank flags.  Listing Type I and local
density again is harmless but logically redundant after the facet guard is
validated.

## 5. Independent inventory reconstruction

There are

```text
15*464 = 6,960
```

strict-support gates.  They cost one variable and four clauses each:

```text
6,960 variables / 27,840 clauses.
```

The production Wallace convention compresses 464 equal-weight inputs with
452 full adders.  Its two residual rows occupy eight bit positions, and the
exact ripple addition uses eight further full adders while retaining the
final carry.  Hence one counter uses

```text
460 full adders = 920 variables / 6,440 clauses.
```

Fifteen counters use

```text
13,800 variables / 96,600 clauses.
```

The nine-bit count ranges from 0 through 464.  The direct first-difference
encoding of `count>=10` emits one clause for each set bit of
`10=000001010_2`, namely two clauses per counter and thirty total.  Exhausting
all 512 bit vectors confirms that these clauses are equivalent to the
unsigned comparison.

Therefore the exact incremental total is

```text
variables = 6,960+13,800       = 20,760,
clauses   = 27,840+96,600+30  = 124,470.
```

This assumes only that the existing `y[b,i]` references and true constant
are retained.  Retaining them adds no variable or clause.

## 6. Checker and nonredundancy scope

The checker passes and independently verifies:

* the `p<=9` capacity maximum thirteen;
* both sharp ten-position gadgets;
* all sixteen assignments of the strict-support gate;
* all 512 inputs of the `>=10` comparator;
* the `452+8` full-adder count and complete inventory;
* an actual Type-I-shaped rank/support/facet/onion/lex multiset with one
  strict ridge load equal to nine.

The current certificate is stronger than a scalar six-set moment witness:
its actual pointwise support minima for subcube ranks `1,...,10` are

```text
1,2,5,9,18,33,61,108,187,297,
```

and its six actual endpoint-facet loads are

```text
38,26,41,43,42,42.
```

Among all fifteen endpoint ridges its strict loads range from 9 to 26, and
only `T\{0,1}` is below ten.  The assigned width vectors satisfy all quoted
numeric width rows, but the checker does not construct their selected
witness intervals.  This is exactly why the certificate should be cited as
a separation from the displayed auxiliary projection, not as a CNF model or
universal word.

The audited artifact hashes are

```text
7406bbfb1da62afcc97da04045d08f595318bfca5b72867900ec08b86b9570ac  K11_TYPE1_BOUNDARY_RIDGE_PIN_LOAD.md
6a7425a304c39d89f445db0908d31a0151af6591f9c9e78b10dea937780a1c0f  scratch/check_k11_type1_boundary_ridge_pin_load.py
```

## 7. Final scope

The theorem is globally WLOG within the exact Type-I branch and is genuinely
coordinate-sensitive.  It changes no mathematical bound by itself.  A SAT
candidate still needs exhaustive OR verification, and an UNSAT conclusion
still needs a checked proof trace.
