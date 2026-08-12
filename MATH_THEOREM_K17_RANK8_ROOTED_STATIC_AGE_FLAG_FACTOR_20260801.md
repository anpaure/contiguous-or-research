# `k=17`: exact rank-eight-rooted static age-flag factor

Date: 2026-08-01

Status: unconditional finite theorem with a compact independently replayable
certificate.  It closes the static necklace flag-factor gate.  It does not
construct changing-owner transitions, a quotient owner cycle, strict-upper
witnesses, or an upper-safe physical opening.

## 1. Root at the deepest suffix, not at the owner

Let

\[
 \mathcal N_s=\binom{\mathbb Z_{17}}s/\mathbb Z_{17}.
\]

All ranks used below are free under rotation.  In particular

\[
 |\mathcal N_8|=|\mathcal N_9|=1430.
\]

Every certified age type has the form

\[
 c=(c_0,c_1,c_2,1),\qquad c_0+c_1+c_2=8.
\]

Therefore first forget the rank-nine owner and root a flag directly at a
rank-eight necklace `Q`.  A rooted flag is a partition

\[
 Q=C_0\mathbin{\dot\cup}C_1\mathbin{\dot\cup}C_2
 \tag{1.1}
\]

of one of the nine certified types.  It emits

\[
 [C_0],\qquad[C_0\cup C_1],\qquad[Q].               \tag{1.2}
\]

The rank-eight target is automatic: use one flag at each `Q in N_8`.
Only ranks two through seven remain as tight exact-cover constraints.

The nine type masses are

\[
 (139,297,8,20,20,140,127,237,442).                 \tag{1.3}
\]

## 2. Owner attachment is automatic

Form the quotient incidence multigraph between `N_8` and `N_9`, retaining
aligned containments modulo simultaneous rotation.

### Lemma 2.1

This is a 9-regular bipartite multigraph and hence has a perfect matching.

### Proof

A physical rank-eight set has exactly nine rank-nine supersets.  A physical
rank-nine set has exactly nine rank-eight subsets.  Freeness of both cyclic
actions carries these aligned incidences to quotient multidegrees nine.

For any left vertex family `X`, its `9|X|` incident multiedges end in
`N(X)`, and every right vertex receives at most nine of them.  Thus

\[
 |N(X)|\ge |X|.
\]

Hall gives a perfect matching. \(\square\)

For a matched aligned containment `Q subset T`, set

\[
 C_3=T-Q.
\]

This is a singleton.  The perfect matching uses every rank-nine owner once,
so any rank-eight-rooted factor lifts to a full static owner age factor.

## 3. Exact rooted certificate

The file

```text
scratch/k17_rank8_rooted_static_age_flag_20260801.certificate.tsv
```

contains one row for every rank-eight necklace representative.  Each row
records its type, the literal classes `C0,C1,C2`, and the first two suffix
necklace representatives.

The independent standalone `-O3` verifier

```text
scratch/verify_k17_rank8_rooted_static_certificate_20260801.cpp
```

checks:

1. all 1430 rank-eight roots occur exactly once;
2. `C0,C1,C2` partition the declared root with the declared type;
3. the nine type multiplicities are exactly (1.3);
4. every target necklace at ranks two through seven occurs exactly once;
5. at least one singleton suffix occurs.

It reports

```text
PASS_K17_RANK8_ROOTED_STATIC_CERTIFICATE
roots=1430 tight_target_orbits=2424
```

The certificate SHA256 is

```text
ad9e15f724b5048c00cf43ae007d0e02c03c72204a5c169736461e946a166eab
```

The separate projector which derives this certificate from the full
owner-rooted certificate and independently rechecks the projection is

```text
scratch/project_verify_k17_rank8_rooted_static_certificate_20260801.cpp
```

### Theorem 3.1

There exists a static `k=17` age-flag factor with the certified type masses
which covers every target necklace at ranks two through eight exactly once
and has a singleton suffix.

### Proof

The compact certificate proves the rooted factor at ranks one through eight.
Apply Lemma 2.1 and append the matched singleton `C3` to every rooted flag.
The resulting 1430 age flags use every rank-nine owner once and retain all
lower suffixes. \(\square\)

## 4. Factorized exact model

The certificate was found through the equivalent factorized model generated
by

```text
scratch/build_k17_rank8_rooted_static_age_flag_cnf_20260801.cpp
```

The H100 `-O3` materialization has

```text
rank-eight roots                  1,430
raw flags per root               1,904
raw flag variables avoided   2,722,720
suffix choices                 403,260
variables                    3,318,036
clauses                     12,385,099
CNF size                          272 MB
generator wall time                1.65 s
generator max RSS                    8 MB
```

The raw menu count is smaller than the owner-rooted menu by exactly a factor
of nine: the omitted choice is the oldest singleton/owner extension, which
Lemma 2.1 supplies afterward by matching.

## 5. Scope

The following are now proved:

* the exact certified type multiset can be realized integrally;
* its nested suffix flags cover every lower target orbit at ranks two
  through eight exactly once; and
* distinct rank-nine owners can be attached afterward.

The following do not follow:

* compatibility of consecutive flags under the changing-owner survivor
  relation;
* residence along any fixed owner chronology;
* a connected nonzero-voltage quotient cycle;
* strict-upper or arbitrary-width owner witnesses; or
* a physical upper-safe opening.

Indeed, the published MMM quotient cycle is an exact negative calibration:
its owner-run minimum is two, so it cannot carry a depth-three age lift.
The remaining owner cycle must be chosen jointly with the certified static
flags.

There is an equally sharp negative in the other order of quantifiers.  If
the full owner attachment appearing in the independently found static
certificate is frozen and one then asks for changing-owner-compatible
Johnson arcs, the exact compatibility graph has only 93 non-self arcs:

```text
zero-out owners     1,338
zero-in owners      1,340
maximum matching       89
deficiency           1,341
```

This is replayed by

```text
scratch/audit_k17_static_flag_changing_owner_matching_20260801.cpp
```

Thus both sequential strategies fail on explicit certified objects:

* owner cycle first, age decoration afterward: the MMM run obstruction;
* static flags plus arbitrary owners first, transitions afterward: matching
  deficiency 1,341.

The live object is necessarily the joint owner/age/transition selector
encoded by the free-cycle lower/owner skeleton.
