#!/usr/bin/env python3
"""Exact r=3 punctured-slice check for the first G.168 local cluster."""

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


M_ORDER = 12
TAIL_A = Fraction(11, 10)


def falling(n, k):
    out = 1
    for i in range(k):
        out *= n - i
    return out


def make_catalogue(r=3):
    b = 2 * r + 1
    targets = (
        [("M", s) for s in combinations(range(b), r)]
        + [("L", s) for s in combinations(range(b), r - 1)]
    )
    target_index = {t: i for i, t in enumerate(targets)}
    rows = set()
    for w in permutations(range(b)):
        row = []
        for start in range(1, b):
            middle = tuple(sorted(w[(start + j) % b] for j in range(r)))
            lower = tuple(sorted(w[(start + j) % b] for j in range(r - 1)))
            row.append(target_index[("M", middle)])
            row.append(target_index[("L", lower)])
        rows.add(tuple(sorted(row)))
    rows = sorted(rows)
    row_masks = [sum(1 << v for v in row) for row in rows]
    incidence = [
        sum(1 << i for i, row in enumerate(rows) if v in row)
        for v in range(len(targets))
    ]
    conflicts = []
    for row in rows:
        mask = 0
        for v in row:
            mask |= incidence[v]
        conflicts.append(mask)
    return targets, target_index, rows, row_masks, incidence, conflicts


def residual_roots(data, missing_middle, missing_lower, r=3):
    targets, target_index, rows, row_masks, incidence, conflicts = data
    state = (1 << len(targets)) - 1
    state &= ~(1 << target_index[("M", tuple(sorted(missing_middle)))])
    state &= ~(1 << target_index[("L", tuple(sorted(missing_lower)))])
    alive = 0
    for i, row_mask in enumerate(row_masks):
        if row_mask & ~state == 0:
            alive |= 1 << i
    alive_rows = [i for i in range(len(rows)) if alive & (1 << i)]
    Z = len(alive_rows)
    n = {"M": 34, "L": 20}
    z = {shore: Fraction(2 * r * Z, n[shore]) for shore in n}
    degrees = [(incidence[v] & alive).bit_count() for v in range(len(targets))]
    conflict_degree = {i: (conflicts[i] & alive).bit_count() for i in alive_rows}
    excess = {
        i: sum(degrees[v] for v in rows[i]) - conflict_degree[i]
        for i in alive_rows
    }

    roots = []
    for v, target in enumerate(targets):
        d = degrees[v]
        if d < M_ORDER:
            continue
        star = incidence[v] & alive
        star_rows = [i for i in alive_rows if star & (1 << i)]
        companion_raw = Fraction(
            sum(
                sum(degrees[u] for u in rows[i] if u != v)
                for i in star_rows
            ),
            d,
        )
        jv = Fraction(sum(excess[i] for i in star_rows), d)
        centered_companions = companion_raw - (
            5 * z[target[0]] + 6 * z["L" if target[0] == "M" else "M"]
        )
        u_real = (centered_companions - jv) / z[target[0]]

        dbar = Fraction(0, 1)
        for g in alive_rows:
            if v in rows[g]:
                continue
            ag = (star & conflicts[g]).bit_count()
            if not ag:
                continue
            dbar += (
                Fraction(M_ORDER * ag, d)
                - 1
                + Fraction(falling(d - ag, M_ORDER), falling(d, M_ORDER))
            )
        roots.append(
            {
                "shore": target[0],
                "d": d,
                "z": z[target[0]],
                "u_real": u_real,
                "raw_minus_j": companion_raw - jv,
                "q_real": dbar / z[target[0]],
                "mass": falling(d, M_ORDER),
            }
        )
    return Z, roots


def summarize(orbits):
    expected_zrows = Fraction(sum(o["count"] * o["Z"] for o in orbits), 735)
    shadow_z = {
        "M": Fraction(6, 34) * expected_zrows,
        "L": Fraction(6, 20) * expected_zrows,
    }
    output = {}
    for shore in ("M", "L"):
        base_mass = Fraction(0)
        base_real_u = Fraction(0)
        base_shadow_u = Fraction(0)
        base_x = Fraction(0)
        tail_mass = Fraction(0)
        tail_real_u = Fraction(0)
        tail_shadow_u = Fraction(0)
        tail_x = Fraction(0)
        base_real_q = Fraction(0)
        tail_real_q = Fraction(0)
        orbit_base = []
        orbit_tail = []
        for orbit in orbits:
            local_base = Fraction(0)
            local_tail = Fraction(0)
            for root in orbit["roots"]:
                if root["shore"] != shore:
                    continue
                mass = Fraction(root["mass"])
                xval = Fraction(root["d"], 1) / root["z"]
                psi = Fraction(0) if xval <= TAIL_A else ((xval - TAIL_A) / xval) ** M_ORDER
                other = "L" if shore == "M" else "M"
                shadow_u = (
                    root["raw_minus_j"]
                    - 5 * shadow_z[shore]
                    - 6 * shadow_z[other]
                ) / shadow_z[shore]
                weight = orbit["count"] * mass
                base_mass += weight
                base_real_u += weight * root["u_real"]
                base_shadow_u += weight * shadow_u
                base_x += weight * xval
                base_real_q += weight * root["q_real"]
                tail_mass += weight * psi
                tail_real_u += weight * psi * root["u_real"]
                tail_shadow_u += weight * psi * shadow_u
                tail_x += weight * psi * xval
                tail_real_q += weight * psi * root["q_real"]
                local_base += weight
                local_tail += weight * psi
            orbit_base.append(local_base)
            orbit_tail.append(local_tail)
        assert tail_mass > 0
        real_deficit = base_real_u / base_mass - tail_real_u / tail_mass
        duplicate_shift = tail_real_q / tail_mass - base_real_q / base_mass
        degree_shift = tail_x / tail_mass - base_x / base_mass
        output[shore] = {
            "real_deficit": real_deficit,
            "shadow_deficit": base_shadow_u / base_mass - tail_shadow_u / tail_mass,
            "tail_q": tail_real_q / tail_mass,
            "base_q": base_real_q / base_mass,
            "duplicate_shift": duplicate_shift,
            "degree_shift": degree_shift,
            "signed_residual": M_ORDER * real_deficit + duplicate_shift,
            "exact_adverse_bracket": M_ORDER * real_deficit + duplicate_shift - degree_shift,
            "tail_fraction": tail_mass / base_mass,
            "orbit_base": [x / base_mass for x in orbit_base],
            "orbit_tail": [x / tail_mass for x in orbit_tail],
        }
    return expected_zrows, shadow_z, output


def complete_catalogue_q(data, shore, target):
    targets, target_index, rows, _, incidence, conflicts = data
    v = target_index[(shore, tuple(sorted(target)))]
    d = incidence[v].bit_count()
    dbar = Fraction(0)
    for g, row in enumerate(rows):
        if v in row:
            continue
        ag = (incidence[v] & conflicts[g]).bit_count()
        dbar += (
            Fraction(M_ORDER * ag, d)
            - 1
            + Fraction(falling(d - ag, M_ORDER), falling(d, M_ORDER))
        )
    return dbar / d


def check_r2_has_no_nonconstant_twelve_carrier_tail():
    data = make_catalogue(r=2)
    targets, _, rows, row_masks, incidence, _ = data
    assert len(targets) == 15 and len(rows) == 120
    saw = {t: 0 for t in range(6)}
    for state in range(1 << len(targets)):
        n_m = sum(
            bool(state & (1 << v)) for v, target in enumerate(targets)
            if target[0] == "M"
        )
        n_l = sum(
            bool(state & (1 << v)) for v, target in enumerate(targets)
            if target[0] == "L"
        )
        if 10 - n_m != 5 - n_l:
            continue
        deleted = 10 - n_m
        alive = 0
        for i, row_mask in enumerate(row_masks):
            if row_mask & ~state == 0:
                alive |= 1 << i
        Z = alive.bit_count()
        if not Z:
            continue
        for v, target in enumerate(targets):
            d = (incidence[v] & alive).bit_count()
            if d < M_ORDER:
                continue
            n_shore = n_m if target[0] == "M" else n_l
            assert Fraction(d, 1) / Fraction(4 * Z, n_shore) == 1
            saw[deleted] += 1
    assert saw[0] > 0 and saw[1] > 0
    assert all(saw[t] == 0 for t in range(2, 6))


def eulerian(m, q):
    row = [1]
    for n in range(2, m + 1):
        nxt = [0] * n
        for k in range(n):
            if k < len(row):
                nxt[k] += (k + 1) * row[k]
            if k:
                nxt[k] += (n - k) * row[k - 1]
        row = nxt
    return row[q]


def check_newton_tail_is_all_order():
    m = M_ORDER
    for c in (12, 20, 50):
        bpoly = [0] * m
        for q in range(m):
            for j in range(m - q):
                bpoly[q + j] += eulerian(m, q) * comb(m - 1 - q, j)
        coefficients = []
        for order in range(c + 61):
            direct = sum(
                (-1) ** (order - d) * comb(order, d) * max(d - c, 0) ** m
                for d in range(order + 1)
            )
            n = order - c - 1
            generated = 0
            if n >= 0:
                for k, value in enumerate(bpoly):
                    if k <= n:
                        generated += (
                            value
                            * (-1) ** (n - k)
                            * comb(c + n - k - 1, n - k)
                        )
            assert direct == generated
            coefficients.append(direct)
        assert all(coefficients[j] != 0 for j in range(2 * c + 1, c + 61))


def main():
    check_r2_has_no_nonconstant_twelve_carrier_tail()
    check_newton_tail_is_all_order()
    data = make_catalogue()
    targets, _, rows, _, _, _ = data
    assert len(targets) == 56
    assert len(rows) == factorial(7) == 5040

    # For a fixed missing 3-set A, the missing 2-set B has respectively
    # 6, 12, and 3 choices with |A cap B|=0,1,2.  Multiply by 35 choices
    # of A to obtain the three exact slice-orbit sizes.
    orbit_specs = [((3, 4), 210, 0), ((0, 3), 420, 1), ((0, 1), 105, 2)]
    assert sum(count for _, count, _ in orbit_specs) == 35 * 21 == 735
    orbits = []
    for missing_lower, count, intersection in orbit_specs:
        Z, roots = residual_roots(data, (0, 1, 2), missing_lower)
        orbits.append(
            {"intersection": intersection, "count": count, "Z": Z, "roots": roots}
        )
    assert [o["Z"] for o in orbits] == [3096, 2856, 3264]
    assert all(len(o["roots"]) == 54 for o in orbits)

    expected_zrows, shadow_z, out = summarize(orbits)
    assert expected_zrows == Fraction(20880, 7)
    assert shadow_z == {"M": Fraction(62640, 119), "L": Fraction(6264, 7)}
    for shore in ("M", "L"):
        assert out[shore]["real_deficit"] > 0
        assert out[shore]["shadow_deficit"] > 0
        assert out[shore]["tail_q"] > 0
        assert out[shore]["degree_shift"] > 0
        assert out[shore]["exact_adverse_bracket"] < 0
        assert sum(out[shore]["orbit_base"]) == 1
        assert sum(out[shore]["orbit_tail"]) == 1

    expected_sign_numerators = {
        ("M", "real_deficit"): 904231771741250389376210136034793803449875647884194265461944964946680871227633935442475058275389963817569289147535720311951579672603830897529073737769654030772906540240575908911136105162037876987,
        ("M", "shadow_deficit"): 158643830038733178428228406482717042344140674431351460099427852320431942562488706024530490388058757379993702146852137930702764152120554641296742172587878552452204036255353536942083894095605955666391,
        ("M", "duplicate_shift"): -4881070546058471135221339887507873018534265612708385636671846147240834863454530617967685368825652187793170223566896066403557507174870064388857514027131506265523414927986490798140578294240890925061,
        ("M", "signed_residual"): 4894428206140578390797801240607974419247237256705361112841771123275148672264725368630284962786554313955949757290372241010915180103799732822353645203316197520400517847831134122987253346496743005077,
        ("M", "degree_shift"): 271966711238256055413095387565589591888614393863342513108627050464679262988069591219189963594578303655954827366736374434931219126160746913986143343252264676665899844230439137253301569783,
        ("M", "exact_adverse_bracket"): -369548696088891025002181168765074738414099621446297655065109076926091197522140444021633997253331327827994011889626516772044961512191328817310001108463819534089553615373744321807145596726523,
        ("L", "real_deficit"): 2228692550519888215676357282676749501097188671293522905991203200742844231310578326625292666947596583410619040762828569303497,
        ("L", "shadow_deficit"): 273748632318424532152289871947818418516014692191144713750938350911749887136402355772478511188145226206119208948656244302707,
        ("L", "duplicate_shift"): -158689554020805098208513802479030428093171070083412398328380880609141048985345376056240516170179100664267918341138698648211001067,
        ("L", "signed_residual"): 17756035203854451826583403590487829908693357022895810138942676793669928807513110062683904272062120844350791116054439183546856423,
        ("L", "degree_shift"): 645402352187757643279190704033488691736942227726214350786382111939324075472366412901935688072813707925112141087878991235,
        ("L", "exact_adverse_bracket"): -6767728329157648701416148372839704672930507719396591828803590472075279466674333527764849471129512968447662637369594351,
    }
    for (shore, key), numerator in expected_sign_numerators.items():
        assert out[shore][key].numerator == numerator

    assert complete_catalogue_q(data, "M", (0, 1, 2)) == Fraction(
        1742622313209714743834173067, 38605786469923192839501588
    )
    assert complete_catalogue_q(data, "L", (0, 1)) == Fraction(
        10786553612545176544411761570383, 475527712495542578401072715640
    )

    print("PASS: exact r=3 punctured two-slice local-cluster obstruction")
    for shore in ("M", "L"):
        q = out[shore]
        print(
            f"  {shore}: real deficit={float(q['real_deficit']):.12g}, "
            f"shadow deficit={float(q['shadow_deficit']):.12g}, "
            f"E Q={float(q['base_q']):.12g}, "
            f"E_tau Q={float(q['tail_q']):.12g}, "
            f"Q shift={float(q['duplicate_shift']):+.12g}, "
            f"mU+Qshift={float(q['signed_residual']):+.12g}, "
            f"degree shift={float(q['degree_shift']):+.12g}, "
            f"exact bracket={float(q['exact_adverse_bracket']):+.12g}, "
            f"tail mass={float(q['tail_fraction']):.12g}"
        )
        print(
            "    orbit masses |A∩B|=0,1,2: baseline="
            + ",".join(f"{float(x):.8f}" for x in q["orbit_base"])
            + " tail="
            + ",".join(f"{float(x):.8f}" for x in q["orbit_tail"])
        )


if __name__ == "__main__":
    main()
